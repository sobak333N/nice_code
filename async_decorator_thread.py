import time
from datetime import datetime
import asyncio

def measure_time(func):
    async def wrapper(*args, **kwargs):
        start_time = datetime.now()
        
        if asyncio.iscoroutinefunction(func):
            result = await func(*args, **kwargs) 
        else: 
            result = await asyncio.to_thread(func,*args, **kwargs)

        end_time = datetime.now()

        print(end_time-start_time)
        return result
    
    return wrapper  


@measure_time
def slow_function(lox):
    print(lox)
    time.sleep(2)

@measure_time
def fast_function():
    time.sleep(0.1)


@measure_time
async def async_func():
    await asyncio.sleep(1)

async def main():
  await slow_function(2)
  await fast_function()
  # asyncio.run(async_func())
  await async_func()


asyncio.run(main())