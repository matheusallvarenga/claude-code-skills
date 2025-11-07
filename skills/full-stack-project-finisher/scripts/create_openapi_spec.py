#!/usr/bin/env python3
"""
OpenAPI Specification Generator
Generates OpenAPI 3.0 specifications for RESTful APIs with best practices
including proper schemas, security, error handling, and documentation.
"""
import sys
import argparse
import yaml
import json
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class OpenAPIGenerator:
    """Generates OpenAPI 3.0 specifications from endpoint definitions."""

    def __init__(self, title: str, version: str = "1.0.0", description: str = ""):
        self.spec = {
            'openapi': '3.0.3',
            'info': {
                'title': title,
                'version': version,
                'description': description,
                'contact': {},
                'license': {
                    'name': 'MIT',
                    'url': 'https://opensource.org/licenses/MIT'
                }
            },
            'servers': [],
            'paths': {},
            'components': {
                'schemas': {},
                'securitySchemes': {},
                'responses': {},
                'parameters': {}
            },
            'tags': []
        }

    def add_server(self, url: str, description: str = ""):
        """Add a server URL."""
        self.spec['servers'].append({
            'url': url,
            'description': description
        })

    def add_tag(self, name: str, description: str = ""):
        """Add a tag for grouping endpoints."""
        self.spec['tags'].append({
            'name': name,
            'description': description
        })

    def add_security_scheme(self, name: str, scheme_type: str, **kwargs):
        """Add a security scheme (JWT, OAuth2, API Key, etc.)."""
        self.spec['components']['securitySchemes'][name] = {
            'type': scheme_type,
            **kwargs
        }

    def add_common_responses(self):
        """Add common error responses."""
        self.spec['components']['responses'] = {
            'BadRequest': {
                'description': 'Bad Request - Invalid input',
                'content': {
                    'application/json': {
                        'schema': {'$ref': '#/components/schemas/Error'}
                    }
                }
            },
            'Unauthorized': {
                'description': 'Unauthorized - Authentication required',
                'content': {
                    'application/json': {
                        'schema': {'$ref': '#/components/schemas/Error'}
                    }
                }
            },
            'Forbidden': {
                'description': 'Forbidden - Insufficient permissions',
                'content': {
                    'application/json': {
                        'schema': {'$ref': '#/components/schemas/Error'}
                    }
                }
            },
            'NotFound': {
                'description': 'Not Found - Resource does not exist',
                'content': {
                    'application/json': {
                        'schema': {'$ref': '#/components/schemas/Error'}
                    }
                }
            },
            'InternalServerError': {
                'description': 'Internal Server Error',
                'content': {
                    'application/json': {
                        'schema': {'$ref': '#/components/schemas/Error'}
                    }
                }
            }
        }

        # Add standard error schema
        self.spec['components']['schemas']['Error'] = {
            'type': 'object',
            'required': ['error', 'message'],
            'properties': {
                'error': {
                    'type': 'string',
                    'description': 'Error code'
                },
                'message': {
                    'type': 'string',
                    'description': 'Human-readable error message'
                },
                'details': {
                    'type': 'object',
                    'description': 'Additional error details'
                }
            }
        }

    def add_schema(self, name: str, schema: Dict):
        """Add a reusable schema component."""
        self.spec['components']['schemas'][name] = schema

    def add_endpoint(self, path: str, method: str, operation: Dict):
        """Add an API endpoint."""
        if path not in self.spec['paths']:
            self.spec['paths'][path] = {}

        self.spec['paths'][path][method.lower()] = operation

    def generate_crud_endpoints(self, resource: str, schema: Dict, tag: str = None):
        """Generate standard CRUD endpoints for a resource."""
        if tag is None:
            tag = resource.title()

        resource_lower = resource.lower()
        resource_title = resource.title()

        # Add schema
        self.add_schema(resource_title, schema)

        # List endpoint
        self.add_endpoint(
            f'/{resource_lower}',
            'GET',
            {
                'summary': f'List {resource_lower}',
                'description': f'Retrieve a list of {resource_lower} with pagination',
                'tags': [tag],
                'parameters': [
                    {
                        'name': 'page',
                        'in': 'query',
                        'schema': {'type': 'integer', 'default': 1, 'minimum': 1}
                    },
                    {
                        'name': 'limit',
                        'in': 'query',
                        'schema': {'type': 'integer', 'default': 20, 'minimum': 1, 'maximum': 100}
                    },
                    {
                        'name': 'sort',
                        'in': 'query',
                        'schema': {'type': 'string'},
                        'description': 'Sort field and order (e.g., created_at:desc)'
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Successful response',
                        'content': {
                            'application/json': {
                                'schema': {
                                    'type': 'object',
                                    'properties': {
                                        'data': {
                                            'type': 'array',
                                            'items': {'$ref': f'#/components/schemas/{resource_title}'}
                                        },
                                        'pagination': {
                                            'type': 'object',
                                            'properties': {
                                                'page': {'type': 'integer'},
                                                'limit': {'type': 'integer'},
                                                'total': {'type': 'integer'},
                                                'pages': {'type': 'integer'}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    '400': {'$ref': '#/components/responses/BadRequest'},
                    '401': {'$ref': '#/components/responses/Unauthorized'},
                    '500': {'$ref': '#/components/responses/InternalServerError'}
                }
            }
        )

        # Create endpoint
        self.add_endpoint(
            f'/{resource_lower}',
            'POST',
            {
                'summary': f'Create {resource_lower}',
                'description': f'Create a new {resource_lower}',
                'tags': [tag],
                'requestBody': {
                    'required': True,
                    'content': {
                        'application/json': {
                            'schema': {'$ref': f'#/components/schemas/{resource_title}'}
                        }
                    }
                },
                'responses': {
                    '201': {
                        'description': 'Successfully created',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': f'#/components/schemas/{resource_title}'}
                            }
                        }
                    },
                    '400': {'$ref': '#/components/responses/BadRequest'},
                    '401': {'$ref': '#/components/responses/Unauthorized'},
                    '500': {'$ref': '#/components/responses/InternalServerError'}
                }
            }
        )

        # Get by ID endpoint
        self.add_endpoint(
            f'/{resource_lower}/{{id}}',
            'GET',
            {
                'summary': f'Get {resource_lower} by ID',
                'description': f'Retrieve a specific {resource_lower} by ID',
                'tags': [tag],
                'parameters': [
                    {
                        'name': 'id',
                        'in': 'path',
                        'required': True,
                        'schema': {'type': 'string', 'format': 'uuid'}
                    }
                ],
                'responses': {
                    '200': {
                        'description': 'Successful response',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': f'#/components/schemas/{resource_title}'}
                            }
                        }
                    },
                    '401': {'$ref': '#/components/responses/Unauthorized'},
                    '404': {'$ref': '#/components/responses/NotFound'},
                    '500': {'$ref': '#/components/responses/InternalServerError'}
                }
            }
        )

        # Update endpoint
        self.add_endpoint(
            f'/{resource_lower}/{{id}}',
            'PATCH',
            {
                'summary': f'Update {resource_lower}',
                'description': f'Update an existing {resource_lower}',
                'tags': [tag],
                'parameters': [
                    {
                        'name': 'id',
                        'in': 'path',
                        'required': True,
                        'schema': {'type': 'string', 'format': 'uuid'}
                    }
                ],
                'requestBody': {
                    'required': True,
                    'content': {
                        'application/json': {
                            'schema': {'$ref': f'#/components/schemas/{resource_title}'}
                        }
                    }
                },
                'responses': {
                    '200': {
                        'description': 'Successfully updated',
                        'content': {
                            'application/json': {
                                'schema': {'$ref': f'#/components/schemas/{resource_title}'}
                            }
                        }
                    },
                    '400': {'$ref': '#/components/responses/BadRequest'},
                    '401': {'$ref': '#/components/responses/Unauthorized'},
                    '404': {'$ref': '#/components/responses/NotFound'},
                    '500': {'$ref': '#/components/responses/InternalServerError'}
                }
            }
        )

        # Delete endpoint
        self.add_endpoint(
            f'/{resource_lower}/{{id}}',
            'DELETE',
            {
                'summary': f'Delete {resource_lower}',
                'description': f'Delete an existing {resource_lower}',
                'tags': [tag],
                'parameters': [
                    {
                        'name': 'id',
                        'in': 'path',
                        'required': True,
                        'schema': {'type': 'string', 'format': 'uuid'}
                    }
                ],
                'responses': {
                    '204': {
                        'description': 'Successfully deleted'
                    },
                    '401': {'$ref': '#/components/responses/Unauthorized'},
                    '404': {'$ref': '#/components/responses/NotFound'},
                    '500': {'$ref': '#/components/responses/InternalServerError'}
                }
            }
        )

    def to_yaml(self) -> str:
        """Export spec as YAML."""
        return yaml.dump(self.spec, default_flow_style=False, sort_keys=False)

    def to_json(self) -> str:
        """Export spec as JSON."""
        return json.dumps(self.spec, indent=2)


def create_sample_api() -> OpenAPIGenerator:
    """Create a sample API specification."""
    api = OpenAPIGenerator(
        title="Sample Blog API",
        version="1.0.0",
        description="A sample blog API demonstrating OpenAPI best practices"
    )

    # Add servers
    api.add_server("https://api.example.com/v1", "Production")
    api.add_server("https://staging-api.example.com/v1", "Staging")
    api.add_server("http://localhost:3000/v1", "Local development")

    # Add tags
    api.add_tag("Authentication", "User authentication and authorization")
    api.add_tag("Users", "User management")
    api.add_tag("Posts", "Blog post management")
    api.add_tag("Comments", "Comment management")

    # Add security schemes
    api.add_security_scheme(
        "bearerAuth",
        "http",
        scheme="bearer",
        bearerFormat="JWT"
    )

    # Add common responses
    api.add_common_responses()

    # Define schemas
    user_schema = {
        'type': 'object',
        'required': ['id', 'email', 'username'],
        'properties': {
            'id': {'type': 'string', 'format': 'uuid'},
            'email': {'type': 'string', 'format': 'email'},
            'username': {'type': 'string', 'minLength': 3, 'maxLength': 50},
            'full_name': {'type': 'string', 'maxLength': 255},
            'role': {'type': 'string', 'enum': ['admin', 'user', 'guest']},
            'created_at': {'type': 'string', 'format': 'date-time'},
            'updated_at': {'type': 'string', 'format': 'date-time'}
        }
    }

    post_schema = {
        'type': 'object',
        'required': ['id', 'title', 'content', 'user_id'],
        'properties': {
            'id': {'type': 'string', 'format': 'uuid'},
            'user_id': {'type': 'string', 'format': 'uuid'},
            'title': {'type': 'string', 'maxLength': 500},
            'slug': {'type': 'string', 'maxLength': 500},
            'content': {'type': 'string'},
            'published_at': {'type': 'string', 'format': 'date-time', 'nullable': True},
            'view_count': {'type': 'integer', 'minimum': 0},
            'created_at': {'type': 'string', 'format': 'date-time'},
            'updated_at': {'type': 'string', 'format': 'date-time'}
        }
    }

    comment_schema = {
        'type': 'object',
        'required': ['id', 'post_id', 'user_id', 'content'],
        'properties': {
            'id': {'type': 'string', 'format': 'uuid'},
            'post_id': {'type': 'string', 'format': 'uuid'},
            'user_id': {'type': 'string', 'format': 'uuid'},
            'content': {'type': 'string', 'maxLength': 2000},
            'parent_comment_id': {'type': 'string', 'format': 'uuid', 'nullable': True},
            'created_at': {'type': 'string', 'format': 'date-time'},
            'updated_at': {'type': 'string', 'format': 'date-time'}
        }
    }

    # Generate CRUD endpoints
    api.generate_crud_endpoints('user', user_schema, 'Users')
    api.generate_crud_endpoints('post', post_schema, 'Posts')
    api.generate_crud_endpoints('comment', comment_schema, 'Comments')

    # Add authentication endpoints
    api.add_endpoint(
        '/auth/register',
        'POST',
        {
            'summary': 'Register new user',
            'tags': ['Authentication'],
            'requestBody': {
                'required': True,
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'required': ['email', 'username', 'password'],
                            'properties': {
                                'email': {'type': 'string', 'format': 'email'},
                                'username': {'type': 'string', 'minLength': 3},
                                'password': {'type': 'string', 'minLength': 8},
                                'full_name': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            'responses': {
                '201': {
                    'description': 'User registered successfully',
                    'content': {
                        'application/json': {
                            'schema': {
                                'type': 'object',
                                'properties': {
                                    'user': {'$ref': '#/components/schemas/User'},
                                    'token': {'type': 'string'}
                                }
                            }
                        }
                    }
                },
                '400': {'$ref': '#/components/responses/BadRequest'},
                '500': {'$ref': '#/components/responses/InternalServerError'}
            }
        }
    )

    api.add_endpoint(
        '/auth/login',
        'POST',
        {
            'summary': 'Login user',
            'tags': ['Authentication'],
            'requestBody': {
                'required': True,
                'content': {
                    'application/json': {
                        'schema': {
                            'type': 'object',
                            'required': ['email', 'password'],
                            'properties': {
                                'email': {'type': 'string', 'format': 'email'},
                                'password': {'type': 'string'}
                            }
                        }
                    }
                }
            },
            'responses': {
                '200': {
                    'description': 'Login successful',
                    'content': {
                        'application/json': {
                            'schema': {
                                'type': 'object',
                                'properties': {
                                    'user': {'$ref': '#/components/schemas/User'},
                                    'token': {'type': 'string'}
                                }
                            }
                        }
                    }
                },
                '401': {'$ref': '#/components/responses/Unauthorized'},
                '500': {'$ref': '#/components/responses/InternalServerError'}
            }
        }
    )

    return api


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate OpenAPI 3.0 specification with best practices',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate sample API specification
  python create_openapi_spec.py --sample --output api-spec.yaml

  # Generate JSON format
  python create_openapi_spec.py --sample --output api-spec.json --format json
        """
    )

    parser.add_argument(
        '--sample',
        action='store_true',
        help='Generate sample API specification'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--format', '-f',
        choices=['yaml', 'json'],
        default='yaml',
        help='Output format (default: yaml)'
    )

    args = parser.parse_args()

    if not args.sample:
        parser.print_help()
        print("\n⚠️  Currently only --sample mode is supported")
        print("💡 Future versions will support custom endpoint definitions")
        sys.exit(1)

    # Generate sample API
    api = create_sample_api()

    # Convert to desired format
    if args.format == 'json':
        output = api.to_json()
    else:
        output = api.to_yaml()

    # Write output
    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"✅ OpenAPI specification generated: {output_path}")
        print(f"\n📚 You can visualize this spec at: https://editor.swagger.io/")
        print(f"   or use tools like Redoc, Stoplight, or Postman")
    else:
        print(output)


if __name__ == '__main__':
    main()
