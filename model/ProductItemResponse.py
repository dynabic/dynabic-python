#!/usr/bin/env python
"""
Copyright 2011 Wordnik, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class ProductItemResponse:
    """

    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'product_item_id': 'int',
            'is_visible_on_hosted_page': 'bool',
            'description': 'str',
            'charge_model': 'str',
            'name': 'str',
            'product_item_children': 'list<ProductItemResponse>',
            'unit_name': 'str',
            'pricing_plan_id': 'int',
            'metered_prices': 'list<ProductMeteredPriceResponse>',
            'item_type': 'str'
        }



        # 
        self.id = None # int


        # 
        self.product_item_id = None # int


        # 
        self.is_visible_on_hosted_page = None # bool


        # 
        self.description = None # str


        # 
        self.charge_model = None # str


        # 
        self.name = None # str


        # 
        self.product_item_children = None # list<ProductItemResponse>


        # 
        self.unit_name = None # str


        # 
        self.pricing_plan_id = None # int


        # 
        self.metered_prices = None # list<ProductMeteredPriceResponse>


        # 
        self.item_type = None # str

