import os
import time
import codecs

prevTime=0
delayBefore=[]
persistenceTime=[]
lyricList=[]

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def time_in_seconds(line):
    line = line.replace(',',':')
    hours,minutes,seconds,milliseconds = [int(n) for n in line.split(":")]
    t=(hours*3600)+(minutes*60)+(seconds)+(milliseconds/1000.0)
    return(t)
    
with codecs.open("lyrics.srt", "rU", encoding="utf-8-sig") as srt_file:
    line1 = srt_file.readline()
    while line1:
        if RepresentsInt(line1):
            t = srt_file.readline()
            lyric=""
            line2 = srt_file.readline()
            
            while line2:
                if line2.strip() == "":
                    break
                lyric=lyric+line2+"\n"
                line2 = srt_file.readline()
            
            #print lyric
            
            begin,sep,end=t.strip().split()
            
            waitbefore = time_in_seconds(begin)-prevTime
            #print waitbefore
            
            delayBefore.append(waitbefore)
            
            prevTime = time_in_seconds(begin)
            #print prevTime
            
            persists = time_in_seconds(end)-time_in_seconds(begin)
            #print persists
            
            persistenceTime.append(persists)
            lyricList.append(lyric)
        line1 = srt_file.readline()

for i in range(0,len(lyricList)):
    time.sleep(delayBefore[i])
    print(lyricList[i])
    time.sleep(persistenceTime[i])
    #os.system('clear') #command for linux/osx, for windows use os.system('cls')
