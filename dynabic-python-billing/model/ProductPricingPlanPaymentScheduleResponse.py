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

class ProductPricingPlanPaymentScheduleResponse:
    """

    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self):
        self.swaggerTypes = {
            'id': 'int',
            'frequency_recurrence_factor': 'int',
            'frequency_interval': 'int',
            'subscription_period_change': 'float',
            'name': 'str',
            'frequency_relative_interval': 'str',
            'frequency_type': 'str',
            'pricing_plan_id': 'int',
            'end_date_offset_days': 'int',
            'start_date_offset_days': 'int'
        }



        # 
        self.id = None # int


        # 
        self.frequency_recurrence_factor = None # int


        # 
        self.frequency_interval = None # int


        # 
        self.subscription_period_change = None # float


        # 
        self.name = None # str


        # 
        self.frequency_relative_interval = None # str


        # 
        self.frequency_type = None # str


        # 
        self.pricing_plan_id = None # int


        # 
        self.end_date_offset_days = None # int


        # 
        self.start_date_offset_days = None # int
