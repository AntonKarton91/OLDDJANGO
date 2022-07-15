from django.utils.text import slugify
from django.views import View

main_menu = [
    {'title': 'главная', 'url': "main", 'submenu':[]},
    {'title': 'отдел разработки', 'url': 'dko', 'submenu':[{'subtitle': 'Задачи', 'url': 'dkotasks'},
                                                        {'subtitle': 'Оборудование', 'url': 'equipmentClient'}]},
    {'title': 'отдел продаж', 'url': 'trades', 'submenu':[]},
    {'title': 'снабжение', 'url': 'supplies', 'submenu':[]},
]

tasks_tags = [
    (1, 'Конструктив'),
    (2, 'Дизайн'),
    (3, 'Выдано в работу'),
    (4, 'Срочно'),
    (5, 'Доработка'),
]

task_type = [
    (1, 'Конструктив'),
    (2, 'Дизайн'),
    (3, 'РМ'),
]


class MainMenuMixin(View):
    def get_user_context(self, *args, **kwargs):
        context = kwargs
        context['menu'] = main_menu
        return context

    def translateForSlug(self, val):
        slug = slugify(val.translate(
            str.maketrans(
                "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
            )))
        return slug

