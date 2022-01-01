import os

from typebuf.lib import (
    TypeField,
    TypeDefinition,
    IR,
    TypeBuf
)

from pytest import raises

TEST_YAML = 'tests/test_yaml.yaml'


def test_typefield():
    tf_a = TypeField(name='user', type='User', optional=True)
    tf_b = TypeField(name='bool', type='boolean', optional=False)
    tf_c = TypeField(name='balance', type='float')

    assert tf_a.name == 'user'
    assert tf_a.type == 'User'
    assert tf_a.optional
    assert tf_a.__dict__ == {
        'name': 'user',
        'type': 'User',
        'optional': True
    }

    assert tf_b.name == 'bool'
    assert tf_b.type == 'boolean'
    assert not tf_b.optional
    assert tf_b.__dict__ == {
        'name': 'bool',
        'type': 'boolean',
        'optional': False
    }

    assert tf_c.name == 'balance'
    assert tf_c.type == 'float'
    assert not tf_c.optional
    assert tf_c.__dict__ == {
        'name': 'balance',
        'type': 'float',
        'optional': False
    }


def test_typedefinition():
    td_a = TypeDefinition(typename='User', fields=[])
    assert td_a.__dict__ == {
        'typename': 'User',
        'imports': None,
        'fields': []
    }

    with raises(Exception):
        TypeDefinition(typename='should_fail', fields=[True, False, 'asdf'])
        TypeDefinition(typename=bool, fields=[])


def test_ir():
    ir_a = IR(**{'typedefs': [
        {'typename': 'User',
         'fields': [
             {'name': 'first_name', 'type': 'string', 'optional': False},
             {'name': 'last_name', 'type': 'string', 'optional': False},
             {'name': 'age', 'type': 'int', 'optional': False},
             {'name': 'weight', 'type': 'float', 'optional': True}]
         }
      ]
    })
    assert ir_a.typedef_c == 1
    assert ir_a.typedefs[0] == {
        'typename': 'User',
        'imports': None,
        'fields': [
            {'name': 'first_name', 'type': 'string', 'optional': False},
            {'name': 'last_name', 'type': 'string', 'optional': False},
            {'name': 'age', 'type': 'int', 'optional': False},
            {'name': 'weight', 'type': 'float', 'optional': True}]
        }


def test_ir_with_custom_imports():
    ir_a = IR(**{'typedefs': [
        {'typename': 'User',
         'imports': {
             'python': ['import os', 'import sys']
         },
         'fields': [
             {'name': 'first_name', 'type': 'string', 'optional': False},
             {'name': 'last_name', 'type': 'string', 'optional': False},
             {'name': 'age', 'type': 'int', 'optional': False},
             {'name': 'weight', 'type': 'float', 'optional': True}]
         }
    ]
    })
    assert ir_a.typedef_c == 1
    assert ir_a.typedefs[0] == {
        'typename': 'User',
        'imports': {
            'python': ['import os', 'import sys']
        },
        'fields': [
            {'name': 'first_name', 'type': 'string', 'optional': False},
            {'name': 'last_name', 'type': 'string', 'optional': False},
            {'name': 'age', 'type': 'int', 'optional': False},
            {'name': 'weight', 'type': 'float', 'optional': True}]
    }


def test_typebuf():
    client = TypeBuf(
        filename=TEST_YAML,
        languages=('python', 'typescript'),
        quiet=False
    )
    assert client.filename == TEST_YAML
    assert client.languages == ('python', 'typescript')
    assert not client.quiet
    assert client.intermediate_representation
    assert client.__dict__() == {
        'filename': TEST_YAML,
        'languages': ('python', 'typescript'),
        'IR': {
            'typedefs': [
                {'typename': 'Address',
                 'imports': None,
                 'fields': [{'name': 'street_address_1', 'type': 'string', 'optional': False},
                                           {'name': 'street_address_2', 'type': 'string', 'optional': True},
                                           {'name': 'postal_code', 'type': 'int', 'optional': False},
                                           {'name': 'state', 'type': 'string', 'optional': False},
                                           {'name': 'user', 'type': '$User', 'optional': False}]}]}}
    client.compile()
    assert os.path.exists('address.py')
    assert os.path.exists('address.ts')
    os.remove('address.py')
    os.remove('address.ts')

    # test early return when no typedefs
    backup_typedefs = client.intermediate_representation.typedefs  # to put back after
    client.intermediate_representation.typedefs = []
    assert client.intermediate_representation.typedef_c == 0
    client.compile()
    client.intermediate_representation.typedefs = backup_typedefs

    # test early return when no languages specified
    client.languages = tuple()
    client.compile()
