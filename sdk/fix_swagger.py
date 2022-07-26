import sys

import yaml


def fix_swagger(swagger):
    paths = swagger['paths']

    for path in paths.items():
        for method in path[1].items():
            for response in method[1]['responses'].items():
                if 'content' in response[1]:
                    for content in response[1]['content'].items():
                        if content[0] == 'application/json':
                            # Remove the examples, not needed for code generation
                            if 'example' in content[1]:
                                content[1].pop('example')
                            # Add the schema property
                            content[1]['schema'] = {
                                'type': 'object'
                            }

    return swagger


file_name = sys.argv[1] if len(sys.argv) else 'Operations.yaml'

with open(file_name, 'r') as f:
    swagger = yaml.load(f, Loader=yaml.Loader)

fixed_swagger = fix_swagger(swagger)

print(yaml.dump(fixed_swagger))
