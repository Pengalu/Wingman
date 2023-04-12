import os; 
import openai;
import wavio;
import scipy;
import sounddevice as sd;
from dotenv import load_dotenv
from scipy.io.wavfile import write
load_dotenv()


#CONSTANTS
kDeviceId = 0;
kSampleTime = 3; #seconds
 #pulseaudio on linux runs @ device 11 and it defaults to device 0, which is some random card...
#just kidding, device 0 is the default device on windows, and device 11 is the default device on linux. great.
kSamplingFrequency = 44100;


openai.api_key = os.getenv("OPENAI_API_KEY")
messagesLog = [

    {"role": "system", "content": "You are a helpful assistant."}


]
def apppendToMessages(input):
     messagesLog.append({"role": "user", "content":input})
def promptGpt():

    hi = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",
    messages=messagesLog

        
        
    )
    return (hi);
#print(hi['choices'][0]['message']['content']);
#def cycle():
  #  print("type 'reset' to reset the cache. type 'quit' to quit the program.")
  #  text = input("insert a prompt: ")
  #  if(text == "reset"):
  #      messagesLog = [

   #      {"role": "system", "content": "You are a helpful assistant."}


   #     ]
   #     print("reset succesfully!")
 #   else:
  #      apppendToMessages(text);
  #      print(promptGpt()['choices'][0]['message']['content'])
  #  if(text == "quit"):
  #      quit()
    
    
  #  cycle();
#cycle();
def transcribe(audioFile): #transcribes an audio file and returns the text using openai's api
    return openai.Audio.transcribe("whisper-1",audioFile);

def audioCycle(duration,name="output.wav"):
    print("type 'r' to begin recording.")
    text=input("ready? ")
    if(text != "r"): audioCycle(duration);
    # Sampling frequency
  

    # Recording duration
    
    myrecording = sd.rec(int(duration * kSamplingFrequency), samplerate=kSamplingFrequency, channels=2)
    sd.wait()
    
    write("output.wav",kSamplingFrequency,myrecording)
    file = open(name, "rb")
    return(file)



def cycleAssistant():

    
    audio = audioCycle(kSampleTime)
    text = transcribe(audio)["text"]
    print(text)
    apppendToMessages(text)
    print(promptGpt()['choices'][0]['message']['content'])
    print("would you like to continue? (y/n)")
    text = input("y/n: ")
    if(text == "y"):
        cycleAssistant()
    else:
        quit()



sd.default.device = kDeviceId
cycleAssistant()

