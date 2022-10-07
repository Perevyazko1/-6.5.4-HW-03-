from django_filters import FilterSet
from .models import News

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class NewsFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = News
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           # количество товаров должно быть больше или равно
           'category': ['gt'],
           'dateCreation': [
               'lt',  # дата должна быть меньше или равна указанной
               'gt',  # дата должна быть больше или равна указанной
           ],
       }
