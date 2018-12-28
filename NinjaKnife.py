# -*- coding: utf-8 -*-
import globals
import httplib
import json
import base64
import ssl
import sys


class NinjaKnife:

    Get     = "GET"
    Post    = "POST"
    Delete  = "DELETE"
    ContentType = "application/json"

    def __init__(self, method, apiurl):
        self.method = method
        self.apiurl = apiurl
        self.body = ""
        self.resp = ""
        self.result = 0

    def fetch(self):
        conn = httplib.HTTPSConnection(globals.SERVER_URL)
        if sys.version_info >= (2, 7, 9):
            conn._context.check_hostname = False
            conn._context.verify_mode = ssl.CERT_NONE
        headers = {}
        headers["Authorization"] = "Basic %s" \
            % base64.standard_b64encode(globals.PASS_PHRASE)
        headers["Accept"] = NinjaKnife.ContentType
        if self.method is NinjaKnife.Post:
            headers["Content-Type"] = NinjaKnife.ContentType
            req = conn.request(self.method, self.apiurl,
                               headers=headers, body=self.body)
        else:
            req = conn.request(self.method, self.apiurl,
                               headers=headers)
        res = conn.getresponse()
        result = res.status
        resp = res.read()
        if res.status == 200:
            parsed = json.loads(resp)
            print json.dumps(parsed, indent=4, sort_keys=True)
        else:
            print resp , res.status, \
                "Error returned in Response to the Request sent"
       
    def success(self):
        return True if result == 200 else False

    def responsetext(self):
        return resp
