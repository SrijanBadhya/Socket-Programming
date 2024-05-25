from socket import *
serverName='hostname'
serverPort=12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr=serverSocket.accept()

    dstring = connectionSocket.recv(1024).decode()
    numberofdays=int(dstring[0:2])

    month=int(dstring[2:4])

    #print(month)
    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=28
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=30
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=30
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=30
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    if (month>1):
        numberofdays+=30
        month=month-1

    if (month>1):
        numberofdays+=31
        month=month-1

    #print(numberofdays)
    dayoftheweek=(numberofdays%7)-1
    #zero is sunday

    minutes=((int(dstring[5:7])*60)+int(dstring[7:]))
    #print(dayoftheweek)
    #print(minutes)

    period=0
    if(495<=minutes<555):
        period=1
    elif(555<=minutes<615):
        period=2
    elif(615<=minutes<645):
        period=7
    elif(645<=minutes<705):
        period=3
    elif(705<=minutes<765):
        period=4
    elif(765<=minutes<810):
        period=8
    elif(810<=minutes<870):
        period=5
    elif(870<=minutes<930):
        period=6
    else:
        period=0

    Monday=["Congrats you don't have class","Time to attend LA period by Silvia Nancy ma'am","Time to attend MPCA by Badriprasad sir","Time to attend DAA by Shylaja ma'am","Time to attend OS class by Pavan sir","Wow! Time to attend CN class by the wonderful Revathi ma'am","Time to attend OS class by Pavan sir","It's short break yo","It's lunch break dude"]
    Tuesday=["Congrats you don't have class","Time to attend MPCA by Badriprasad sir","Time to attend LA by Silvia Nancy ma'am","Time to attend DAA by Shylaja ma'am","Wow! Time to attend CN class by the wonderful Revathi ma'am","Time to attend MPCA by Badriprasad sir","Time to attend MPCA by Badriprasad sir","It's short break yo","It's lunch break dude"]
    Wednesday=["Congrats you don't have class","Time to attend OS by Pavan sir","Wow! Time to attend CN class by the wonderful Revathi ma'am","Time to attend DAA by Shylaja ma'am","Time to attend MPCA by Badriprasad sir","Time to attend LA by Silvia Nancy Ma'am","Congrats, you don't have class","It's short break yo","It's lunch break dude"]
    Thursday=["Congrats you don't have class","Time to attend LA by Silvia Nancy ma'am","Time to attend OS by Pavan sir","Time to attend DAA by Shylaja ma'am","Time to attend MPCA by Badriprasad sir","Time to attend MPCA by Badriprasad sir","Wow! Time to attend CN class by the wonderful Revathi ma'am","It's short break yo","It's lunch break dude"]
    Friday=["Congrats you don't have class","Time to attend OS by Pavan sir","Wow! Time to attend CN class by the wonderful Revathi ma'am","Time to attend DAA by Shylaja ma'am","Time to attend LA by Silvia Nancy ma'am","Wow! Time to attend CN class by the wonderful Revathi ma'am","Wow! Time to attend CN class by the wonderful Revathi ma'am","It's short break yo","It's lunch break dude"]



    if(dayoftheweek==1):
        message=Monday[period]
    elif(dayoftheweek==2):
        message=Tuesday[period]
    elif(dayoftheweek==3):
        message=Wednesday[period]
    elif(dayoftheweek==4):
        message=Thursday[period]
    elif(dayoftheweek==5):
        message=Friday[period]
    else:
        message=Monday[0]

    #print("\n"+message)


    connectionSocket.send(message.encode())

    connectionSocket.close()

