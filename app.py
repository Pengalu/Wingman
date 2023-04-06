import os; 
import openai;
import wavio;
import scipy;
import sounddevice as sd;
from dotenv import load_dotenv
from scipy.io.wavfile import write
load_dotenv()


#CONSTANTS
kDeviceId = 11; #pulseaudio on linux runs @ device 11 and it defaults to device 0, which is some random card...
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
def audioCycle(duration):
    print("type 'r' to begin recording.")
    text=input("ready? ")
    if(text != "r"): audioCycle(duration);
    # Sampling frequency
  

    # Recording duration
    
    myrecording = sd.rec(int(duration * kSamplingFrequency), samplerate=kSamplingFrequency, channels=2)
    sd.wait()
    write("output.wav",kSamplingFrequency,myrecording)
sd.default.device=kDeviceId;
audioCycle(5)
    

