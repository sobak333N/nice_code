from typing import List, Dict, Optional, Any, Type, Coroutine
from abc import ABC, abstractmethod
import aiohttp
import asyncio



class BaseRepository(ABC):
    @abstractmethod
    def __init__(self):
        self.session_type: Type = ...
    @abstractmethod
    async def fetch_data(self, user_id: int, session: Any) -> Optional[Dict[str,Any]]:
        pass


class DataBaseRepository(BaseRepository):
    def __init__(self):
        self.session_type: Type = ...

    async def fetch_data(self, user_id: int, session: Any):
        pass


class APIRepository(BaseRepository):
    def __init__(self):
        self.session_type = aiohttp.ClientSession
        self.fetch_url = f"https://jsonplaceholder.typicode.com/users/"

    async def fetch_data(self, user_id: int, session: aiohttp.ClientSession):
        print(f"[Worker {user_id}] Захватил семафор, начинаю работу...")
        try:
            await asyncio.sleep(1)
            cur_url = self.fetch_url + str(user_id)
            async with session.get(cur_url) as response:
                if response.status == 404:
                    return None
                response.raise_for_status()
                print(f"[Worker {user_id}] Завершил работу, освобождаю семафор")
                return await response.json()
        except (aiohttp.ClientResponseError, asyncio.TimeoutError):
            return None


class UserLoader:
    def __init__(
        self, 
        repository: BaseRepository,
        timeout: float=2.0,
        concurency: int=1
    ):
        self.repository = repository
        self.timeout = timeout
        self.concurency=concurency

    async def load_users(self, user_list: List[int]) -> Dict[int, Dict]:
        semaphore = asyncio.Semaphore(self.concurency)
        answer = {}
        async with self.repository.session_type() as session:
            tasks = [
                asyncio.create_task(
                    self._security_create_task(
                        self.repository.fetch_data(user_id, session),
                        semaphore
                    )
                ) 
                for user_id in user_list
            ]
            result = await asyncio.gather(*tasks)
            for res in result:
                if res is not None:
                    res_id = res["id"]
                    res.pop("id")
                    answer[res_id] = res
        return answer
    
    async def _security_create_task(self, coro: Coroutine, semaphore: asyncio.Semaphore) -> Any:
        try:
            async with semaphore:
                return await asyncio.wait_for(coro, self.timeout)
        except asyncio.TimeoutError:
            return None

async def main():
    users = [i for i in range(1,16)]
    user_loader = UserLoader(APIRepository())
    result = await user_loader.load_users(users)
    print(result)

asyncio.run(main())