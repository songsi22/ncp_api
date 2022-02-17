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

    def svccreate(self, name):
        MAXVM = 20
        uri = "/server/v2/createServerInstances?"

        def create_uri(name):
            name_split = name.split('-')
            name_split_count = len(name_split)

            if name_split_count == 1:
                uri3 = []
                for i in self.json_data['types']:
                    acglist = ""
                    if "mv" == i['type']:
                        totalVM = int(i['count'])
                        startNo = 1
                        for index, data in enumerate(i['acg']):
                            acglist += "&accessControlGroupConfigurationNoList." + str(index + 1) + "=" + str(data)
                        while totalVM > MAXVM:
                            if startNo == 1:
                                uri2 = uri + "serverName=" + name + "-mv-&memberServerImageNo=" + \
                                       i['msino'] + "&serverProductCode=" + i['spc'] + \
                                       "&serverCreateCount=" + str(MAXVM) + \
                                       "&serverCreateStartNo=00" + str(startNo) + \
                                       "&loginKeyName=keris-lms" + \
                                       "&isProtectServerTermination=True" + \
                                       "&initScriptNo=" + str(i['init']) + \
                                       acglist + '&' + self.response_json
                                uri3.append(uri2)
                            else:
                                uri2 = uri + "serverName=" + name + "-mv-&memberServerImageNo=" + \
                                       i['msino'] + "&serverProductCode=" + i['spc'] + \
                                       "&serverCreateCount=" + str(MAXVM) + \
                                       "&serverCreateStartNo=0" + str(startNo) + \
                                       "&loginKeyName=keris-lms" + \
                                       "&isProtectServerTermination=True" + \
                                       "&initScriptNo=" + str(i['init']) + \
                                       acglist + '&' + self.response_json
                                uri3.append(uri2)
                            startNo += MAXVM
                            totalVM -= MAXVM
                            if totalVM < MAXVM:
                                uri2 = uri + "serverName=" + name + "-mv-&memberServerImageNo=" + i[
                                    'msino'] + "&serverProductCode=" + i['spc'] + \
                                       "&serverCreateCount=" + str(MAXVM) + \
                                       "&serverCreateStartNo=0" + str(startNo) + "&loginKeyName=keris-lms" + \
                                       "&isProtectServerTermination=True" + \
                                       "&initScriptNo=" + str(i['init']) + \
                                       acglist + '&' + self.response_json
                                uri3.append(uri2)
                    else:
                        for index, data in enumerate(i['acg']):
                            acglist += "&accessControlGroupConfigurationNoList." + str(index + 1) + "=" + str(data)
                        uri2 = uri + "serverName=" + name + "-" + i['type'] + "-" + \
                               "&memberServerImageNo=" + i['msino'] + "&serverProductCode=" + \
                               i['spc'] + "&serverCreateCount=" + str(i['count']) + \
                               "&serverCreateStartNo=" + i['scsn'] + \
                               "&loginKeyName=keris-lms" + \
                               "&isProtectServerTermination=True" + \
                               "&initScriptNo=" + str(i['init']) + \
                               acglist + '&' + self.response_json
                        uri3.append(uri2)
            elif name_split_count == 2:
                if "ap" == name_split[1]:
                    num = 0
                elif "stream" == name_split[1]:
                    num = 1
                elif "api" == name_split[1]:
                    num = 2
                elif "stmg" == name_split[1]:
                    num = 3
                elif "redis" == name_split[1]:
                    num = 4
                elif "mv" == name_split[1]:
                    num = 5
                type_info_list = self.json_data['types'][num]
                acglist = ""
                for index, data in enumerate(type_info_list['acg']):
                    acglist += "&accessControlGroupConfigurationNoList." + str(index + 1) + "=" + str(data)
                uri3 = uri + "serverName=" + name + "-" + type_info_list['type'] + "-" + \
                       "&memberServerImageNo=" + type_info_list['msino'] + \
                       "&serverProductCode=" + type_info_list['spc'] + \
                       "&serverCreateCount=" + str(type_info_list['count']) + \
                       "&serverCreateStartNo=" + type_info_list['scsn'] + \
                       "&loginKeyName=keris-lms" + "&isProtectServerTermination=True" + \
                       "&initScriptNo=" + str(type_info_list['init']) + \
                       acglist + '&' + self.response_json

            elif name_split_count == 3:
                if "ap" == name_split[1]:
                    num = 0
                elif "stream" == name_split[1]:
                    num = 1
                elif "api" == name_split[1]:
                    num = 2
                elif "stmg" == name_split[1]:
                    num = 3
                elif "redis" == name_split[1]:
                    num = 4
                elif "mv" == name_split[1]:
                    num = 5
                type_info_list = self.json_data['types'][num]
                acglist = ""
                for index, data in enumerate(type_info_list['acg']):
                    acglist += "&accessControlGroupConfigurationNoList." + str(index + 1) + "=" + str(data)
                uri3 = uri + "serverName=" + name + "&memberServerImageNo=" + \
                       type_info_list['msino'] + "&serverProductCode=" + \
                       type_info_list['spc'] + "&loginKeyName=keris-lms" + \
                       "&isProtectServerTermination=True" + "&initScriptNo=" + \
                       str(type_info_list['init']) + acglist + '&' + self.response_json
            return uri3

        return create_uri(name)
