from django.views.generic import TemplateView

menu = [
    [
        {"name": "Главная", "url": "/", "static": True}
    ],
    [
        {"name": "Админ-панель", "url": "admin:index", 'superuser': True}
    ],
    [
        {"name": "Зарегистрироваться", "url": 'register', 'without_authorization': True},
        {"name": "Войти", "url": 'login', 'without_authorization': True},
    ],
    [
        {'name': "Drawer",  
            "url": "/services/drawer/0", "static": True},
        {'name': "Сортировка массива",  
            "url": "/services/sort/2,-1,10,-20,100", "static": True},
        {"name": "Команды", "url": 'shell'}    
    ],
    [
        {"name": "Список товаров", "url": 'all-product'},
        {"name": "Добавить товар", "url": 'create-product', 'staff': True},
        {"name": "Удалить товар", "url": 'delete-product', 'staff': True}
    ],
    
    [
        {"name": "Загруженные файлы", "url": 'all-pdf'},
        {"name": "Загрузить файл", "url": 'create-pdf', 'staff': True},
        {"name": "Удалить файл", "url": 'delete-pdf', 'staff': True}
    ],
    [
        {"name": "Список городов", "url": 'all-city'},
        {"name": "Графики", "url": 'graphics-city'},
    ],
    [
        {"name": "Настройки", 
         "url": "settings", 
         'require_authorization': True}
    ],
    [
        {"name": "Выйти", 
         "url": "logout", 
         'require_authorization': True}
    ]
]

class HomeView(TemplateView):
    template_name = "navigation.html"
    extra_context = {'menu': menu, 
                     'title': "Страница навигации",
                     'require_back': False}