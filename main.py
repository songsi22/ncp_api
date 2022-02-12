import publicIP as pip
import svcoperation as svop

a = pip.publicIP()
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
        except Exception as e:
            print("error: ", e)
elif typeoper == "svcoper":
    while True:
        try:
            oper = input('Operate: ')
            if oper == 'status':
                print(b.svcstatus())
            elif oper == 'stop':
                print(b.svcstop())
            elif oper == 'restart':
                print(b.svcrestart())
            elif oper == 'start':
                print(b.svcstart())
        except Exception as e:
            print("error: ", e)