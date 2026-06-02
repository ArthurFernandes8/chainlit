from datetime import datetime

import chainlit as cl

@cl.set_starters
def starters():
    return [
        cl.Starter(label="Que horas são?", message="Que horas são?"),
        cl.Starter(label="Me conte uma piada", message="Me conte uma piada")
        ]

@cl.on_chat_start
def inicio():
    contador = cl.user_session.get("contador", 0)
    horario = datetime.now().strftime("%H:%M")
    cl.Message(f"Bem-vindo! Agora são {horario}").send()

@cl.on_message
async def responder(message: cl.Message):
    n = cl.user_session.get("contador") + 1
    cl.user_session.set("contador", n)
    horario = datetime.now().strftime("%H:%M")
    await cl.Message(
        content=f"[(horario)] Mensagem #{n} - você disse: {message.content}").send()
     