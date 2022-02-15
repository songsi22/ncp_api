import makesig
import apikey

API_URL = "https://ncloud.apigw.gov-ntruss.com"
# API_URL = "https://ncloud.apigw.ntruss.com"
response_json = "responseFormatType=json"

def getpublicipno(ip=""):
    if len(ip) != 0:
        get_pubip_uri = "/server/v2/getPublicIpInstanceList?searchFilterName=publicIp&searchFilterValue=" \
                        + ip + '&' + response_json
        re = makesig.send(apikey.G_access_key, apikey.G_secret_key, get_pubip_uri, API_URL)
        print(re["getPublicIpInstanceListResponse"]["totalRows"])
        for i in re["getPublicIpInstanceListResponse"]["publicIpInstanceList"]:
            if ip == i["publicIp"]:
                getpubipno = i["publicIpInstanceNo"]
        return getpubipno


def getserverinstanceno(servername=""):
    if len(servername) != 0:
        get_server_uri = "/server/v2/getServerInstanceList?searchFilterName=serverName&searchFilterValue=" \
                         + servername + "&" + response_json
        re = makesig.send(apikey.G_access_key, apikey.G_secret_key, get_server_uri, API_URL)
        for i in re["getServerInstanceListResponse"]["serverInstanceList"]:
            if servername == i["serverName"]:
                getsvcno = i["serverInstanceNo"]
        return getsvcno
