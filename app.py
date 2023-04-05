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
    text = input("insert a prompt: ")
    apppendToMessages(text);
    print(promptGpt()['choices'][0]['message']['content'])
    cycle();
cycle();

