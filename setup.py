from setuptools import setup
setup(name='ocds-cli-validator',
      scripts=['ocds-cli-validator'],
      install_requires=[
        'jsonschema',
        'json-merge-patch',
        'requests'
      ]
)
