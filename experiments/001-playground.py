import asyncio
import time


def func_001(tag: str):
    print(f'[{tag}] func_001: start')
    time.sleep(2)
    print(f'[{tag}] func_001: end')

    return 'r001'


async def afunc_001(tag: str):
    print(f'[{tag}] afunc_001: start')
    result = await asyncio.get_event_loop().run_in_executor(None, func_001, tag)
    print(f'[{tag}] afunc_001: end')

    return result


def func_002(tag: str):
    print(f'[{tag}] func_002: start')
    time.sleep(2)
    print(f'[{tag}] func_002: end')

    return 'r002'


async def afunc_002(tag: str):
    print(f'[{tag}] afunc_002: start')
    result = await asyncio.get_event_loop().run_in_executor(None, func_002, tag)
    print(f'[{tag}] afunc_002: end')

    return result


async def main():
    print(f'main: start')
    print(f'main: [set-000] afunc_001 = {afunc_001}')
    print(f'main: [set-000] func_001 = {func_001}')
    print(f'main: [set-000] afunc_002 = {afunc_002}')
    print(f'main: [set-000] func_002 = {func_002}')
    print(f'main: [set-001] waiting tasks with await')
    print(f'main: [set-001] t001 created')
    t001: asyncio.Task = asyncio.create_task(afunc_001('set-001'))
    print(f'main: [set-001] t002 created')
    t002: asyncio.Task = asyncio.create_task(afunc_002('set-001'))
    print(f'main: [set-001] sleeping')
    time.sleep(5)
    print(f'main: [set-001] t001 awaited')
    p001 = await t001
    print(f'main: [set-001] sleeping again')
    time.sleep(5)
    print(f'main: [set-001] t002 awaited')
    p002 = await t002
    print(f'main: [set-001] t001 inspecting')
    print(f'main: [set-001] t001.result() = {t001.result()}')
    print(f'main: [set-001] t001 inspected')
    print(f'main: [set-002] waiting tasks with await + gather')
    p003 = await asyncio.gather(afunc_001('set-002'), afunc_002('set-002'), return_exceptions=True)
    print(f'main: [set-003] waiting tasks with await + run_coroutine_threadsafe')
    print(f'main: [set-001] func_001 awaited')
    p004 = await asyncio.get_event_loop().run_in_executor(None, func_001, 'set-003')
    print(f'main: [set-001] func_002 awaited')
    p005 = await asyncio.get_event_loop().run_in_executor(None, func_002, 'set-003')
    print(f'main: [set-004] waiting tasks with await + gather + run_coroutine_threadsafe')
    p006 = await asyncio.gather(
        asyncio.get_event_loop().run_in_executor(None, func_001, 'set-004'),
        asyncio.get_event_loop().run_in_executor(None, func_002, 'set-004'),
        return_exceptions=True
    )
    print(f'main: compare results')
    print(f'main: p001 = {p001}')
    print(f'main: p002 = {p002}')
    print(f'main: p003 = {p003}')
    print(f'main: p004 = {p004}')
    print(f'main: p005 = {p005}')
    print(f'main: p006 = {p006}')
    print(f'main: end')

asyncio.run(main(), debug=True)