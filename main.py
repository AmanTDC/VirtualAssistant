import my_player
import my_opener
import speech_recognition as sr 
import playsound
import subprocess
from gtts import gTTS  
import os
from pynput.keyboard import Key, Controller
import wolframalpha 
from selenium import webdriver 
import chat
import webbrowser
import my_scrapper
import threading
import googlesearch
import keyboard
key_board = Controller()
play_csv=[]
def process_text(input): 
	try: 
		if 'search' in input or 'play' in input: 
			# a basic web crawler using selenium 
			search_web(input) 
			return

		elif "who are you" in input or "define yourself" in input: 
			speak = '''Hello, I am Person. Your personal Assistant. 
			I am here to make your life easier. You can command me to perform 
			various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak) 
			return

		elif "who made you" in input or "who created you" in input: 
			speak = "I have been created by Harshit, Aman, Aman, Avaneesh and Asif."
			assistant_speaks(speak) 
			return

		elif "geeksforgeeks" in input:# just 
			speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
			assistant_speaks(speak) 
			return

		elif "calculate" in input.lower(): 
			
			
			app_id = "WOLFRAMALPHA_APP_ID"
			client = wolframalpha.Client(app_id) 

			indx = input.lower().split().index('calculate') 
			query = input.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text 
			assistant_speaks("The answer is " + answer) 
			return

		elif 'open' in input: 
		
			open_re(input.lower()) 
			return

		else: 

			assistant_speaks("I can search the web for you, Do you want to continue?") 
			ans = get_audio() 
			if 'yes' in str(ans) or 'yeah' in str(ans): 
				search_web(input) 
			else: 
				return
	except : 

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
		ans = get_audio() 
		if 'yes' in str(ans) or 'yeah' in str(ans): 
			search_web(input)

def assistant_speaks(output):
        try:
                playsound.playsound(output+".mp3",True)
        except:
                if(output=='""'):
                        return
                toSpeak=gTTS(text=output,lang='en',slow=False)
                file=output+".mp3"
                toSpeak.save(file)
                playsound.playsound(file,True)

def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		keyboard.press_and_release('f9+f8');print("Speak...")		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	keyboard.press_and_release('f8+f7');print("Stop.")

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		#assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0

def search_web_re(input):
        str=input.split("search")[1]
        s=str.split(" ")
        query="+"
        query=query.join(s)
        query="https://www.google.com/search?q="+query
        webbrowser.open(query)

def search_web(input): 

	driver = webdriver.Firefox() 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'youtube' in input.lower(): 

		assistant_speaks("Opening in youtube") 
		indx = input.lower().split().index('youtube') 
		query = input.split()[indx + 1:] 
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
		return

	elif 'wikipedia' in input.lower(): 

		assistant_speaks("Opening Wikipedia") 
		indx = input.lower().split().index('wikipedia') 
		query = input.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		elif 'search' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 

		return
def open(text):
        try:
                text=text.split("open ")[1]
        except:
                assistant_speaks('What do you want me to open')
                text=get_audio().lower()
        
        assistant_speaks('Ok. Opening '+text)
        f=my_opener.open_it(text)
        if(f==1):
                print("hohoh")
                return
        else:
                open_on_web(text)

def open_on_web(input):
        lists=googlesearch.search(input)
        url=""
        for i in lists:
                url=i
                break
        webbrowser.open(url)


def process_text_re(text):
        medium=chat.chat(text)
        speak=medium[0]
        assistant_speaks(speak)
        if(medium[1]):
                data=medium[3]
                print(medium[2])
                exec(medium[2])

def answer_question(input):
        str=input
        try:
                str=str.split("who is")[1]
        except:
                try:
                        str=str.split("what is")[1]
                except:
                        print("occured---",str)
        print(str)
        a=googlesearch.search(str,stop=10)
        urls=[]
        for url in a:
                urls.append(url)
                print(url)
        for url in urls:
                if 'wikipedia' in url and 'list' not in url.lower():
                        speak=my_scrapper.scrap_answer(url)
                        assistant_speaks(speak[1][0])
                        return
                if 'wikipedia' in url and 'list' in url.lower():
                        speak=my_scrapper.scrap_answer_from_list(url)[0]
                        assistant_speaks(speak+" is"+str)
                        return
        webbrowser.open(urls[0])
                
def play_song(text):
        try:
                text=text.split("play ")[1]
        except:
                assistant_speaks('which song')
                text=get_audio()
                assistant_speaks('Ok. Playing '+text)
        assistant_speaks('Ok. Playing '+text)
        playing=my_player.play(text)
        if(playing==0):
                assistant_speaks("Couldn't find "+text)
        return
def stop():
        my_player.stop()
'''
def thread1():
        #assistant_speaks("What can i do for you?") 
	text = get_audio()
if text == 0:
        continue
	if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
		assistant_speaks("Ok bye, "+ name+'.') 
		break
	process_text_re(text.lower())'''

def key_driver():
        while(1):
                if keyboard.is_pressed('alt+f9'):
                        text=get_audio()
                        if text!=0:
                                process_text_re(text.lower())


def window_switch():
        keyboard.press('alt+tab')
        ll=(get_audio())
        try:
                if ll.lower()=='tu':
                        ll=2
                elif ll=='sex':
                        ll=6
                else:
                        ll=int(ll)
        except:
                ll=0
        for i in range(ll):
                keyboard.press('alt+tab')
        keyboard.release('alt+tab')
                 
def typer(text):
    print(text)
    try:
        text=text.split('type ')[1]
    except:
        text=get_audio()
    for i in range(len(text)):
        a=text[i]
        if a.isupper():
            a='shift+'+a
        #keyboard.press(a)
        str='keyboard.press(\"'+a+'\");keyboard.release(\"'+a+'\")'
        exec(str)

def driver():
        while(1):
                text=get_audio()
                if text!=0:
                        process_text_re(text.lower())




# Driver Code 
if __name__ == "__main__": 
	#assistant_speaks("What's your name ?")
	#name = get_audio()
	#assistant_speaks("Hello, " + name + '.')
	thread=threading.Thread(target=key_driver)
	thread.start()
	th=threading.Thread(target=driver);th.start()
	stopper=threading.Thread(target=my_player.stop_on_urgent);stopper.start()
