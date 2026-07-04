# Parts.kz – Каталог автомобильных запчастей

Django приложение для управления и поиска автомобильных запчастей. Проект предоставляет удобный интерфейс для фильтрации запчастей по марке, модели, типу и году выпуска.

## 📋 Описание

Parts.kz — это полнофункциональное решение для создания каталога автомобильных запчастей. Приложение позволяет:

- Управлять базой данных запчастей (запасных частей)
- Фильтровать запчасти по множеству параметров (марка, модель, тип, год выпуска)
- Искать запчасти по названию, бренду, серии, месту производства
- Отслеживать доступность и количество на складе
- Хранить информацию об условии (новая/б/у), цене и изображениях

## 🚀 Технологический стек

- **Backend**: Django 5.2+
- **API**: Django REST Framework + drf-yasg (Swagger/OpenAPI)
- **БД**: PostgreSQL (конфигурируется через .env)
- **Background tasks**: Celery
- **Фильтрация**: django-filter
- **Утилиты**: Unidecode (транслитерация)

## 📦 Требования

```
django
djangorestframework
drf-yasg
django-filter==24.3
celery
unidecode
```

## 🔧 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/aresinferno/parts.kz.git
cd parts.kz
```

### 2. Создание виртуального окружения
```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate     # для Windows
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Конфигурация переменных окружения
Скопируй файл `.env.example` в `.env` и заполни необходимые переменные:

```bash
cp .env.example .env
```

Отредактируй `.env`:
```env
DEBUG=True                    # Режим разработки
SECRET_KEY=your_secret_key   # Секретный ключ Django
DB_NAME=parts_db             # Имя базы данных
DB_USER=postgres             # Пользователь БД
DB_PASSWORD=your_password    # Пароль БД
DB_HOST=localhost            # Хост БД
DB_PORT=5432                 # Порт БД
```

### 5. Миграции БД
```bash
python manage.py migrate
```

### 6. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 7. Запуск сервера
```bash
python manage.py runserver
```

Приложение будет доступно по адресу: `http://localhost:8000`

## 📁 Структура проекта

```
parts.kz/
├── core/                   # Основная конфигурация Django проекта
│   ├── settings.py        # Настройки проекта
│   ├── urls.py            # Маршруты главного приложения
│   ├── wsgi.py            # WSGI конфигурация
│   └── asgi.py            # ASGI конфигурация
├── parts/                 # Главное Django приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # Представления (views)
│   ├── urls.py            # Маршруты приложения
│   ├── admin.py           # Конфигурация админ-панели
│   └── migrations/        # Миграции БД
├── Templates/             # HTML шаблоны
├── static/                # Статические файлы (CSS, JS)
├── media/                 # Загруженные медиафайлы
├── manage.py              # Утилита управления Django
├── requirements.txt       # Зависимости проекта
└── .env.example           # Пример файла конфигурации
```

## 🗂️ Модели данных

### PartBrand (Марка)
- `name` — название марки (уникальное)
- `slug` — URL-friendly версия названия
- `picture` — логотип марки

### PartSeries (Модель)
- `brand` — связь с маркой
- `name` — название модели
- `slug` — URL-friendly версия названия

### PartType (Тип запчасти)
- `name` — название типа (двигатель, коробка передач и т.д.)
- `slug` — URL-friendly версия названия

### Part (Запчасть)
- `part_type` — тип запчасти
- `part_number` — артикул
- `brand` — производитель
- `year` — год выпуска
- `price` — цена
- `car_series` — серия автомобиля
- `availability` — наличие
- `image` — изображение
- `condition` — состояние (новая/б/у)
- `quantity` — количество на складе
- `made_in` — место производства

### PartPlace (Место производства)
- `name` — название страны/места

## 🔍 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|---------|
| GET | `/` | Главная страница с фильтрацией |
| GET | `/search/` | Поиск по запчастям |

## 🛠️ Администрирование

Админ-панель Django доступна по адресу: `http://localhost:8000/admin/`

Используй учетные данные суперпользователя, созданные на этапе установки.

## 🔄 Запуск Celery (для фоновых задач)

```bash
celery -A core worker -l info
```

## 📝 Лицензия

Не указана

## 👤 Автор

[aresinferno](https://github.com/aresinferno)

## 💬 Обратная связь

Если у тебя есть вопросы или предложения, откройте issue в репозитории.

---

**Последнее обновление**: July 4, 2026