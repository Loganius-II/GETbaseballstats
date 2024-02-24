from requests_html import HTMLSession
import sys
from time import sleep
from os import system,mkdir
try:
    open("getBatterStats.csv")
except:
    mkdir("getBatterStats.csv")
    pass
s = HTMLSession()
url = "https://www.espn.com/mlb/history/leaders"
r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'})
BBBSWrite = open("getBatterStats.csv", "w")
BBBSWrite.write("RANK,PLAYER,YRS,G,AB,R,H,2B,3B,HR,RBI,BB,SO,SB,CS,BA\n")
BBBSAppend = open("getBatterStats.csv", "a")
OddPlayer = r.html.find('tr.oddrow')
index = 0

pOdd = r.html.find("tr.oddrow")
pEven = r.html.find("tr.evenrow")
pOddName = r.html.find("tr.oddrow a")
pOddStats = r.html.find("tr.oddrow td")
pEvenStats = r.html.find("tr.evenrow td")
for i in pOdd:
    for i in pOddStats:
        index+=1
        if index < 16:
            BBBSAppend.write(f"{i.text},")
        elif index == 16:
            BBBSAppend.write(f"{i.text}\n")
        elif index < 32:
            BBBSAppend.write(f"{i.text},")
        elif index == 32:
            BBBSAppend.write(f"{i.text}\n")  
        elif index < 48:
            BBBSAppend.write(f"{i.text},")     
        elif index == 48:
            BBBSAppend.write(f"{i.text}\n") 
        elif index < 64:
            BBBSAppend.write(f"{i.text},")
        elif index == 64:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 80:
            BBBSAppend.write(f"{i.text},")
        elif index == 80:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 96:
            BBBSAppend.write(f"{i.text},")
        elif index == 96:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 112:
            BBBSAppend.write(f"{i.text},")
        elif index == 112:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 128:
            BBBSAppend.write(f"{i.text},")
        elif index == 128:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 144:
            BBBSAppend.write(f"{i.text},")
        elif index == 144:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 160:
            BBBSAppend.write(f"{i.text},")
        elif index == 160:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 176:
            BBBSAppend.write(f"{i.text},")
        elif index == 176:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 192:
            BBBSAppend.write(f"{i.text},")
        elif index == 192:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 208:
            BBBSAppend.write(f"{i.text},")
        elif index == 208:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 224:
            BBBSAppend.write(f"{i.text},")
        elif index == 224:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 240:
            BBBSAppend.write(f"{i.text},")
        elif index == 240:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 256:
            BBBSAppend.write(f"{i.text},")
        elif index == 256:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 272:
            BBBSAppend.write(f"{i.text},")
        elif index == 272:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 288:
            BBBSAppend.write(f"{i.text},")
        elif index == 288:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 304:
            BBBSAppend.write(f"{i.text},")
        elif index == 304:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 320:
            BBBSAppend.write(f"{i.text},")
        elif index == 320:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 336:
            BBBSAppend.write(f"{i.text},")
        elif index == 336:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 352:
            BBBSAppend.write(f"{i.text},")
        elif index == 352:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 368:
            BBBSAppend.write(f"{i.text},")
        elif index == 368:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 384:
            BBBSAppend.write(f"{i.text},")
        elif index == 384:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 400:
            BBBSAppend.write(f"{i.text},")
        elif index == 400:
            BBBSAppend.write(f"{i.text}\n")

#---------------------------EVEN BELOW-----------------------------------------------------------     
index = 0   
for i in pEven:
    for i in pEvenStats:
        index+=1
        if index < 16:
            BBBSAppend.write(f"{i.text},")
        elif index == 16:
            BBBSAppend.write(f"{i.text}\n")
        elif index < 32:
            BBBSAppend.write(f"{i.text},")
        elif index == 32:
            BBBSAppend.write(f"{i.text}\n")  
        elif index < 48:
            BBBSAppend.write(f"{i.text},")     
        elif index == 48:
            BBBSAppend.write(f"{i.text}\n") 
        elif index < 64:
            BBBSAppend.write(f"{i.text},")
        elif index == 64:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 80:
            BBBSAppend.write(f"{i.text},")
        elif index == 80:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 96:
            BBBSAppend.write(f"{i.text},")
        elif index == 96:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 112:
            BBBSAppend.write(f"{i.text},")
        elif index == 112:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 128:
            BBBSAppend.write(f"{i.text},")
        elif index == 128:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 144:
            BBBSAppend.write(f"{i.text},")
        elif index == 144:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 160:
            BBBSAppend.write(f"{i.text},")
        elif index == 160:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 176:
            BBBSAppend.write(f"{i.text},")
        elif index == 176:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 192:
            BBBSAppend.write(f"{i.text},")
        elif index == 192:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 208:
            BBBSAppend.write(f"{i.text},")
        elif index == 208:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 224:
            BBBSAppend.write(f"{i.text},")
        elif index == 224:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 240:
            BBBSAppend.write(f"{i.text},")
        elif index == 240:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 256:
            BBBSAppend.write(f"{i.text},")
        elif index == 256:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 272:
            BBBSAppend.write(f"{i.text},")
        elif index == 272:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 288:
            BBBSAppend.write(f"{i.text},")
        elif index == 288:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 304:
            BBBSAppend.write(f"{i.text},")
        elif index == 304:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 320:
            BBBSAppend.write(f"{i.text},")
        elif index == 320:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 336:
            BBBSAppend.write(f"{i.text},")
        elif index == 336:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 352:
            BBBSAppend.write(f"{i.text},")
        elif index == 352:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 368:
            BBBSAppend.write(f"{i.text},")
        elif index == 368:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 384:
            BBBSAppend.write(f"{i.text},")
        elif index == 384:
            BBBSAppend.write(f"{i.text}\n")


        elif index < 400:
            BBBSAppend.write(f"{i.text},")
        elif index == 400:
            BBBSAppend.write(f"{i.text}\n")












##for i in pName:
##    print(i.text)






