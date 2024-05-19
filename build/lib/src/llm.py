import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

from src.config import instruction

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


#def ask_bot(user_message,instruction):
    
    #model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    
    
    #respones=model(
    #[
        #SystemMessage(content=instruction),
        #HumanMessage(content=user_message),
    #]
#)
    
    #return respones.content

def ask_bot(message):
    llm=ChatGoogleGenerativeAI(model="gemini-pro")
    respones=llm.invoke(message)
    return respones.content

if __name__=="__main__":
    print("welcome to chat bot!")
    message=ask_bot("what is the meaninig of machine learning")
    #user_message = "hi how are you?"
    #respones=ask_bot(user_message)
    print(message)