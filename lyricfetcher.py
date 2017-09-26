from bs4 import BeautifulSoup
import requests
import urllib2
import time
from string import punctuation

def lyricslookup(url,word):
        k=url[7:]
        r  = requests.get("http://www.lyrics.com/print.php?id="+k)
        data = r.text
        soup = BeautifulSoup(data, "html.parser")
        try:
                m=soup.find(id='lyric-body-text').text
                print "Successfully parsed text for id:"+k
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
                        print "Successfully parsed contents for id:"+k
                        #return count(m,word)
                        c=0
                        x=m.split()
                        for s in x:
                                if s.strip(punctuation).lower()==word.lower():
                                        c+=1
                        return c
                except Exception as e:
                        print "Error for id "+k+': Lyrics not available or not found\n'
                        pass
        return 0
        
def songslookup(artist,word):
        url = "http://www.lyrics.com/artist.php?name="+artist.replace(" ","+")
        r  = requests.get(url)
        print "requested"#
        data = r.text
        soup = BeautifulSoup(data,"html.parser")
        print "opened"#
        albumsdiv = soup.find('div', class_="tdata-ext")
        c=0
        print 'Fetching..'
        for d in albumsdiv:
                if d.name=='div':
                        lyriclinks = d.findAll("strong")
                        for song in lyriclinks:
                                c=c+lyricslookup(song.a['href'],word)
        return c

if __name__ == '__main__':
        array=[]
        arrwordcnt=[]
        fi = open("input.txt", "r")
        line=fi.readline()
        while line.rstrip()!="":
                array.append(line.rstrip())
                line=fi.readline()
        word=fi.readline()
        for i in range(0,len(array)):
                arrwordcnt.append(songslookup(array[i],word))
        pts=zip(arrwordcnt,array)
        sort=sorted(pts,reverse=True)
        fo = open("out.txt", "w")
        for point in sort:
                fo.write(point[1]+'\n')
        fi.close()
        fo.close()