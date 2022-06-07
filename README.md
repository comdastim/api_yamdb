#черновик
# api_yamdb
api_yamdb

### Описание:
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на предустановленные категории (Categories), список которых может быть расширен администратором.
В каждой категории произведений существует предустановленные жанры (Genres), перечень которых может быть пополнен администратором.
Сами произведения в YaMDb не хранятся, пользователи могут ознакомиться с текстовым описанием произведения и оставить отзыв (Review) и поставить оценку. Из оценок формируется усреднённая оценка произведения — рейтинг.
К отзывам пользователи также могут оставлять комментарии (Comments). 

### Установка
Клонировать репозиторий и перейти в него в командной строке:
git clone https://@github.com/comdastim/api_yamdb.git

Перейти в api_yamdb:
cd api_yamdb

Cоздать виртуальное окружение:
python3 -m venv env

Активировать виртуальное окружение:
source env/bin/activate(для macOS или Linux:) 
либо 
source/venv/Scripts/activate (для Windows)

Установить зависимости из файла requirements.txt:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:
python3 manage.py migrate

Запустить проект:
python3 manage.py runserver

### Техническое описание проекта
По адресу http://127.0.0.1:8000/redoc/  можно найти документацию, в которой описаны примеры возможных запросов к API и структура ожидаемых ответов.



