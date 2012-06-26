#!/usr/bin/env python
"""
AddressAPI.py
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

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import model

class AddressAPI(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def GetAddressXml(self, addressId, ):
        """GetAddressXml
        Args:
            addressId -- address id

        Return:
            Address -- an instance of Address"""

        # Parse inputs
        resourcePath = '/address/{addressId}.xml'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if addressId != None:
            resourcePath = resourcePath.replace('{addressId}', self.apiClient.toPathValue(addressId))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'Address')
        return responseObject


    def GetAddressJson(self, addressId, ):
        """GetAddressJson
        Args:
            addressId -- address id

        Return:
            Address -- an instance of Address"""

        # Parse inputs
        resourcePath = '/address/{addressId}.json'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if addressId != None:
            resourcePath = resourcePath.replace('{addressId}', self.apiClient.toPathValue(addressId))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'Address')
        return responseObject


