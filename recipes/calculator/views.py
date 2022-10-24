from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def count_person(request,dish):
    count = request.GET.get("servings")
    if count != None:
        print(count)
        int_count = int(count)
        value_count = DATA[dish]
        for ingr in value_count:
            value_count[ingr] = value_count[ingr] * int_count
        context = {'recipe':value_count}
        return render(request, 'calculator/index.html', context)

    else:
        context = {'recipe':DATA[dish]}
        return render(request, 'calculator/index.html', context)





# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
