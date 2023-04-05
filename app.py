import os; 
import openai;

from dotenv import load_dotenv

load_dotenv()

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
def cycle():
    print("type 'reset' to reset the cache. type 'quit' to quit the program.")
    text = input("insert a prompt: ")
    if(text == "reset"):
        messagesLog = [

         {"role": "system", "content": "You are a helpful assistant."}


        ]
        print("reset succesfully!")
    else:
        apppendToMessages(text);
        print(promptGpt()['choices'][0]['message']['content'])
    if(text == "quit"):
        quit()
    
    
    cycle();
cycle();

