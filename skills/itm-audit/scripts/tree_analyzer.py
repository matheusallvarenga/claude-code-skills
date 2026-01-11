#!/usr/bin/env python3
"""
ITM Audit System - Tree Analyzer
Generates hierarchical directory structure with size analysis.

Part of Phase 1.5 (between SCAN and HASH) or standalone.
"""

import os
import sys
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def format_size(size: int) -> str:
    """Format bytes to human readable string."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def get_dir_size(path: str) -> int:
    """Calculate total size of a directory."""
    total = 0
    try:
        for entry in os.scandir(path):
            try:
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += get_dir_size(entry.path)
            except (PermissionError, OSError):
                continue
    except (PermissionError, OSError):
        pass
    return total


@dataclass
class TreeNode:
    """Represents a directory in the tree."""
    name: str
    path: str
    size: int = 0
    files_count: int = 0
    dirs_count: int = 0
    depth: int = 0
    children: List[Dict] = None
    
    def __post_init__(self):
        if self.children is None:
            self.children = []
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "path": self.path,
            "size": self.size,
            "size_formatted": format_size(self.size),
            "files_count": self.files_count,
            "dirs_count": self.dirs_count,
            "depth": self.depth,
            "children": self.children
        }


class TreeAnalyzer:
    """Analyzes and generates directory tree structure."""
    
    def __init__(self, max_depth: int = 5, include_hidden: bool = False):
        self.max_depth = max_depth
        self.include_hidden = include_hidden
        self.stats = {
            "total_dirs": 0,
            "total_files": 0,
            "total_size": 0,
            "max_depth_reached": 0,
            "largest_dirs": [],
            "deepest_paths": []
        }
    
    def analyze(self, root_path: str) -> Dict[str, Any]:
        """
        Analyze directory structure and return tree with statistics.
        
        Args:
            root_path: Path to analyze
            
        Returns:
            Dictionary with tree structure and statistics
        """
        root = Path(root_path).resolve()
        if not root.exists():
            raise ValueError(f"Path does not exist: {root_path}")
        if not root.is_dir():
            raise ValueError(f"Path is not a directory: {root_path}")
        
        logger.info(f"🌳 Analyzing tree structure: {root}")
        
        # Reset stats
        self.stats = {
            "total_dirs": 0,
            "total_files": 0,
            "total_size": 0,
            "max_depth_reached": 0,
            "largest_dirs": [],
            "deepest_paths": []
        }
        
        # Build tree
        tree = self._build_tree(str(root), depth=0)
        
        # Calculate statistics
        self._calculate_stats(tree)
        
        # Sort largest dirs
        self.stats["largest_dirs"] = sorted(
            self.stats["largest_dirs"],
            key=lambda x: x["size"],
            reverse=True
        )[:20]
        
        result = {
            "metadata": {
                "root_path": str(root),
                "analyzed_at": datetime.now().isoformat(),
                "max_depth": self.max_depth,
                "include_hidden": self.include_hidden
            },
            "tree": tree,
            "statistics": self.stats
        }
        
        logger.info(f"✅ Analysis complete: {self.stats['total_dirs']} dirs, {self.stats['total_files']} files")
        
        return result
    
    def _build_tree(self, path: str, depth: int) -> Dict:
        """Recursively build tree structure."""
        node = TreeNode(
            name=os.path.basename(path) or path,
            path=path,
            depth=depth
        )
        
        if depth > self.max_depth:
            node.size = get_dir_size(path)
            return node.to_dict()
        
        try:
            entries = list(os.scandir(path))
        except (PermissionError, OSError) as e:
            logger.warning(f"Cannot access: {path} - {e}")
            return node.to_dict()
        
        dirs = []
        files = []
        
        for entry in entries:
            if not self.include_hidden and entry.name.startswith('.'):
                continue
            try:
                if entry.is_dir(follow_symlinks=False):
                    dirs.append(entry)
                elif entry.is_file(follow_symlinks=False):
                    files.append(entry)
            except (PermissionError, OSError):
                continue
        
        node.files_count = len(files)
        node.dirs_count = len(dirs)
        
        for f in files:
            try:
                node.size += f.stat().st_size
            except (PermissionError, OSError):
                continue
        
        for d in sorted(dirs, key=lambda x: x.name.lower()):
            child = self._build_tree(d.path, depth + 1)
            node.children.append(child)
            node.size += child.get("size", 0)
        
        node.children = sorted(
            node.children,
            key=lambda x: x.get("size", 0),
            reverse=True
        )
        
        return node.to_dict()
    
    def _calculate_stats(self, tree: Dict, path_parts: List[str] = None):
        """Calculate aggregate statistics from tree."""
        if path_parts is None:
            path_parts = []
        
        self.stats["total_dirs"] += 1
        self.stats["total_files"] += tree.get("files_count", 0)
        
        depth = tree.get("depth", 0)
        if depth > self.stats["max_depth_reached"]:
            self.stats["max_depth_reached"] = depth
        
        if tree.get("size", 0) > 0:
            self.stats["largest_dirs"].append({
                "name": tree["name"],
                "path": tree["path"],
                "size": tree["size"],
                "size_formatted": tree.get("size_formatted", format_size(tree["size"])),
                "files_count": tree.get("files_count", 0),
                "depth": depth
            })
        
        if depth == 0:
            self.stats["total_size"] = tree.get("size", 0)
        
        for child in tree.get("children", []):
            self._calculate_stats(child, path_parts + [tree["name"]])

    def generate_markdown(self, result: Dict, include_stats: bool = True) -> str:
        """Generate markdown report from tree analysis."""
        lines = []
        tree = result["tree"]
        stats = result["statistics"]
        meta = result["metadata"]
        
        # Header
        lines.append(f"# 📁 Estrutura de Diretórios: {tree['name']}")
        lines.append("")
        lines.append(f"**Analisado em:** {meta['analyzed_at'][:19].replace('T', ' ')}")
        lines.append(f"**Caminho:** `{meta['root_path']}`")
        lines.append("")
        
        # Summary table
        lines.append("## 📊 Resumo")
        lines.append("")
        lines.append("| Métrica | Valor |")
        lines.append("|---------|-------|")
        lines.append(f"| **Tamanho Total** | {format_size(stats['total_size'])} |")
        lines.append(f"| **Total de Pastas** | {stats['total_dirs']} |")
        lines.append(f"| **Total de Arquivos** | {stats['total_files']} |")
        lines.append(f"| **Profundidade Máxima** | {stats['max_depth_reached']} níveis |")
        lines.append("")
        
        # Top 10 largest directories
        if include_stats and stats["largest_dirs"]:
            lines.append("## 🏆 Top 10 Maiores Pastas")
            lines.append("")
            lines.append("| # | Pasta | Tamanho | Arquivos | Prof. |")
            lines.append("|---|-------|---------|----------|-------|")
            for i, d in enumerate(stats["largest_dirs"][:10], 1):
                name = d["name"][:35] + "..." if len(d["name"]) > 35 else d["name"]
                lines.append(f"| {i} | {name} | {d['size_formatted']} | {d['files_count']} | {d['depth']} |")
            lines.append("")
        
        # Tree structure
        lines.append("## 🌳 Estrutura Hierárquica")
        lines.append("")
        lines.extend(self._tree_to_lines(tree, indent=0))
        
        return "\n".join(lines)
    
    def _tree_to_lines(self, node: Dict, indent: int = 0) -> List[str]:
        """Convert tree node to markdown lines."""
        lines = []
        prefix = "  " * indent
        
        size_str = node.get("size_formatted", format_size(node.get("size", 0)))
        files_info = f"({node.get('files_count', 0)} arquivos)" if node.get('files_count', 0) > 0 else ""
        
        if indent == 0:
            lines.append(f"📁 **{node['name']}** — {size_str} {files_info}")
        else:
            lines.append(f"{prefix}📁 **{node['name']}** — {size_str} {files_info}")
        
        for child in node.get("children", []):
            lines.extend(self._tree_to_lines(child, indent + 1))
        
        return lines


def analyze_tree(
    target_path: str,
    output_dir: str = None,
    max_depth: int = 5,
    include_hidden: bool = False,
    output_format: str = "both",
    report_session_dir: str = None
) -> Dict[str, Any]:
    """
    Convenience function for tree analysis.
    
    Args:
        target_path: Directory to analyze
        output_dir: Where to save results (default: ../data relative to script)
        max_depth: Maximum depth to recurse
        include_hidden: Include hidden files/directories
        output_format: "json", "markdown", or "both"
        report_session_dir: Specific directory for MD report (e.g., audit-reports/20251229_123456/)
    
    Returns:
        Analysis result dictionary
    """
    # Determine output directory
    if output_dir:
        out_path = Path(output_dir)
    else:
        out_path = Path(__file__).parent / "data"
    out_path.mkdir(parents=True, exist_ok=True)
    
    # Run analysis
    analyzer = TreeAnalyzer(max_depth=max_depth, include_hidden=include_hidden)
    result = analyzer.analyze(target_path)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save JSON
    if output_format in ["json", "both"]:
        json_path = out_path / "tree_structure.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        logger.info(f"📄 JSON: {json_path}")
    
    # Save Markdown
    if output_format in ["markdown", "both"]:
        md_content = analyzer.generate_markdown(result)
        if report_session_dir:
            reports_dir = Path(report_session_dir)
        else:
            reports_dir = out_path.parent / "audit-reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        md_path = reports_dir / f"tree_structure_{timestamp}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        logger.info(f"📄 Markdown: {md_path}")
    
    return result


def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="ITM Audit - Tree Analyzer")
    parser.add_argument("path", help="Directory path to analyze")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--max-depth", "-d", type=int, default=5, help="Max depth")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden")
    parser.add_argument("--format", choices=["json", "markdown", "both"], default="both")
    
    args = parser.parse_args()
    
    result = analyze_tree(
        target_path=args.path,
        output_dir=args.output,
        max_depth=args.max_depth,
        include_hidden=args.include_hidden,
        output_format=args.format
    )
    
    stats = result["statistics"]
    print(f"\n{'='*50}")
    print(f"🌳 TREE ANALYSIS COMPLETE")
    print(f"{'='*50}")
    print(f"📁 Root: {args.path}")
    print(f"📊 Total Size: {format_size(stats['total_size'])}")
    print(f"📂 Directories: {stats['total_dirs']}")
    print(f"📄 Files: {stats['total_files']}")
    print(f"📏 Max Depth: {stats['max_depth_reached']}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
