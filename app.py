import chainlit as cl
#from src.llm import ask_bot
#from src.config import instruction

@cl.on_message
async def main(message:cl.Message):

    #response=ask_bot(user_message.content,instruction)
    
    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()
