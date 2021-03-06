import json

import getNo as gn


class svcoperation:
    def __init__(self):
        self.API_URL = "https://ncloud.apigw.gov-ntruss.com"
        # self.API_URL = "https://ncloud.apigw.ntruss.com"
        self.response_json = "responseFormatType=json"
        with open('types.json') as json_file:
            self.json_data = json.load(json_file)

    def svcinstanceno(self):
        parameter = ""
        make_list = []
        noList = ""
        while True:
            svc = input().strip()
            if svc == '':
                # print('ing..wait please')
                break;
            else:
                make_list.append(str(gn.getserverinstanceno(svc)))
        for i, list in enumerate(make_list):
            noList += "serverInstanceNoList." + str(i + 1) + "=" + list + '&'
        if len(make_list):
            parameter = parameter + noList + self.response_json
        return parameter

    def svcstop(self):
        uri = "/server/v2/stopServerInstances?"
        parameter = self.svcinstanceno()
        uri += parameter
        return uri

    def svcrestart(self):
        uri = "/server/v2/rebootServerInstances?"
        parameter = self.svcinstanceno()
        uri += parameter
        return uri

    def svcstart(self):
        uri = "/server/v2/startServerInstances?"
        parameter = self.svcinstanceno()
        uri += parameter
        return uri

    def svcstatus(self):
        uri = "/server/v2/getServerInstanceList?"
        parameter = self.svcinstanceno()
        uri += parameter
        return uri
