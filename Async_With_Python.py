import asyncio

async def task(name):
    print(f"Task {name} Started...", flush=True)
    await asyncio.sleep(1)
    print(f"Task {name} Ended.", flush=True)

async def main():
    tasks = [task(i) for i in range(1, 4)]
    for t in asyncio.as_completed(tasks):
        await t

asyncio.run(main())
print("Script Finished", flush=True)