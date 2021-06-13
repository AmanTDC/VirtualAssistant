import csv
import pafy
import vlc
import requests
import googlesearch
import threading
import keyboard
play_csv=[]
def match(str1,str2):
	 for i in range(len(str1)):
		 if str1[i]!=str2[i]:
			 return 0
	 return 1
cols=[]
play_csv_len=0
with open('play_data.csv','r') as filee:

        reader=csv.reader(filee)
        cols=next(reader)
    
        
        for row in reader:
                
                play_csv.append(row)
        play_csv_len=reader.line_num
#print(cols)
#print(play_csv)

        
def stop_on_urgent():
    while(1):
        if keyboard.is_pressed('alt+f12'):
            stop()
        

window=vlc.Instance()
player=window.media_player_new()


def play(text):
    play_url=""
    found=0
    req_url=""
    print(play_csv_len)
    for i in range(play_csv_len-1):
        try:
            
            if play_csv[i]!=[] and match(text,play_csv[i][0])==1:
                print(play_csv[i][0])
                req_url=play_csv[i][1]
                found=1
        except:
            ("Error at value",i)
    if found==0:    
        for url in googlesearch.search(text,stop=20):
            if 'youtube.' in url and 'watch' in url:
                req_url=url
                break
        with open('play_data.csv','a') as write:
            writer=csv.writer(write)
            writer.writerow([text,req_url])
            
    
    print("URL :=",req_url)
    if(req_url==""):
        return 0
    video=pafy.new(req_url)
    if 'video' in text:
        best=video.streams[0]
    else:
        best= video.getbestaudio()
    play_url=best.url
    window=vlc.Instance()
    Media=window.media_new(play_url)
    player.set_media(Media)
    player.play()
    return 1

def pause():
    player.pause()

def stop():
    player.stop()
#play('despacito')
    
