import chainlit as cl

@cl.set_starters
async def starters():
    return [
        cl.Starter(
            label="Me conte uma curiosidade",
            message="Me conte uma curiosidade interessante sobre o espaço.",
            icon="https://raw.githubusercontent.com/Chainlit/chainlit/main/backend/chainlit/public/logo_light.png",
        ),
        cl.Starter(
            label="Escreva um poema",
            message="Escreva um poema curto sobre o oceano.",
            icon="/public/write.svg",
        ),
        cl.Starter(
            label="Explique algo complexo",
            message="Explique como funciona a memória RAM de forma simples.",
        ),
    ]

@cl.on_chat_start
async def inicio():
    await cl.Message(content="Olá! Escolha uma opção ou escreva sua pergunta.").send()

@cl.on_message
async def responder(message: cl.Message):
    await cl.Message(content=f"Você perguntou: {message.content}").send()