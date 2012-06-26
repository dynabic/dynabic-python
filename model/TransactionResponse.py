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

class TransactionResponse:
    """

    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            'gateway_response_message': 'str',
            'subscription_id': 'int',
            'transaction_type': 'str',
            'gateway_raw_response': 'str',
            'transaction_date': 'str',
            'settlement_attempts_count': 'int',
            'currency': 'str',
            'purchase_order_reference': 'str',
            'amount': 'float',
            'id': 'int',
            'last_settlement_attempt_date': 'str',
            'transaction_status': 'str',
            'refunded': 'float',
            'details': 'str',
            'gateway_raw_request': 'str',
            'gateway_transaction_id': 'str',
            'subscription_balance': 'float',
            'gateway_response_code': 'str',
            'gateway_response_description': 'str',
            'gateway_status': 'str',
            'gateway_ref_transaction_id': 'str',
            'gateway_settle_date': 'str'
        }



        # 
        self.gateway_response_message = None # str


        # 
        self.subscription_id = None # int


        # 
        self.transaction_type = None # str


        # 
        self.gateway_raw_response = None # str


        # 
        self.transaction_date = None # str


        # 
        self.settlement_attempts_count = None # int


        # 
        self.currency = None # str


        # 
        self.purchase_order_reference = None # str


        # 
        self.amount = None # float


        # 
        self.id = None # int


        # 
        self.last_settlement_attempt_date = None # str


        # 
        self.transaction_status = None # str


        # 
        self.refunded = None # float


        # 
        self.details = None # str


        # 
        self.gateway_raw_request = None # str


        # 
        self.gateway_transaction_id = None # str


        # 
        self.subscription_balance = None # float


        # 
        self.gateway_response_code = None # str


        # 
        self.gateway_response_description = None # str


        # 
        self.gateway_status = None # str


        # 
        self.gateway_ref_transaction_id = None # str


        # 
        self.gateway_settle_date = None # str
