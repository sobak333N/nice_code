### **Docker и Docker Compose: Основные Тезисы и Конспекты**

---

## **1. Основы Docker**
- **Docker** — инструмент для создания, доставки и запуска контейнеров, которые изолируют приложение с его зависимостями.
- Контейнеры строятся на основе **образов**, описанных в `Dockerfile`.

### **Слои и Кэширование**
1. **Каждая команда в Dockerfile создаёт новый слой:**
   - `FROM`, `RUN`, `COPY`, `ADD` создают слои.
   - Слои кэшируются, чтобы ускорить сборку, если команда и её входные данные не изменились.

2. **Оптимизация слоёв:**
   - Разделяйте зависимости (`COPY requirements.txt`) и код (`COPY . .`) для эффективного кэширования.
   - Устанавливайте зависимости до копирования кода:
     ```dockerfile
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     COPY . .
     ```

3. **Сокращение количества слоёв:**
   - Объединяйте команды `RUN`:
     ```dockerfile
     RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
     ```

4. **Удаление временных файлов:**
   - Уменьшает размер образа:
     ```dockerfile
     RUN apt-get clean && rm -rf /var/lib/apt/lists/*
     ```

5. **Используйте `.dockerignore`:**
   - Исключает ненужные файлы из контекста сборки:
     ```
     .git
     __pycache__
     *.pyc
     .env
     ```

---

## **2. Основные Команды в Dockerfile**

1. **`FROM`** — задаёт базовый образ:
   ```dockerfile
   FROM python:3.10-slim
   ```

2. **`WORKDIR`** — задаёт рабочую директорию:
   ```dockerfile
   WORKDIR /app
   ```

3. **`COPY`** — копирует файлы в контейнер:
   ```dockerfile
   COPY requirements.txt .
   ```

4. **`RUN`** — выполняет команды на этапе сборки:
   ```dockerfile
   RUN pip install --no-cache-dir -r requirements.txt
   ```

5. **`CMD`** — задаёт команду по умолчанию при запуске контейнера:
   ```dockerfile
   CMD ["python", "app.py"]
   ```

6. **`ENTRYPOINT`** — задаёт команду, которую всегда будет выполнять контейнер:
   ```dockerfile
   ENTRYPOINT ["python"]
   CMD ["app.py"]
   ```

7. **`ENV`** — задаёт переменные окружения:
   ```dockerfile
   ENV APP_ENV=production
   ```

8. **`EXPOSE`** — документирует порты:
   ```dockerfile
   EXPOSE 8000
   ```

9. **`VOLUME`** — создаёт точку монтирования для хранения данных:
   ```dockerfile
   VOLUME /data
   ```

10. **`HEALTHCHECK`** — проверяет состояние контейнера:
    ```dockerfile
    HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
      CMD curl -f http://localhost:8000/health || exit 1
    ```

---

## **3. Docker Compose**
- **Docker Compose** используется для управления многоконтейнерными приложениями.
- Контейнеры описываются в `docker-compose.yml`.

### **Структура `docker-compose.yml`**
Пример:
```yaml
version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app
    depends_on:
      - db
    environment:
      - APP_ENV=production

  db:
    image: postgres:14
    volumes:
      - db_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydatabase

volumes:
  db_data:
```

---

### **Ключевые элементы Docker Compose**

1. **`services`** — описывает контейнеры:
   - Например, `app`, `db`, `redis`.

2. **`build`** — собирает образ из `Dockerfile`:
   ```yaml
   build:
     context: .
     dockerfile: Dockerfile
   ```

3. **`image`** — указывает готовый образ:
   ```yaml
   image: postgres:14
   ```

4. **`volumes`** — монтирование данных:
   - Именованные:
     ```yaml
     volumes:
       - db_data:/var/lib/postgresql/data
     ```
   - Привязанные к хосту:
     ```yaml
     volumes:
       - ./app:/app
     ```

5. **`ports`** — пробрасывание портов:
   ```yaml
   ports:
     - "8000:8000"
   ```

6. **`environment`** — задаёт переменные окружения:
   ```yaml
   environment:
     - POSTGRES_USER=user
     - POSTGRES_PASSWORD=password
   ```

7. **`depends_on`** — задаёт зависимости между контейнерами:
   ```yaml
   depends_on:
     - db
   ```

8. **`networks`** — задаёт пользовательские сети:
   ```yaml
   networks:
     mynetwork:
       driver: bridge
   ```

---

## **4. `depends_on` и `healthcheck`**

### **`depends_on`**
- Указывает порядок запуска контейнеров.
- **Важно:** `depends_on` не проверяет готовность контейнера, только его запуск.

Пример:
```yaml
depends_on:
  db:
    condition: service_healthy  # Ожидание готовности контейнера
```

---

### **`healthcheck`**
- Проверяет, что контейнер готов к работе.
- Используется совместно с `depends_on` для надёжной зависимости.

Пример:
```yaml
healthcheck:
  test: ["CMD", "pg_isready", "-U", "user"]
  interval: 10s
  timeout: 5s
  retries: 3
```

---

## **5. Лучшие практики**

1. **Оптимизируйте слои:**
   - Разделяйте команды копирования зависимостей и кода.
   - Удаляйте временные файлы после установки.

2. **Используйте `.dockerignore`:**
   - Исключайте ненужные файлы из контекста сборки.

3. **Используйте `healthcheck`:**
   - Проверяйте готовность критически важных сервисов, например, базы данных или API.

4. **Управляйте окружением:**
   - Используйте переменные окружения для конфигурации (`ENV`, `environment`).

5. **Организуйте сервисы:**
   - Разделяйте сервисы на логические группы, например, приложение, база данных, кеш.

6. **Проверяйте конфигурацию:**
   - Используйте команду:
     ```bash
     docker-compose config
     ```

7. **Управляйте проектами:**
   - Используйте разные файлы для разработки и продакшена:
     ```bash
     docker-compose -f docker-compose.prod.yml up
     ```

---

Эти тезисы помогут вам эффективно использовать Docker и Docker Compose для разработки, развертывания и управления приложениями!