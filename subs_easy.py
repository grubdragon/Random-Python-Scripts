import os
import time
import codecs
import numpy

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
                lyric=lyric+line2
                line2 = srt_file.readline()
            
            print lyric
            
            begin,sep,end=t.strip().split()
            
            t_begin=time_in_seconds(begin)
            t_end=time_in_seconds(end)
            waitbefore = t_begin - prevTime
            persists = t_end-t_begin
            
            print waitbefore
            print prevTime
            print persists
            
            prevTime = t_end
            delayBefore.append(waitbefore)
            persistenceTime.append(persists)
            lyricList.append(lyric)
        line1 = srt_file.readline()

for i in range(0,len(lyricList)):
    time.sleep(delayBefore[i])
    print(lyricList[i])
    time.sleep(persistenceTime[i])
