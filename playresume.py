from bs4 import BeautifulSoup
import requests
import urllib2
import cookielib
import sys
import os
import time
import subprocess       
from getpass import getpass
from stat import *

def message(message,number):    
    username = "<You phone number here>" #TO BE MODIFIED
    passwd = "<Your password here>" #TO BE MODIFIED

    message = "+".join(message.split(' '))

 #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

 #For cookies

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

 #Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"
        #return()

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
        #return()

    print "success" 
    #return ()

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

if __name__ == '__main__':

        while True:
                url = "http://www.cricbuzz.com/"
                r  = requests.get(url)
                print "requested"#
                data = r.text
                soup = BeautifulSoup(data)
                mydivs = soup.findAll("div", { "class" : "cb-lv-scrs-col cb-text-live" })
                if mydivs[0].text!="Play stopped due to rain":
                        sendmessage("Play has started!")
                        message("Play has started!","<YOUR PHONE NUMBER HERE>")
                        break
                time.sleep(10)
