from bs4 import BeautifulSoup
import argparse
import requests
import urllib2
import time
from string import punctuation

def lyricslookup(url,word,isVerbose):
        k=url[7:]
        r  = requests.get("http://www.lyrics.com/print.php?id="+k)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        try:
                m=soup.find(id='lyric-body-text').text
                if isVerbose:
                        print "Successfully parsed text for song id:"+k
                #return count(m,word)
                c=0
                x=m.split()
                for s in x:
                        if s.strip(punctuation).lower()==word.lower():
                                c+=1
                return c
        except:
                try:
                        m=soup.find("pre").contents[0]
                        if isVerbose:
                                print "Successfully parsed contents for id:"+k
                        #return count(m,word)
                        c=0
                        x=m.split()
                        for s in x:
                                if s.strip(punctuation).lower()==word.lower():
                                        c+=1
                        return c
                except Exception as e:
                        if isVerbose:
                                print "Error for id "+k+': Lyrics not available or not found\n'
                        pass
        return 0
        
def songslookup(artist,word,isVerbose):
        url = "http://www.lyrics.com/artist.php?name="+artist.replace(" ","+")
        r  = requests.get(url)
        if isVerbose:
                print "requested profile of '"+artist+"'"#
        data = r.text
        soup = BeautifulSoup(data,"html.parser")
        if isVerbose:
                print "parsed artist profile"#
        albumsdiv = soup.find('div', class_="tdata-ext")
        c=0
        if isVerbose:
                print 'Fetching..'
        for d in albumsdiv:
                if d.name=='div':
                        lyriclinks = d.findAll("strong")
                        for song in lyriclinks:
                                c=c+lyricslookup(song.a['href'],word,isVerbose)
        return c

if __name__ == '__main__':
        isVerbose = False
        array=[]
        arrwordcnt=[]
        fi = open("input.txt", "r")
        line=fi.readline()
        while line.rstrip()!="":
                array.append(line.rstrip())
                line=fi.readline()
        word=fi.readline()
        for i in range(0,len(array)):
                arrwordcnt.append(songslookup(array[i],word,isVerbose))
        pts=zip(arrwordcnt,array)
        sort=sorted(pts,reverse=True)
        fo = open("out.txt", "w")
        for point in sort:
                fo.write(point[1]+'\n')
        fi.close()
        fo.close()
