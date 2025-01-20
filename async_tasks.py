import aiohttp
import asyncio
import time
from datetime import datetime

urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
]


def measure_time(func):
    async def wrapper(*args, **kwargs):
        start = datetime.now()
        if asyncio.iscoroutinefunction(func):
            result = await func(*args, **kwargs)
        else:
            result = await asyncio.to_thread(func, *args, **kwargs)
        end = datetime.now()
        print(f"time of function execution = {end-start}")
        return result

    return wrapper


@measure_time
async def fetch(session, url) -> dict:
    try:
        async with session.get(url) as response:
            data = await response.json()
            print(type(data))
            # print((data))
            return data
    except Exception as e:
        print(f"error while request to {url} - {e}")


class AsyncTasksExecution:
    def __init__(self,urls=None):
        self.urls = urls
    
    async def start_tasks(self):
        async with aiohttp.ClientSession() as session:
            # another
            tasks = []
            for url in urls:
                task = asyncio.create_task(fetch(session,url))
                tasks.append(task)
            
            result = await asyncio.gather(*tasks)
            return result
            
            # tasks = [fetch(session,url) for url in urls]
            # result = await asyncio.gather(*tasks)
            # return result


async def main():
    async_task_executor = AsyncTasksExecution(urls=urls)
    res = await async_task_executor.start_tasks()
    # print(res)

asyncio.run(main())