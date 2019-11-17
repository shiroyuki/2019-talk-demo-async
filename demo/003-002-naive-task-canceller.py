# This is a modified copy of an example from https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel.
import asyncio


async def sleepy_brain():
    print('sleepy_brain(): Begin sleeping')
    try:
        for i in range(1, 6):
            await asyncio.sleep(1)
            print(f'sleepy_brain(): {i} sleep{"" if i == 1 else "s"}')
    except asyncio.CancelledError:
        print('sleepy_brain(): No more sleeping')
        raise
    print('sleepy_brain(): After sleeping')

async def main():
    print("main(): sleepy_brain (task) is created")

    # Create a "sleepy_brain" Task
    task = asyncio.create_task(sleepy_brain())

    print("main(): paused for a few seconds before cancelling sleepy_brain")

    # Wait for 1 second
    await asyncio.sleep(2)

    # NOTE: Despite of the fact that "task" is never awaited, "task" is running at this point.

    print("main(): task.cancel() will be called")
    task.cancel()
    print("main(): task.cancel() is called")

    try:
        await task
    except asyncio.CancelledError:
        print("main(): sleepy_brain (task) is now cancelled")

asyncio.run(main())
