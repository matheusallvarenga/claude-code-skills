Activate Obsidian vault enhancement agents.

Available agents for PKM/Obsidian:

1. **connection-agent**: Discover links between notes
   - Entity-based connections
   - Keyword overlap analysis
   - Orphaned note detection
   - Link suggestion reports

2. **moc-agent**: Maps of Content
   - Identify missing MOCs
   - Generate from template
   - Organize orphaned images
   - Maintain MOC network

3. **metadata-agent**: Frontmatter standardization
   - Add missing metadata
   - Extract creation dates
   - Generate tags from content
   - Ensure consistency

4. **tag-agent**: Tag taxonomy
   - Normalize tech names (LangChain, OpenAI)
   - Hierarchical structure (ai/agents)
   - Consolidate duplicates
   - Max 3 levels deep

5. **review-agent**: Quality assurance
   - Validate other agents' work
   - Check metadata consistency
   - Verify link quality
   - Generate quality metrics

Workflow: metadata-agent → tag-agent → connection-agent → moc-agent → review-agent
