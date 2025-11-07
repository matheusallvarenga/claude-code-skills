#!/usr/bin/env python3
"""
Database Schema Generator
Generates PostgreSQL database schemas with best practices including proper
normalization, indexes, constraints, and audit trails.
"""
import sys
import argparse
import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class DatabaseSchemaGenerator:
    """Generates optimized PostgreSQL schemas from requirements."""

    def __init__(self):
        self.tables = []
        self.relationships = []
        self.enums = []
        self.indexes = []

    def generate_from_requirements(self, requirements: Dict) -> str:
        """Generate schema from requirements dictionary."""
        schema_sql = []

        # Add header
        schema_sql.append(self._generate_header())

        # Create extensions
        schema_sql.append(self._generate_extensions())

        # Create enums
        if 'enums' in requirements:
            for enum_def in requirements['enums']:
                schema_sql.append(self._generate_enum(enum_def))

        # Create tables
        if 'tables' in requirements:
            for table_def in requirements['tables']:
                schema_sql.append(self._generate_table(table_def))

        # Create indexes
        if 'indexes' in requirements:
            for index_def in requirements['indexes']:
                schema_sql.append(self._generate_index(index_def))

        # Create relationships (foreign keys)
        if 'relationships' in requirements:
            for rel_def in requirements['relationships']:
                schema_sql.append(self._generate_relationship(rel_def))

        # Create functions and triggers
        if requirements.get('enable_audit_trail', True):
            schema_sql.append(self._generate_audit_triggers())

        # Add footer
        schema_sql.append(self._generate_footer())

        return '\n\n'.join(schema_sql)

    def _generate_header(self) -> str:
        """Generate schema file header."""
        return f"""-- Database Schema
-- Generated: {datetime.now().isoformat()}
-- Generator: Full-Stack Project Finisher
-- PostgreSQL Version: 14+

-- This schema follows best practices:
-- - UUID primary keys for distributed systems
-- - Audit trail columns (created_at, updated_at)
-- - Soft deletes (deleted_at)
-- - Proper indexes for performance
-- - Foreign key constraints with cascade rules
-- - Check constraints for data validation

BEGIN;"""

    def _generate_extensions(self) -> str:
        """Generate PostgreSQL extensions."""
        return """-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "pg_trgm"; -- For text search optimization"""

    def _generate_enum(self, enum_def: Dict) -> str:
        """Generate ENUM type."""
        name = enum_def['name']
        values = enum_def['values']

        values_str = ', '.join(f"'{v}'" for v in values)
        return f"""-- Enum: {name}
CREATE TYPE {name} AS ENUM ({values_str});"""

    def _generate_table(self, table_def: Dict) -> str:
        """Generate table CREATE statement."""
        table_name = table_def['name']
        columns = table_def.get('columns', [])
        enable_audit = table_def.get('enable_audit', True)
        enable_soft_delete = table_def.get('enable_soft_delete', True)

        sql_parts = [f"-- Table: {table_name}"]

        if table_def.get('description'):
            sql_parts.append(f"-- {table_def['description']}")

        sql_parts.append(f"CREATE TABLE {table_name} (")

        # Primary key (UUID by default)
        pk_column = table_def.get('primary_key', 'id')
        pk_type = table_def.get('primary_key_type', 'UUID')

        if pk_type == 'UUID':
            sql_parts.append(f"    {pk_column} UUID PRIMARY KEY DEFAULT uuid_generate_v4(),")
        elif pk_type == 'SERIAL':
            sql_parts.append(f"    {pk_column} SERIAL PRIMARY KEY,")
        else:
            sql_parts.append(f"    {pk_column} {pk_type} PRIMARY KEY,")

        # Custom columns
        for col in columns:
            sql_parts.append(self._generate_column(col))

        # Audit trail columns
        if enable_audit:
            sql_parts.append("    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,")
            sql_parts.append("    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP NOT NULL,")

        # Soft delete
        if enable_soft_delete:
            sql_parts.append("    deleted_at TIMESTAMP WITH TIME ZONE,")

        # Remove trailing comma from last column
        sql_parts[-1] = sql_parts[-1].rstrip(',')

        sql_parts.append(");")

        # Add table comment
        if table_def.get('description'):
            sql_parts.append(f"COMMENT ON TABLE {table_name} IS '{table_def['description']}';")

        # Create default indexes
        if enable_soft_delete:
            sql_parts.append(f"CREATE INDEX idx_{table_name}_deleted_at ON {table_name}(deleted_at) WHERE deleted_at IS NULL;")

        if enable_audit:
            sql_parts.append(f"CREATE INDEX idx_{table_name}_created_at ON {table_name}(created_at);")

        return '\n'.join(sql_parts)

    def _generate_column(self, col_def: Dict) -> str:
        """Generate column definition."""
        name = col_def['name']
        col_type = col_def['type']
        nullable = col_def.get('nullable', True)
        default = col_def.get('default')
        unique = col_def.get('unique', False)
        check = col_def.get('check')

        parts = [f"    {name} {col_type}"]

        if not nullable:
            parts.append("NOT NULL")

        if default:
            if isinstance(default, str) and default.upper() not in ['CURRENT_TIMESTAMP', 'NOW()']:
                parts.append(f"DEFAULT '{default}'")
            else:
                parts.append(f"DEFAULT {default}")

        if unique:
            parts.append("UNIQUE")

        if check:
            parts.append(f"CHECK ({check})")

        return ' '.join(parts) + ','

    def _generate_relationship(self, rel_def: Dict) -> str:
        """Generate foreign key constraint."""
        from_table = rel_def['from_table']
        from_column = rel_def['from_column']
        to_table = rel_def['to_table']
        to_column = rel_def.get('to_column', 'id')
        on_delete = rel_def.get('on_delete', 'CASCADE')
        on_update = rel_def.get('on_update', 'CASCADE')

        constraint_name = f"fk_{from_table}_{from_column}_{to_table}"

        sql = f"""-- Relationship: {from_table}.{from_column} -> {to_table}.{to_column}
ALTER TABLE {from_table}
    ADD CONSTRAINT {constraint_name}
    FOREIGN KEY ({from_column})
    REFERENCES {to_table}({to_column})
    ON DELETE {on_delete}
    ON UPDATE {on_update};

-- Index for foreign key lookup performance
CREATE INDEX idx_{from_table}_{from_column} ON {from_table}({from_column});"""

        return sql

    def _generate_index(self, index_def: Dict) -> str:
        """Generate index."""
        table = index_def['table']
        columns = index_def['columns']
        index_type = index_def.get('type', 'btree')
        unique = index_def.get('unique', False)
        where = index_def.get('where')

        columns_str = ', '.join(columns)
        index_name = f"idx_{table}_{'_'.join(columns)}"

        unique_str = 'UNIQUE ' if unique else ''

        sql = f"-- Index: {index_name}\n"
        sql += f"CREATE {unique_str}INDEX {index_name} ON {table} USING {index_type} ({columns_str})"

        if where:
            sql += f" WHERE {where}"

        sql += ";"

        return sql

    def _generate_audit_triggers(self) -> str:
        """Generate audit trail triggers."""
        return """-- Audit Trail Function
-- Automatically updates updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply audit trigger to all tables with updated_at column
-- Note: Call this function after creating each table:
-- CREATE TRIGGER trigger_update_timestamp
--     BEFORE UPDATE ON your_table
--     FOR EACH ROW
--     EXECUTE FUNCTION update_updated_at_column();"""

    def _generate_footer(self) -> str:
        """Generate schema file footer."""
        return """-- Commit transaction
COMMIT;

-- Grant permissions (adjust as needed)
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO your_app_user;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO your_app_user;"""


def load_requirements_file(file_path: str) -> Dict:
    """Load requirements from YAML or JSON file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Requirements file not found: {file_path}")

    with open(path, 'r', encoding='utf-8') as f:
        if path.suffix in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        elif path.suffix == '.json':
            return json.load(f)
        else:
            raise ValueError("Requirements file must be .yaml, .yml, or .json")


def create_sample_requirements() -> Dict:
    """Create sample requirements file."""
    return {
        'enums': [
            {
                'name': 'user_role',
                'values': ['admin', 'user', 'guest']
            },
            {
                'name': 'status',
                'values': ['active', 'inactive', 'pending']
            }
        ],
        'tables': [
            {
                'name': 'users',
                'description': 'Application users',
                'primary_key': 'id',
                'primary_key_type': 'UUID',
                'enable_audit': True,
                'enable_soft_delete': True,
                'columns': [
                    {'name': 'email', 'type': 'VARCHAR(255)', 'nullable': False, 'unique': True},
                    {'name': 'username', 'type': 'VARCHAR(100)', 'nullable': False, 'unique': True},
                    {'name': 'password_hash', 'type': 'VARCHAR(255)', 'nullable': False},
                    {'name': 'full_name', 'type': 'VARCHAR(255)', 'nullable': True},
                    {'name': 'role', 'type': 'user_role', 'nullable': False, 'default': 'user'},
                    {'name': 'status', 'type': 'status', 'nullable': False, 'default': 'pending'},
                    {'name': 'last_login_at', 'type': 'TIMESTAMP WITH TIME ZONE', 'nullable': True}
                ]
            },
            {
                'name': 'posts',
                'description': 'User blog posts',
                'primary_key': 'id',
                'primary_key_type': 'UUID',
                'enable_audit': True,
                'enable_soft_delete': True,
                'columns': [
                    {'name': 'user_id', 'type': 'UUID', 'nullable': False},
                    {'name': 'title', 'type': 'VARCHAR(500)', 'nullable': False},
                    {'name': 'slug', 'type': 'VARCHAR(500)', 'nullable': False, 'unique': True},
                    {'name': 'content', 'type': 'TEXT', 'nullable': False},
                    {'name': 'published_at', 'type': 'TIMESTAMP WITH TIME ZONE', 'nullable': True},
                    {'name': 'view_count', 'type': 'INTEGER', 'nullable': False, 'default': '0', 'check': 'view_count >= 0'}
                ]
            },
            {
                'name': 'comments',
                'description': 'Comments on posts',
                'primary_key': 'id',
                'primary_key_type': 'UUID',
                'enable_audit': True,
                'enable_soft_delete': True,
                'columns': [
                    {'name': 'post_id', 'type': 'UUID', 'nullable': False},
                    {'name': 'user_id', 'type': 'UUID', 'nullable': False},
                    {'name': 'content', 'type': 'TEXT', 'nullable': False},
                    {'name': 'parent_comment_id', 'type': 'UUID', 'nullable': True}
                ]
            }
        ],
        'relationships': [
            {
                'from_table': 'posts',
                'from_column': 'user_id',
                'to_table': 'users',
                'to_column': 'id',
                'on_delete': 'CASCADE'
            },
            {
                'from_table': 'comments',
                'from_column': 'post_id',
                'to_table': 'posts',
                'to_column': 'id',
                'on_delete': 'CASCADE'
            },
            {
                'from_table': 'comments',
                'from_column': 'user_id',
                'to_table': 'users',
                'to_column': 'id',
                'on_delete': 'CASCADE'
            },
            {
                'from_table': 'comments',
                'from_column': 'parent_comment_id',
                'to_table': 'comments',
                'to_column': 'id',
                'on_delete': 'CASCADE'
            }
        ],
        'indexes': [
            {
                'table': 'posts',
                'columns': ['published_at'],
                'where': 'published_at IS NOT NULL AND deleted_at IS NULL'
            },
            {
                'table': 'posts',
                'columns': ['slug'],
                'unique': True
            },
            {
                'table': 'comments',
                'columns': ['post_id', 'created_at']
            },
            {
                'table': 'users',
                'columns': ['email'],
                'type': 'btree'
            }
        ],
        'enable_audit_trail': True
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate PostgreSQL database schema with best practices',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate schema from requirements file
  python generate_db_schema.py --requirements schema-requirements.yaml --output schema.sql

  # Generate sample requirements file
  python generate_db_schema.py --create-sample requirements.yaml

  # Generate schema from sample and output to stdout
  python generate_db_schema.py --sample
        """
    )

    parser.add_argument(
        '--requirements', '-r',
        help='Path to requirements file (YAML or JSON)'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output SQL file path (default: stdout)'
    )
    parser.add_argument(
        '--create-sample', '-s',
        metavar='FILE',
        help='Create a sample requirements file'
    )
    parser.add_argument(
        '--sample',
        action='store_true',
        help='Generate schema from sample requirements'
    )

    args = parser.parse_args()

    # Create sample requirements file
    if args.create_sample:
        sample = create_sample_requirements()
        output_path = Path(args.create_sample)

        if output_path.suffix in ['.yaml', '.yml']:
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(sample, f, default_flow_style=False, sort_keys=False)
        else:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(sample, f, indent=2)

        print(f"✅ Sample requirements created: {output_path}")
        print(f"\n📝 Edit this file to define your schema, then run:")
        print(f"   python generate_db_schema.py -r {output_path} -o schema.sql")
        return

    # Load requirements
    if args.sample:
        requirements = create_sample_requirements()
    elif args.requirements:
        try:
            requirements = load_requirements_file(args.requirements)
        except Exception as e:
            print(f"❌ Error loading requirements: {e}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    # Generate schema
    generator = DatabaseSchemaGenerator()
    schema_sql = generator.generate_from_requirements(requirements)

    # Output
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(schema_sql)
        print(f"✅ Schema generated: {output_path}")
    else:
        print(schema_sql)


if __name__ == '__main__':
    main()
