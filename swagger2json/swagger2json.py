# -*- coding: UTF-8 -*-
"""
@author: yuyu1987、hhyo
@license: Apache Licence
@file: test.py
@time: 2018/12/16
"""
from requests.compat import basestring

__author__ = 'yuyu1987、hhyo'

import requests
import sys
import json
from collections import deque

python_version = sys.version[0]


class Swagger(object):

    def __init__(self, json_url):
        """
        :param json_url: Examples "https://petstore.swagger.io/v2/swagger.json"
        """
        self.raw_data = requests.get(json_url).json()
        self._definitions = self.raw_data['definitions']
        self.tags = [self._make_class_name(tag['name']) for tag in self.raw_data['tags']]
        self.result = []
        self.q = deque(maxlen=5)

    def parse(self):
        """
        parse to result
        :return:
        """
        for path, api_dicts in self.raw_data['paths'].items():
            if_params_in_url = '{' in path
            for method, values in api_dicts.items():
                self.result.append(
                    {
                        'name': self._make_function_name(path),
                        'tag': self._make_class_name(values.get('tags')[0]),
                        'path': path,
                        'if_params_in_url': if_params_in_url,
                        'method': method,
                        'summary': values.get('summary'),
                        'description': values.get('description'),
                        'type': values.get('consumes'),
                        'parameters': self._parse_parameters(values.get('parameters', []))
                    }
                )

    def _parse_parameters(self, parameters):
        """
        :param parameters:
        :return:
        """
        result = {}
        if isinstance(parameters, dict):
            return result

        for parameter in parameters:
            _in = parameter['in']
            name = parameter['name']
            _type = parameter.get('type')
            schema = parameter.get('schema')
            if _type:
                result[_in] = result.get(_in, {})
                result[_in][name] = self._type2value(_type)
            elif schema:
                result[_in] = self._parse_schema(schema)
            else:
                raise Exception(u'错错错')
        for k, v in result.items():
            result[k] = self.format_json(v)
        return result

    @staticmethod
    def _type2value(t):
        if t == 'string':
            return 'string'
        elif t == 'integer':
            return 1
        elif t == 'array':
            return []
        elif t == 'boolean':
            return True
        elif t == 'object':
            return {}
        elif t == 'number':
            return 1
        elif t == 'file':
            return 'string'
        else:
            raise Exception('unknown type')

    def _parse_schema(self, schema):
        result = {}
        try:
            if self.q[0] == self.q[4]:
                return result
        except:
            pass

        _type = schema.get('type')
        if _type == 'array':
            return [self._parse_schema(schema['items']), ]
        elif _type in ['integer', 'string', 'boolean', 'number']:
            return self._type2value(schema.get('type'))

        try:
            definition_name = schema['$ref'].split('/')[-1]
        except KeyError:
            return {}

        self.q.append(definition_name)

        definition = self._definitions[definition_name]
        if definition['type'] == 'object':
            properties = definition.get('properties')
            if not properties:
                return result
            for name, value in properties.items():
                if value.get('type') == 'array' or value.get('$ref'):
                    result[name] = self._parse_schema(value)
                else:
                    result[name] = self._type2value(value['type'])
        else:
            raise Exception('unknown type')

        return result

    def _make_class_name(self, s):
        return self._underline2camel(s)

    def _make_function_name(self, s):
        s = [i for i in s.split('/') if '{' not in i]
        return self._camel2underline(s[-1])

    @staticmethod
    def _camel2underline(s):
        """
            convert variables camel2underline
        """
        s = list(s)
        for index, value in enumerate(s[1:]):
            if 'A' <= value <= 'Z':
                s[index + 1] = '_' + value.lower()
        return ''.join(s).lower().replace('-', '_')

    @staticmethod
    def _underline2camel(underline_format):
        """
            convert variables underline2camel
        """
        camel_format = ''
        if isinstance(underline_format, str):
            for _s_ in underline_format.replace('-', '_').split('_'):
                camel_format += _s_.capitalize()
        return camel_format

    @staticmethod
    def format_json(content):
        """
        Format result to JSON
        """
        if isinstance(content, basestring):
            content = json.loads(content)

        if python_version == '3':
            result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
                encode('latin-1').decode('unicode_escape')
        else:
            result = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': ')). \
                decode("unicode_escape")

        result = result.split('\n')
        result = [result[0]] + [u'        ' + i for i in result[1:]]

        return '\n'.join(result).replace('true', 'True').replace('false', 'False')
