import asyncio

async def tarea(nombre):
    await asyncio.sleep(2)
    print(f"Tarea {nombre} terminada")

async def main():
    await asyncio.gather(
        tarea(1),
        tarea(2)
    )

#Este comando crea el event loop
asyncio.run(main())
