import getNo

class publicip:
    def __init__(self):
        self.API_URL = "https://ncloud.apigw.gov-ntruss.com"
        # self.API_URL = "https://ncloud.apigw.ntruss.com"
        self.response_json = "responseFormatType=json"

    def delete(self):
        uri = "/server/v2/deletePublicIpInstances?"
        make_list = []
        noList = ""
        while True:
            ip = input().strip()
            if ip == '':
                # print('ing..wait please')
                break;
            else:
                make_list.append(getNo.getpublicipno(ip))
        for i, list in enumerate(make_list):
            noList += "publicIpInstanceNoList." + str(i + 1) + "=" + list + '&'
        if len(make_list):
            uri = uri + noList + self.response_json
        else:
            uri = "error"
        return uri

    def create(self):
        uri = "/server/v2/createPublicIpInstance?" + self.response_json
        count = input("how many: ").strip()
        if count == '' or int(count) == 0:
            uri = "error"
            count = 0
        return uri, int(count)

    def associate(self):
        uri = "/server/v2/associatePublicIpWithServerInstance?"
        make_list = []
        while True:
            ipnserver = input().strip().split('\t')
            if ipnserver[0] == '' or ipnserver[1] == '':
                break;
            else:
                pubipNo = getNo.getpublicipno(ipnserver[0])
                serverNo = getNo.getserverinstanceno(ipnserver[1])
                ipnserveruri = "publicIpInstanceNo=" + str(pubipNo).strip() + "&" \
                                                                              "serverInstanceNo=" + str(
                    serverNo).strip() + "&" + self.response_json
                make_list.append(uri + ipnserveruri)
        return make_list

    def disassociate(self):
        uri = "/server/v2/disassociatePublicIpFromServerInstance?"
        make_list = []
        while True:
            ip = input().strip()
            if ip == '':
                break;
            else:
                disas_uri = uri + "publicIpInstanceNo=" + str(getNo.getpublicipno(ip)) + "&" + self.response_json
                make_list.append(disas_uri)
        return make_list

