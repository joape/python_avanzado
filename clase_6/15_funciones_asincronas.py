import asyncio


async def enviar_email_que_tarda_mas(nombre: str):
    print(f"🥲 Enviando email a {nombre}")
    await asyncio.sleep(5)  # simulando
    print(f"✅ Email enviado a {nombre}")


async def enviar_email(nombre: str):
    print(f"Enviando email a {nombre}")
    await asyncio.sleep(2)  # simulando
    print(f"✅ Email enviado a {nombre}")


async def main():
    await asyncio.gather(
        enviar_email_que_tarda_mas("Pepe"),
        enviar_email("Juan"),
        enviar_email("Luis"),
    )


asyncio.run(main())
