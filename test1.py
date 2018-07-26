#coding:utf-8

import socket
import struct
class getipRange:

    def __init__(self):
        self.iplist = ["203.195.161.86","203.195.161.85","203.195.161.87","192.168.10.123","203.195.161.86","203.195.161.88","2.3.5.6","2.3.5.7","3.2.3.6","203.195.161.84"]
        self.RangeResult = []

    def getip(self,interip):
        return socket.inet_ntoa(struct.pack('I',socket.htonl(interip)))      #int to ip address

    def getinterRange(self):
        interiplist = list(set([socket.ntohl(struct.unpack("I",socket.inet_aton(str(strip)))[0]) for strip in self.iplist]))     #ip address to int
        interiplist.sort()
        ResultList = []
        for index in range(len(interiplist)):
            if len(ResultList) == 0:
                ResultList.append(interiplist[index])
            else:
                if interiplist[index] - interiplist[index - 1] == 1:
                    each1 = [interiplist[index-1],interiplist[index]]
                    flag = False
                    for each in ResultList:
                        if isinstance(each,list) and interiplist[index-1] in each:
                            each.append(interiplist[index])
                            flag = True
                    if not flag:
                        ResultList.append(each1)
                    if interiplist[index-1] in ResultList:
                        ResultList.remove(interiplist[index-1])
                else:
                    ResultList.append(interiplist[index])
        return ResultList

    def getRangeinfo(self):
        ResultList = self.getinterRange()
        for eachunit in ResultList:
            if isinstance(eachunit,list):
                strresult = self.getip(eachunit[0]) + "-" + self.getip(eachunit[-1])
                self.RangeResult.append(strresult)
            else:
                self.RangeResult.append(self.getip(eachunit))
        return self.RangeResult

if __name__ == "__main__":
    execunit = getipRange()
    print(execunit.getRangeinfo())