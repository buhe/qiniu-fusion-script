#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from qiniu import Auth
import requests
import json

DOMAIN_HOST = 'http://fusion.qiniuapi.com'

if __name__ == '__main__':
        q = Auth("you-access-key", "you-sercet-key")
        data = {
            "sourceType": "qiniuBucket",
            "sourceQiniuBucket": "you-source",
            # "testURLPath": "http://www.qianfanyun.com",
            "lineId": "b7e2424d1c5599d1ffdecccac9daec4b",
            # "lineId": "357e2201bedce39a9f3845ca056f9671 ",
            # "lineId": "cdb07271bfe14dc06d5cdb51d5a1041b",
            "registerNo": "you-register-no"
        }
        # token = self.generate_upload_token(scope)

        url = '%s/v2/domains/%s' % (DOMAIN_HOST, "you-domain-name")
        print str(data)
        token = q.token_of_request(url,content_type="application/json");
        print token;
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'QBox {0}'.format(token)
        }
        
        res = requests.post(url, data=json.dumps(data),headers=headers)
        print res.text
