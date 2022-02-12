import makesig
import apikey


class publicIP:
    def __init__(self):
        self.API_URL = "https://ncloud.apigw.gov-ntruss.com"
        self.response_json = "responseFormatType=json"

    def delete(self):
        uri = "/server/v2/deletePublicIpInstances?"
        make_list = []
        noList = ""
        while True:
            ip = input().strip()
            if ip == '':
                break;
            else:
                make_list.append(self.getPublicIpNo(ip))
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
                pubipNo = self.getPublicIpNo(ipnserver[0])
                serverNo = self.getServerInstanceNo(ipnserver[1])
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
                disas_uri = uri + "publicIpInstanceNo=" + self.getPublicIpNo(ip) + "&" + self.response_json
                make_list.append(disas_uri)
        return make_list

    def getPublicIpNo(self, ip=""):
        if len(ip) != 0:
            get_pubip_uri = "/server/v2/getPublicIpInstanceList?searchFilterName=publicIp&searchFilterValue=" \
                            + ip + '&' + self.response_json
            re = makesig.send(apikey.G_access_key, apikey.G_secret_key, get_pubip_uri, self.API_URL)
            getPubIpNo = re["getPublicIpInstanceListResponse"]["publicIpInstanceList"][0]["publicIpInstanceNo"]
            return getPubIpNo

    def getServerInstanceNo(self, servername=""):
        if len(servername) != 0:
            get_server_uri = "/server/v2/getServerInstanceList?searchFilterName=serverName&searchFilterValue=" \
                             + servername + "&" + self.response_json
            re = makesig.send(apikey.G_access_key, apikey.G_secret_key, get_server_uri, self.API_URL)
            get_server_no = re["getServerInstanceListResponse"]["serverInstanceList"][0]["serverInstanceNo"]
            return get_server_no
