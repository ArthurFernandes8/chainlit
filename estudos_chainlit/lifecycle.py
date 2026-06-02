import chainlit as cl

@cl.on_chat_start
async def inicio():
    cl.user_session.set("contador", 0)
    await cl.Message(
        content="Sesssão iniciada! O contador foi resetado para 0."
    ).send()

@cl.on_message
async def responder(message: cl.Message):
    contador = cl.user_session.get("contador", 0) + 1
    cl.user_session.set("contador", contador)
    
    await cl.Message(
        content=f"Mensagem {contador}: {message.content}"
    ).send()

@cl.on_chat_end
async def fim():
    print("Sessão encerrada.")