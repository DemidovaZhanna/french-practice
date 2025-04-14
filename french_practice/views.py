"""
Модуль для обработки запросов и отображения данных на сайте с использованием Django.

Этот модуль содержит функции для:
- Отображения списка изучаемых слов;
- Выполнения викторины и отображения результатов;
- Добавления новых слов;
- Вывод текстовых данных;
- Отображения статистики по терминологии.

Используемые функции:
- Обработка HTTP запросов и рендеринг шаблонов.
- Взаимодействие с модулями для работы с терминами, текстами и тестами (terms_work, texts_work).
- Валидация данных пользователя и добавление новых терминов в систему.

Функции:
    - index: Отображает главную страницу сайта.
    - terms_list: Отображает список терминов.
    - texts_list: Отображает список текстов.
    - test_input: Обрабатывает запросы из мини-викторины.
    - add_term: Отображает страницу для добавления нового термина.
    - send_term: Обрабатывает добавление нового термина.
    - show_stats: Отображает статистику по терминам.
"""


from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import texts_work


def index(request):
    return render(request, "index.html")    # работа с http запросом 


def terms_list(request):
    terms = terms_work.get_terms_for_table()    # извлечение терминов и их передача в html-шаблон 
    return render(request, "term_list.html", context={"terms": terms})


def texts_list(request):
    texts = texts_work.get_texts_for_table()    # извлечение текстов и их передача в html-шаблон 
    return render(request, "text_list.html", context={"texts": texts})


def test_input(request):
    return render(request, "quiz.html")


def add_term(request): 
    return render(request, "term_add.html")     # Добавление нового термина


def send_term(request): 
    if request.method == "POST":    # Обработка POST для отправки нового термина
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово добавлено"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    return add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()    # Извлечение статистики по добавленным словам
    return render(request, "stats.html", stats)
