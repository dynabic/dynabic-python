#!/usr/bin/env python
"""
ReportsAPI.py
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

class ReportsAPI(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    def GetProductsSignupsEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetProductsSignupsEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ProductsSignups> -- an instance of ProductsSignups"""

        # Parse inputs
        resourcePath = '/reports/ProductsSignupsEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ProductsSignups'))
        return responseObjects
    def GetProductsRevenuesEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetProductsRevenuesEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ProductsRevenues> -- an instance of ProductsRevenues"""

        # Parse inputs
        resourcePath = '/reports/ProductsRevenuesEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ProductsRevenues'))
        return responseObjects
    def GetTotalRevenueAmount(self, siteSubdomain, ):
        """GetTotalRevenueAmount
        Args:
            siteSubdomain -- site Subdomain

        Return:
            list<RevenueAmount> -- an instance of RevenueAmount"""

        # Parse inputs
        resourcePath = '/reports/TotalRevenueAmount/{siteSubdomain}/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'RevenueAmount'))
        return responseObjects
    def GetActiveSubscriptionsCount(self, siteSubdomain, ):
        """GetActiveSubscriptionsCount
        Args:
            siteSubdomain -- site Subdomain

        Return:
            ActiveSubscriptionsCountResponse -- an instance of ActiveSubscriptionsCountResponse"""

        # Parse inputs
        resourcePath = '/reports/ActiveSubscriptionsCount/{siteSubdomain}/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'ActiveSubscriptionsCountResponse')
        return responseObject


    def GetTotalSubscribersCount(self, siteSubdomain, ):
        """GetTotalSubscribersCount
        Args:
            siteSubdomain -- site Subdomain

        Return:
            TotalSubscribersCountResponse -- an instance of TotalSubscribersCountResponse"""

        # Parse inputs
        resourcePath = '/reports/TotalSubscribersCount/{siteSubdomain}/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'TotalSubscribersCountResponse')
        return responseObject


    def GetTodayRevenueAmount(self, siteSubdomain, ):
        """GetTodayRevenueAmount
        Args:
            siteSubdomain -- site Subdomain

        Return:
            list<RevenueAmount> -- an instance of RevenueAmount"""

        # Parse inputs
        resourcePath = '/reports/TodayRevenueAmount/{siteSubdomain}/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'RevenueAmount'))
        return responseObjects
    def GetTodayNewSubscribersCount(self, siteSubdomain, ):
        """GetTodayNewSubscribersCount
        Args:
            siteSubdomain -- site Subdomain

        Return:
            TodayNewSubscribersCountResponse -- an instance of TodayNewSubscribersCountResponse"""

        # Parse inputs
        resourcePath = '/reports/TodayNewSubscribersCount/{siteSubdomain}/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response,
                                                    'TodayNewSubscribersCountResponse')
        return responseObject


    def GetSignupsEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetSignupsEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ReportIntValueItem> -- an instance of ReportIntValueItem"""

        # Parse inputs
        resourcePath = '/reports/SignupsEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ReportIntValueItem'))
        return responseObjects
    def GetRevenuesEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetRevenuesEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ReportDecimalValueItem> -- an instance of ReportDecimalValueItem"""

        # Parse inputs
        resourcePath = '/reports/RevenuesEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ReportDecimalValueItem'))
        return responseObjects
    def GetCustomersEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetCustomersEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ReportIntValueItem> -- an instance of ReportIntValueItem"""

        # Parse inputs
        resourcePath = '/reports/CustomersEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ReportIntValueItem'))
        return responseObjects
    def GetSubscriptionsEvolution(self, siteSubdomain, startDate, endDate, ):
        """GetSubscriptionsEvolution
        Args:
            siteSubdomain -- site Subdomain
            startDate -- start Date
            endDate -- end Date

        Return:
            list<ReportIntValueItem> -- an instance of ReportIntValueItem"""

        # Parse inputs
        resourcePath = '/reports/SubscriptionsEvolution/{siteSubdomain}/{startDate}/{format}?endDate={endDate}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}


        if siteSubdomain != None:
            resourcePath = resourcePath.replace('{siteSubdomain}', self.apiClient.toPathValue(siteSubdomain))
        if startDate != None:
            resourcePath = resourcePath.replace('{startDate}', self.apiClient.toPathValue(startDate))
        if endDate != None:
            resourcePath = resourcePath.replace('{endDate}', self.apiClient.toPathValue(endDate))


        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'ReportIntValueItem'))
        return responseObjects
    def GetSitesSummary(self, ):
        """GetSitesSummary
        Args:
        Return:
            list<SiteSummary> -- an instance of SiteSummary"""

        # Parse inputs
        resourcePath = '/reports/SitesSummary/{format}'
        resourcePath = resourcePath.replace('{format}', 'json')
        resourcePath = resourcePath.replace('*', '')
        method = 'GET'

        queryParams = {}
        headerParams = {}



        # Make the API Call
        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          None, headerParams)
        if not response:
            return None


        # Create output objects if the response has more than one object
        responseObjects = []
        for responseObject in response:
          responseObjects.append(self.apiClient.deserialize(responseObject,
                                                         'SiteSummary'))
        return responseObjects