from .models import Category


def get_popular_category(queryset, amount=3):
    """Возвращает популярные категории среди пользователей"""
    count = {}
    for i in Category.objects.all():
        if i.name not in count:
            count.update({i.name: 1})
        else:
            count[i.name] += 1
    sorted_count = sorted(count.items(), key=lambda x: x[1])  # сортирует словарь по значениям
    sorted_count.reverse()
    return sorted_count[:amount]
