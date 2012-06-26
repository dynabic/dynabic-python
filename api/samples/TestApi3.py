import sys
import os
import hmac

from api.CustomersAPI import CustomersAPI
from api.APIClient3 import APIClient3
from model.CustomerRequest import CustomerRequest


def getCustomer(customerId):
    response = CustomersAPI(apiClient).GetCustomer(customerId)
    print(apiClient.serialize(response))
    
def addCustomer():
    postData = CustomerRequest()
    postData.first_name = "John"
    postData.last_name = "Doe"
    postData.email = "hopefullysome@nonexisting.email"
    response = CustomersAPI(apiClient).AddCustomer("test", postData)
    print(apiClient.serialize(response))


if __name__ == '__main__':
    privateKey = "19c7a0d97d2d4413aba5"
    clientKey = "19c7a0d97d2d4413aba5";
    apiServer = "http://stage-api.dynabic.com/billing";
    apiClient = APIClient3(privateKey, clientKey, apiServer)

    getCustomer("14")
#    addCustomer()
