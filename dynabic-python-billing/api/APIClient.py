#!/usr/bin/env python
"""Wordnik.com's Swagger generic API client. This client handles the client-
server communication, and is invariant across implementations. Specifics of
the methods and models for each application are generated from the Swagger
templates."""

import sys
import os
import re
import urllib
import urlparse
import urllib2
import httplib
import json
import hmac
import mimetypes

from hashlib import sha1
from base64 import b64encode

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import model


class APIClient:
    """Generic API client for Swagger client library builds"""

    def __init__(self, privateKey=None, clientKey=None, apiServer=None):
        if privateKey == None:
            raise Exception('You must pass a privateKey when instantiating the APIClient')
        if clientKey == None:
            raise Exception('You must pass a clientKey when instantiating the APIClient')
        self.privateKey = privateKey
        self.clientKey = clientKey
        self.apiServer = apiServer

    def callAPI(self, resourcePath, method, queryParams, postData,
                headerParams=None):

        url = self.apiServer + resourcePath
        headers = {}
        if headerParams:
            for param, value in headerParams.iteritems():
                headers[param] = value

        filename = False
        if not postData:
            headers['Content-type'] = 'text/html'
        elif isinstance(postData, str) and postData.startswith('file://'):
            filename = postData[7:len(postData)]
            headers['Content-type'] = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            headers['Content-Length'] = str(os.path.getsize(filename))
        else:
            headers['Content-type'] = 'application/json'

        data = None
        if method == 'GET':
            if queryParams:
                # Need to remove None values, these should not be sent
                sentQueryParams = {}
                for param, value in queryParams.iteritems():
                    if value != None:
                        sentQueryParams[param] = value
                url = url + '?' + urllib.urlencode(sentQueryParams)
            request = urllib2.Request(url=self.sign(url), headers=headers)
        elif method in ['POST', 'PUT', 'DELETE']:
            data = postData
            if filename:
                data = open(filename, "rb")
            elif data and type(postData) not in [str, int, float, bool]:
                data = json.dumps(self.serialize(postData))
            headers['clientkey'] = self.clientKey
            headers['signature'] = self.signRequestBody(data)

            request = urllib2.Request(url=self.sign(url), headers=headers, data=data)
            if method in ['PUT', 'DELETE']:
                # Monkey patch alert! Urllib2 doesn't really do PUT / DELETE
                request.get_method = lambda: method

        else:
            raise Exception('Method ' + method + ' is not recognized.')

        # Make the request
        response = urllib2.urlopen(request).read()

        try:
            data = json.loads(response)
        except ValueError: # PUT requests don't return anything
            data = None

        return data

    def toPathValue(self, obj):
        """Serialize a list to a CSV string, if necessary.
        Args:
            obj -- data object to be serialized
        Returns:
            string -- json serialization of object
        """
        if type(obj) == list:
            return urllib.quote(','.join(obj))
        else:
            return urllib.quote(obj)

    def deserialize(self, obj, objClass):
        """Derialize a JSON string into an object.

        Args:
            obj -- string or object to be deserialized
            objClass -- class literal for deserialzied object, or string
                of class name
        Returns:
            object -- deserialized object"""

        # Have to accept objClass as string or actual type. Type could be a
        # native Python type, or one of the model classes.
        if type(objClass) == str:
            try:
                objClass = eval(objClass)
            except NameError: # not a native type, must be model class
                objClass = eval('model.' + objClass + '.' + objClass)

        if objClass in [str, int, float, bool]:
            return objClass(obj)

        instance = objClass()

        for attr, attrType in instance.swaggerTypes.iteritems():
            lc_attr = attr;
            if lc_attr[0].isupper():
                lc_attr = lc_attr.lower()

            if lc_attr in obj:
                value = obj[lc_attr]
                if attrType in ['str', 'int', 'float', 'bool']:
                    attrType = eval(attrType)
                    try:
                        value = attrType(value)
                    except UnicodeEncodeError:
                        value = unicode(value)
                    setattr(instance, attr, value)
                elif 'list<' in attrType:
                    match = re.match('list<(.*)>', attrType)
                    subClass = match.group(1)
                    subValues = []

                    for subValue in value:
                        subValues.append(self.deserialize(subValue, subClass))
                    setattr(instance, attr, subValues)
                else:
                    setattr(instance, attr, self.deserialize(value,
                                                             objClass))

        return instance

    def serialize(self, obj):
        """Serialize an object hierarchy into dict.

        Args:
            obj -- object to be serialized
        Returns:
            dict -- data structure containing only non empty values"""

        props = obj
        if not isinstance(props, dict):
            props = obj.__dict__

        for attr in list(props.keys()):
            if attr == 'swaggerTypes':
                del props[attr]
            elif props[attr] is None:
                del props[attr]
            elif not isinstance(props[attr], (str, int, float, bool)):
                if isinstance(props[attr], list):
                    tmpList = []
                    for val in props[attr]:
                        tmpList.append(self.serialize(val))
                    props[attr] = tmpList
                else:
                    props[attr] = self.serialize(props[attr])
        return props

    def sign(self, url):
        urlParts = urlparse.urlparse(url)
        url = url + ('&' if urlParts.query else '?') + "clientkey=" + self.clientKey
        signed = hmac.new(self.privateKey.encode('utf-8'), url.lower().encode('utf-8'), sha1)
        signature = b64encode(signed.digest()).decode('utf-8')
        if signature.endswith("="):
            signature = signature[0 : (len(signature) - 1)]

        url = url + "&signature=" + signature.replace("+", "-").replace("/", "_")
        return url

    def signRequestBody(self, body):
        signed = hmac.new(self.privateKey.encode('utf-8'), body.lower().encode('utf-8'), sha1)
        signature = b64encode(signed.digest()).decode('utf-8')
        if signature.endswith("="):
            signature = signature[0 : (len(signature) - 1)]
        return signature.replace("+", "-").replace("/", "_")

