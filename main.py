import apikey
import publicip as pip
import svcoperation as svop
import makesig
API_URL = "https://ncloud.apigw.gov-ntruss.com"
a = pip.publicip()
b = svop.svcoperation()

typeoper = input("type oper: ")
if typeoper == "pubip":
    while True:
        try:
            oper = input('Operate: ')
            if oper == 'delete':
                uri = a.delete()
                print(uri)
                print("delete done")
            elif oper == 'create':
                get_list = a.create()
                uri = get_list[0]
                count = get_list[1]
                for i in range(count):
                    print(uri)
                print("create done")
            elif oper == 'associate':
                for i in a.associate():
                    print(i)
                print("associate done")
            elif oper == 'disassociate':
                for i in a.disassociate():
                    print(i)
                print("disassociate done")
            elif oper == 'exit' or oper == 'quit':
                break;
        except Exception as e:
            print("error: ", e)
elif typeoper == "svcoper":
    while True:
        try:
            oper = input('Operate: ')
            if oper == 'status':
                nolist = b.svcstatus()
                re = makesig.send(apikey.G_access_key,apikey.G_secret_key,nolist,API_URL)
                re = re["getServerInstanceListResponse"]
                print("return Message: "+re["returnMessage"],"total count: "+str(re["totalRows"]))
                for i in re["serverInstanceList"]:
                    print(i["serverName"],i["serverInstanceStatus"]["codeName"])
            elif oper == 'stop':
                print(b.svcstop())
            elif oper == 'restart':
                print(b.svcrestart())
            elif oper == 'start':
                print(b.svcstart())
            elif oper == 'exit' or oper == 'quit':
                break;
        except Exception as e:
            print("error: ", e)