# -*- coding: UTF-8 -*-
""" 
@author: hhyo 
@license: Apache Licence 
@file: test.py 
@time: 2018/12/16
"""
import json
import os
import unittest
import swagger2json

__author__ = 'hhyo'

base_dir = os.path.abspath(os.path.dirname(__file__))


class Swagger2JsonTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.swagger = swagger2json.Swagger(json_url='https://petstore.swagger.io/v2/swagger.json')
        cls.swagger.parse()

    def test(self):
        for items in self.swagger.result:
            print(json.dumps(items, sort_keys=True, indent=4, separators=(',', ': ')).encode('utf-8').decode(
                'unicode_escape'))
