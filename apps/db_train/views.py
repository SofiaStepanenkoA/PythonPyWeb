from django.shortcuts import render
from django.views import View
# from .models import ...
from .models import Author, AuthorProfile, Entry, Tag


from django.db.models import Q, Max, Min, Avg, Count

class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        self.answer2 = Author.objects.annotate(num_entries=Count('entries')).order_by('-num_entries').first()   # TODO Какой автор имеет наибольшее количество опубликованных статей?
        Tags_id= Tag.objects.filter(
            Q(name__icontains='Кино') | Q(name__icontains='Музыка'))  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = Entry.objects.filter(id__in = Tags_id)
        self.answer4 = Author.objects.filter(gender='ж').count()  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer5 = round((Author.objects.filter(status_rule=True).count() / Author.objects.count()) * 100 )   # TODO Какой процент авторов согласился с правилами при регистрации?

        Stage_id = AuthorProfile.objects.filter(stage__range=(1, 5)) # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(id__in =Stage_id)
        self.answer7 = Author.objects.order_by('-age').first()  # TODO Какой автор имеет наибольший возраст?
        self.answer8 = Author.objects.filter(
            phone_number__isnull=False).count()  # TODO Сколько авторов указали свой номер телефона?
        self.answer9 = Author.objects.filter(age__lt=25)  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer10 =Author.objects.annotate(count=Count('create_at')).values('username', 'count') # TODO Сколько статей написано каждым автором?

        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)
