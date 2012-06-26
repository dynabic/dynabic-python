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

class PricingPlanResponse:
    """

    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'product_id': 'int',
            'trial_period_duration_days': 'int',
            'trial_period_charge': 'float',
            'name': 'str',
            'upfront_charge': 'float',
            'product_items': 'list<ProductItemResponse>',
            'pricing_plan_payment_schedules': 'list<ProductPricingPlanPaymentScheduleResponse>',
            'currency_code': 'str'
        }



        # 
        self.id = None # int


        # 
        self.product_id = None # int


        # 
        self.trial_period_duration_days = None # int


        # 
        self.trial_period_charge = None # float


        # 
        self.name = None # str


        # 
        self.upfront_charge = None # float


        # 
        self.product_items = None # list<ProductItemResponse>


        # 
        self.pricing_plan_payment_schedules = None # list<ProductPricingPlanPaymentScheduleResponse>


        # 
        self.currency_code = None # str
