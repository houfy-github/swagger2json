Swagger2JSON
==================
[![Build Status](https://travis-ci.org/hhyo/swagger2json.svg?branch=master)](https://travis-ci.org/hhyo/swagger2json)
[![codecov](https://codecov.io/gh/hhyo/swagger2json/branch/master/graph/badge.svg)](https://codecov.io/gh/hhyo/swagger2json)
[![image](https://img.shields.io/pypi/v/swagger2json.svg)](https://pypi.org/project/swagger2json/)
[![image](https://img.shields.io/pypi/l/swagger2json.svg)](https://github.com/hhyo/swagger2json/blob/master/LICENSE)
[![image](https://img.shields.io/pypi/pyversions/swagger2json.svg)](https://pypi.org/project/swagger2json/)

Generate request parameters from the Swagger json  

Installation
------------
`pip install swagger2json`


Usage
-------------

```python
   import swagger2json
   import json
   swagger= Swagger(json_url='https://petstore.swagger.io/v2/swagger.json')
   swagger.parse()
   for items in swagger.result:
       print(json.dumps(items, sort_keys=True, indent=4, separators=(',', ': ')).encode('utf-8').decode('unicode_escape'))
```

Examples
-------------
> https://petstore.swagger.io/v2/swagger.json

`python setup.py test`


#### Result
```json
{
    "description": "",
    "if_params_in_url": false,
    "method": "post",
    "name": "pet",
    "parameters": {
        "body": "{
            "category": {
                "id": 1,
                "name": "string"
            },
            "id": 1,
            "name": "string",
            "photoUrls": [
                "string"
            ],
            "status": "string",
            "tags": [
                {
                    "id": 1,
                    "name": "string"
                }
            ]
        }"
    },
    "path": "/pet",
    "summary": "Add a new pet to the store",
    "tag": "Pet",
    "type": [
        "application/json",
        "application/xml"
    ]
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "put",
    "name": "pet",
    "parameters": {
        "body": "{
            "category": {
                "id": 1,
                "name": "string"
            },
            "id": 1,
            "name": "string",
            "photoUrls": [
                "string"
            ],
            "status": "string",
            "tags": [
                {
                    "id": 1,
                    "name": "string"
                }
            ]
        }"
    },
    "path": "/pet",
    "summary": "Update an existing pet",
    "tag": "Pet",
    "type": [
        "application/json",
        "application/xml"
    ]
}
{
    "description": "Multiple status values can be provided with comma separated strings",
    "if_params_in_url": false,
    "method": "get",
    "name": "find_by_status",
    "parameters": {
        "query": "{
            "status": []
        }"
    },
    "path": "/pet/findByStatus",
    "summary": "Finds Pets by status",
    "tag": "Pet",
    "type": null
}
{
    "description": "Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.",
    "if_params_in_url": false,
    "method": "get",
    "name": "find_by_tags",
    "parameters": {
        "query": "{
            "tags": []
        }"
    },
    "path": "/pet/findByTags",
    "summary": "Finds Pets by tags",
    "tag": "Pet",
    "type": null
}
{
    "description": "Returns a single pet",
    "if_params_in_url": true,
    "method": "get",
    "name": "pet",
    "parameters": {
        "path": "{
            "petId": 1
        }"
    },
    "path": "/pet/{petId}",
    "summary": "Find pet by ID",
    "tag": "Pet",
    "type": null
}
{
    "description": "",
    "if_params_in_url": true,
    "method": "post",
    "name": "pet",
    "parameters": {
        "formData": "{
            "name": "string",
            "status": "string"
        }",
        "path": "{
            "petId": 1
        }"
    },
    "path": "/pet/{petId}",
    "summary": "Updates a pet in the store with form data",
    "tag": "Pet",
    "type": [
        "application/x-www-form-urlencoded"
    ]
}
{
    "description": "",
    "if_params_in_url": true,
    "method": "delete",
    "name": "pet",
    "parameters": {
        "header": "{
            "api_key": "string"
        }",
        "path": "{
            "petId": 1
        }"
    },
    "path": "/pet/{petId}",
    "summary": "Deletes a pet",
    "tag": "Pet",
    "type": null
}
{
    "description": "",
    "if_params_in_url": true,
    "method": "post",
    "name": "upload_image",
    "parameters": {
        "formData": "{
            "additionalMetadata": "string",
            "file": "string"
        }",
        "path": "{
            "petId": 1
        }"
    },
    "path": "/pet/{petId}/uploadImage",
    "summary": "uploads an image",
    "tag": "Pet",
    "type": [
        "multipart/form-data"
    ]
}
{
    "description": "Returns a map of status codes to quantities",
    "if_params_in_url": false,
    "method": "get",
    "name": "inventory",
    "parameters": {},
    "path": "/store/inventory",
    "summary": "Returns pet inventories by status",
    "tag": "Store",
    "type": null
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "post",
    "name": "order",
    "parameters": {
        "body": "{
            "complete": True,
            "id": 1,
            "petId": 1,
            "quantity": 1,
            "shipDate": "string",
            "status": "string"
        }"
    },
    "path": "/store/order",
    "summary": "Place an order for a pet",
    "tag": "Store",
    "type": null
}
{
    "description": "For valid response try integer IDs with value >= 1 and <= 10. Other values will generated exceptions",
    "if_params_in_url": true,
    "method": "get",
    "name": "order",
    "parameters": {
        "path": "{
            "orderId": 1
        }"
    },
    "path": "/store/order/{orderId}",
    "summary": "Find purchase order by ID",
    "tag": "Store",
    "type": null
}
{
    "description": "For valid response try integer IDs with positive integer value. Negative or non-integer values will generate API errors",
    "if_params_in_url": true,
    "method": "delete",
    "name": "order",
    "parameters": {
        "path": "{
            "orderId": 1
        }"
    },
    "path": "/store/order/{orderId}",
    "summary": "Delete purchase order by ID",
    "tag": "Store",
    "type": null
}
{
    "description": "This can only be done by the logged in user.",
    "if_params_in_url": false,
    "method": "post",
    "name": "user",
    "parameters": {
        "body": "{
            "email": "string",
            "firstName": "string",
            "id": 1,
            "lastName": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 1,
            "username": "string"
        }"
    },
    "path": "/user",
    "summary": "Create user",
    "tag": "User",
    "type": null
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "post",
    "name": "create_with_array",
    "parameters": {
        "body": "[
            {
                "email": "string",
                "firstName": "string",
                "id": 1,
                "lastName": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 1,
                "username": "string"
            }
        ]"
    },
    "path": "/user/createWithArray",
    "summary": "Creates list of users with given input array",
    "tag": "User",
    "type": null
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "post",
    "name": "create_with_list",
    "parameters": {
        "body": "[
            {
                "email": "string",
                "firstName": "string",
                "id": 1,
                "lastName": "string",
                "password": "string",
                "phone": "string",
                "userStatus": 1,
                "username": "string"
            }
        ]"
    },
    "path": "/user/createWithList",
    "summary": "Creates list of users with given input array",
    "tag": "User",
    "type": null
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "get",
    "name": "login",
    "parameters": {
        "query": "{
            "password": "string",
            "username": "string"
        }"
    },
    "path": "/user/login",
    "summary": "Logs user into the system",
    "tag": "User",
    "type": null
}
{
    "description": "",
    "if_params_in_url": false,
    "method": "get",
    "name": "logout",
    "parameters": {},
    "path": "/user/logout",
    "summary": "Logs out current logged in user session",
    "tag": "User",
    "type": null
}
{
    "description": "",
    "if_params_in_url": true,
    "method": "get",
    "name": "user",
    "parameters": {
        "path": "{
            "username": "string"
        }"
    },
    "path": "/user/{username}",
    "summary": "Get user by user name",
    "tag": "User",
    "type": null
}
{
    "description": "This can only be done by the logged in user.",
    "if_params_in_url": true,
    "method": "put",
    "name": "user",
    "parameters": {
        "body": "{
            "email": "string",
            "firstName": "string",
            "id": 1,
            "lastName": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 1,
            "username": "string"
        }",
        "path": "{
            "username": "string"
        }"
    },
    "path": "/user/{username}",
    "summary": "Updated user",
    "tag": "User",
    "type": null
}
{
    "description": "This can only be done by the logged in user.",
    "if_params_in_url": true,
    "method": "delete",
    "name": "user",
    "parameters": {
        "path": "{
            "username": "string"
        }"
    },
    "path": "/user/{username}",
    "summary": "Delete user",
    "tag": "User",
    "type": null
}
```

Running the tests
-----------------
`python setup.py test`


Acknowledgments
-----------------
- https://petstore.swagger.io/v2/swagger.json
