import asyncio
import random

async def worker(semaphore: asyncio.Semaphore, worker_id: int):
    """
    Каждый worker «приобретает» семафор, потом «делает работу» (имитируем),
    и наконец освобождает семафор.
    """
    async with semaphore:
        print(f"[Worker {worker_id}] Захватил семафор, начинаю работу...")
        # Имитируем некоторое время работы
        await asyncio.sleep(random.uniform(0.5, 2.0))
        print(f"[Worker {worker_id}] Завершил работу, освобождаю семафор.")

async def main():
    # Допустим, мы хотим ограничить параллельное выполнение максимум 3 задач.
    concurrency_limit = 3
    semaphore = asyncio.Semaphore(concurrency_limit)

    # Создадим 10 «воркеров»
    tasks = []
    for i in range(10):
        t = asyncio.create_task(worker(semaphore, i))
        tasks.append(t)

    # Дождёмся завершения всех
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
