# -*- coding: UTF-8 -*-
"""
@author: hhyo
@license: Apache Licence
@file: test.py
@time: 2018/12/16

Swagger2JSON
----------------------
Generate request parameters from the Swagger json
usage:
   >>> import swagger2json
   >>> swagger= Swagger(json_url='https://petstore.swagger.io/v2/swagger.json')
   >>> swagger.parse()
   >>> print(swagger.result)

"""
__author__ = 'hhyo'

from .swagger2json import Swagger
