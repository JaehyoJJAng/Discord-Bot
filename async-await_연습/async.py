import time
import asyncio

async def async_wait(n:int)-> None:
    for i in range(1 , 3 + 1):
        await asyncio.sleep(1)
        print(f'{n} : {i}번째')

async def process_async():
    start = time.time()
    await asyncio.wait(
        [
            async_wait(n=3),
            async_wait(n=1)
        ]
    )
    end = time.time()

    print(f'경과 시간 : {end - start}')    

def main() -> None:
    asyncio.run(process_async())

main()