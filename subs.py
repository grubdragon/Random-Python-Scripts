import thread
import Tkinter as tk
import os
import time
import codecs

root = tk.Tk()
prevTime=0
delayBefore=[]
persistenceTime=[]
lyricList=[]
currentLyric=0

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def time_in_seconds(line):
    line = line.replace(',',':')
    hours,minutes,seconds,milliseconds = [int(n) for n in line.split(":")]
    time=(hours*3600)+(minutes*60)+(seconds)+(milliseconds/1000.0)
    return(time)
        
def add_lyric_to_screen():
    x = currentLyric
    currentLyric+=1
    lyric = lyricList[x]
    persistence = persistenceTime[x]
    l = tk.Label(root,text=lyric)
    l.pack()
    time.sleep(persistence)
    l.destroy()
    
with codecs.open("lyrics.srt", "rU", encoding="utf-8-sig") as srt_file:
    line1 = srt_file.readline()
    while line1:
        if RepresentsInt(line1):
            time = srt_file.readline()
            lyric=""
            line2 = srt_file.readline()
            
            while line2:
                if line2.strip() == "":
                    break
                lyric=lyric+line2+"\n"
                line2 = srt_file.readline()
            
            begin,sep,end=time.strip().split()
            delayBefore.append(time_in_seconds(begin)-prevTime)
            prevTime = time_in_seconds(begin)
            persistenceTime.append(time_in_seconds(end)-time_in_seconds(begin))
            lyricList.append(lyric)
        line1 = srt_file.readline()
        
root.mainloop()
for t in delayBefore:
    time.sleep(t)
    thread.start_new_thread(add_lyric_to_screen, ())
