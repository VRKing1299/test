import speech_recognition as sr
import win32com.client as win
import datetime
import wikipedia
import webbrowser



speaker = win.Dispatch("SAPI.SpVoice")
def say(text):
    # speaker = win.Dispatch("SAPI.SpVoice")
    print(text)
    speaker.Speak(text)
# print ("enter the word ")
# s=input()
# speaker.Speak(s)

def wishme():
    hours= int(datetime.datetime.now().hour)
    if hours>=4 and hours<12 :
        speaker.Speak('Good morning')
    elif hours>=12  and hours<16 :
        speaker.Speak("Good afer noon")
    elif hours>=16 and hours<22 :
        speaker.speak("good evening")
    else :
        speaker.speak("good night")
    speaker.Speak("Hello , I am Jarvis How may I help you")
    
    
def takecommands():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
    try:
        query=r.recognize_google(audio , language="en-in")
        # print("user said :", query)
        # say(query)
        return query
    except Exception as e:
        # print(e)
        # say("please say it again")
        return "please say it again"
        
    

def searching_wikipedia(query):
    say("searching wikipedia")
    try:
        query=query.replace("wikipedia","").replace("search","").replace("about","")
        result=wikipedia.summary(query, sentences=2)
        say("according to wikipedia :" + result)
    except wikipedia.exceptions.DisambiguationError as e:
        say("There are multiple results for this query. Please be more specific.")
    except wikipedia.exceptions.PageError:
        say("I could not find any results for this query on Wikipedia.")
    except Exception as e:
        say("An error occurred while searching Wikipedia.")
        
        
def searching_youtube(query):
    query=query.replace("youtube","").replace("search","").replace("about","")
    say("searching youtube")
    webbrowser.open(".youtube.com/results?search_query="+query)
    
    
    
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommands().lower()
        ''' Check if "jarvis" is in the query '''
        if "jarvis" in query:
        #     ''' Split the query at the first occurrence of "jarvis" and take everything after it '''
            parts = query.split("jarvis", 1)
            query = parts[1].strip()
        # if query.startswith("jarvis"):
            query = query.replace("jarvis", "")
            
            say(query)
            
            
        #task executed based on query
            if "wikipedia" in query :
                searching_wikipedia (query)
            
            elif "search youtube" in query :
                searching_youtube (query)    
                    
            elif "google" in query :
                say ("searching on google")
                query = query.replace("search","").replace("google","")
                # url("")
            elif "exit program" in query:
                say("shutting down the app")    
                break
                
        
     