# Random-Python-Scripts
Some random python scripts I made to kill time/make life easier.
For their individual functionalities, look below

## lyricfetcher.py
Accesses input.txt in the same directory, and reads the first line for a word, and reads each following line for artist names. Now looks up each artist on lyrics.com and searches for the word in all songs of the artist. Generates out.txt, a text file which prints artist names in descending order of number of appearances of the provided word.  

## playresume.py
Uses hardcoded (I'll change this someday) Way2SMS credentials and phone number. Messages the provided number when "Play stopped due to rain" changes on cricbuzz. The match tracked is the one being displayed on the homepage of cricbuzz. Easily customizable for a different match.  
Made out of frustration during Ind vs Pak, Summer of '17

## AutoLoginInOut internet.iitb.ac.in
Autologin and logout scripts for IITB's internal web access login. Uses the requests module instead of mechanize, hence much lighter than your conventional login scripts.  

## subs_easy.py
Extracts lyrics from lyrics.srt, and displays them according to their timestamp  
