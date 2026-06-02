import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
     maiusculas = message.content.upper()
     num_caracteres = len(message.content)
     await cl.Message(content=f"Você disse: {maiusculas} (com {num_caracteres} caracteres)").send()