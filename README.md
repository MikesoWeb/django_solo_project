# django_solo_project

Здесь я тестировал чтобы создать проект без приложений с несколькими страницами

Так же создал в корне файл admin.py чтобы попробовать зарегистрировать модели именно так

Так же пробовал эксперименты с urls из корня дял проекта.

Еще потренировался в файлом игноров, ну и не забыл перед заливом удалить ключ в settings.py

Изучая django я провожу различные эксперименты как в IDE так и в shell django

Создав проект blog но не создавая приложения я решил попробовать что будет если я создам не достающие файлы 
и попробую соотнести проект как приложение. Эксперимент подтвердил мои ожидания:

создавая проект командой django-admin startproject blog создалось автоматом приложение blog в папке blog

Но оно не полное чтоли, не знаю как объяснть, но оно не похоже на приложение если:

django-admin startapp name_app

Ну действительно в нем не хватает файлов:

admin.py
views.py 

В принципе я хорошо поэкспериментировал и запустил приложение с четырьмя страницами, зарегистрировал две модели Post, Tag
создал templates, создал миграции и настроил пути

Хороший день.
