import os,time
import codecs
def parset(line):
    
    hours = int(line.split(':')[0])
    minutes = int(line.split(':')[1])
    seconds = int(line.split(':')[2].split(',')[0])
    milliseconds=int(line.split(':')[2].split(',')[1])
    time=(hours*3600)+(minutes*60)+(seconds)+(milliseconds/1000)
    print(time)
    return(time)


#srt_file = open("lyrics.srt",'rU')
with codecs.open("lyrics.srt", "rU", encoding="utf-8-sig") as srt_file:
    s=srt_file.readlines()
    for i in range(len(s)):
        if(s[i].split('\n')[0][0].isdigit()):

            if(len(s[i].split('\n')[0])>2):
                if (s[i].split('\n')[0][2].isdigit()):
                    continue
                else:
                    print(str(5))
                    s1=s[i].split(' --> ')[1].split('\n')[0]
                    print(s1)
                    s2=s[i].split(' --> ')[0]
                    print(s2)
                    delay=parset(s1)-parset(s2)
                    print(str(delay))
                    time.sleep(delay)
        else:
            print(s[i].split('\n')[0].split('\n')[0])
                  

        

# i=0
# s=(srt_file.readlines())
# for i in range()

# print (srt_file.readlines())
srt_file.close()
