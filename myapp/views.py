import asyncio
from datetime import datetime, date, time
from os import name

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseForbidden, \
    HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.template.response import TemplateResponse
from .models import Person,Order
from .forms import UserForm
from django.db.models import Avg, Max, Min, Sum
from django.db import connection

# def index(request):
#     return HttpResponse("Hello")



# def index(request):
#     return HttpResponse('<h2>Главная</h2>')
# def about(request):
#     return HttpResponse('<h2>О сайте</h2>')
# def contact(request):
#     return HttpResponse('<h2>Контакты</h2>')



# def index(request):
#     return HttpResponse('<h2>Главная</h2>')
# def about(request,name,age):
#     return HttpResponse(f''
#                         f'<h2>О пользователе</h2>'
#                         f'<p>Имя: {name}</p>'
#                         f'<p>Возраст: {age}</p>')



# def index(request):
#     host=request.META['HTTP_HOST']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path = request.path
#     return HttpResponse(f"<p>Host: {host}</p>"
#                         f"<p>Path: {path}</p>"
#                         f"<p>User-Agent: {user_agent}</p>")



# def index(request):
#     return HttpResponse('Произошла ошибка',status=400,reason='Incorrect data')


# def index(request):
#     return HttpResponse("<h1>Hello World!</h1>",content_type="text/plain",charset='utf-8')


# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
# def user(request, name="Undefined", age =0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
# def user(request, name="Undefined", age =0):
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


# def index(request):
#     return HttpResponse("Главная страница")
# def products(request):
#     return HttpResponse("Список товаров")
# def new(request):
#     return HttpResponse("Новые товары")
# def top(request):
#     return HttpResponse("Наиболее популярные товары")




# def index(request):
#     return HttpResponse("Главная страница")
# def products(request, id):
#     return HttpResponse(f"Товар {id}")
# def comments(request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")
# def questions(request, id):
#     return HttpResponse(f"Вопросы о товаре {id}")


# def index(request):
#     return HttpResponse("<h2>Главная</h2>")
# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


# def index(request):
#     return HttpResponse("Index")
# def about(request):
#     return HttpResponse("About")
# def contact(request):
#     return HttpResponseRedirect("/about")
# def details(request):
#     return HttpResponsePermanentRedirect("/")


# def index(request, id):
#     people = ["Tom", "Bob", "Sam"]
#     if id in range(0, len(people)):
#         return HttpResponse(people[id])
#     else:
#         return HttpResponseNotFound("Not Found")
# def access(request, age):
#     if age not in range(1, 111):
#         return HttpResponseBadRequest("Некорректные данные")
#     if (age > 17):
#         return HttpResponse("Доступ разрешен")
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")




# def index(request):
#     return JsonResponse({"name": "Tom", "age": 38})




# def index(request):
#     bob = Person("Bob", 41)
#     return JsonResponse(bob, safe=False, encoder=PersonEncoder)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#         return super().default(obj)



# def set(request):
#     username = request.GET.get('username','Undefined')
#     response =HttpResponse(f'Hello {username}')
#     response.set_cookie('username',username)
#     return response



# def set(request):
#     username = request.GET.get('username','Undefined')
#     response =HttpResponse(f'Hello {username}')
#     response.set_cookie('username',username)
#     return response
# def get(request):
#     username = request.COOKIES['username']
#     return HttpResponse(f'Hello {username}')


# def index(request):
#     return render(request,'index.html')


# def index(request):
#     return TemplateResponse(request, 'index.html')



# def index(request):
#     data={'header':'Hello Django','message':'Welcome to Python'}
#     return render(request,'index.html',context=data)



# def index(request):
#     header='User data'
#     langs=['Python','C++','C#']
#     user={'name':'Sammy','age':23}
#     address={'Furkat',23,45}
#     data={'header':header,'langs':langs,'user':user,'address':address}
#     return render(request,'index.html',context=data)



# def index(request):
#     return render(request, "index.html",context={'body':'<h1>Hello World!</h1>'})



# def index(request):
#     return render(request, "index.html")


# def index(request):
#     data={'n':0}
#     return render(request,'index.html',context=data)


# def index(request):
#     langs=['Python','JavaScript','Java','C#','C++']
#     return render(request, "index.html",context={'langs':langs})


# def index(request):
#     data={'red':'красный','green':'зеленый','blue':'cиний'}
#     return render(request,'index.html',{'data':data})



# def index(request):
#     return render(request, "index.html")



# def index(request):
#     return render(request, "index.html", context={"my_date": datetime.now()})



# def index(request):
#     return render(request, "index.html")



# def index(request):
#     return render(request, "index1.html")
# def contacts(request):
#     return render(request, "contacts.html")



# def index(request):
#     return render(request, "index.html",context={'site':'METANIT.COM'})



# def index(request):
#     return render(request, "index.html")
# def postuser(request):
#     name=request.POST.get("name",'Undefined')
#     age=request.POST.get("age",1)
#     return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")


# def index(request):
#     return render(request, "index.html")
# def postuser(request):
#     name = request.POST.get("name", "Undefined")
#     age = request.POST.get("age", 1)
#     langs = request.POST.getlist("languages", ["python"])
#
#     return HttpResponse(f"""
#                 <div>Name: {name}  Age: {age}<div>
#                 <div>Languages: {langs}</div>
#             """)



# def index(request):
#     userform = UserForm()
#     return render(request, "index.html", {"form": userform})



# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
#     else:
#         userform = UserForm()
#         return render(request, "index.html", {"form": userform})




# def index(request):
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             return HttpResponse(f'<h2>Hello {name}</h2>')
#         else:
#             return HttpResponse(f'<h2>Invalid data</h2>')
#     else:
#         userform = UserForm()
#         return render(request, 'index.html', {'form': userform})



# def index(request):
#     userform = UserForm()
#     if request.method == 'POST':
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             name = userform.cleaned_data['name']
#             return HttpResponse(f'<h2>Hello {name}</h2>')
#     return render(request, 'index.html', {'form': userform})



# people=Person.objects.all()
# print(people.query)
# people=people.filter(name='Tom')
# print(people.query)
# people=people.filter(age=31)
# print(people.query)
# for person in people:
#     print(f'{people.id}.{person.name}-{person.age}')



# tom=Person.objects.create(name="Tom",age=23)
# print(tom.id)


# async def acreate_person():
#     person = await Person.objects.acreate(name='Tim',age=20)
#     print(person.name)
# asyncio.run(acreate_person())



# tom=Person.objects.create(name="Tom",age=23)
# tom.save()
# print(tom.id)


# people=Person.objects.bulk_create([
#     Person(name='Kate',age=20),
#     Person(name='Ann',age=30),
# ])
# for person in people:
#     print(f'{person.id}.{person.name}')


# tom=Person.objects.get(name='Bob')
# bob=Person.objects.get(age=24)
# print(tom)
# print(bob)


# bob,created = Person.objects.get_or_create(name='Bob',age=24)
# print(created)
# print(bob.name)
# print(bob.age)


# # получаем пользователя по имени Tom
# tom = Person.objects.get(name__exact="Tom")
# # получаем пользователей, у которых возраст равен 32
# people_by_age = Person.objects.filter(age__exact=32)
# # получаем пользователя по имени Tom или tom или TOM
# tom = Person.objects.get(name__iexact="Tom")


# # получаем пользователей, у которых имя равно NULL
# people_by_name = Person.objects.filter(name__exact=None)


# # получаем пользователей, у которых имя содержит букву o
# people1 = Person.objects.filter(name__contains="o")
# print(people1.query)
# # получаем пользователей, у которых имя содержит букву T или t
# people2 = Person.objects.filter(name__icontains="T")
# print(people2.query)


# # получаем пользователей, у которых возраст равен или 32, или 35, или 38,
# people = Person.objects.filter(age__in=[32, 35, 38])
# print(people.query)


# # получаем пользователей, у которых возраст меньше или равен 32
# people = Person.objects.filter(age__lte=32)
# # получаем пользователей, у которых возраст больше 40
# people1 = Person.objects.filter(age__gt=40)


# # получаем пользователей, у которых имя начинается с To
# people = Person.objects.filter(name__startswith="To")
# # получаем пользователей, у которых имя начинается с To или to
# people1 = Person.objects.filter(name__istartswith="To")


# # получаем пользователей, у которых имя заканчивается на m
# people = Person.objects.filter(name__endswith="m")
# # получаем пользователей, у которых имя заканчивается на m или M
# people1 = Person.objects.filter(name__iendswith="m")


# # получаем пользователей, у которых возраст в диапазоне от 28 до 38 включительно
# people = Person.objects.filter(age__range=(28, 38))


# # получаем пользователей, у которых имя не установлено
# people = Person.objects.filter(name__isnull=True)
# # получаем пользователей, у которых возраст установлен
# people1 = Person.objects.filter(age__isnull=False)


# # получаем пользователей, у которых имя заканчивается на am или om
# people = Person.objects.filter(name__regex=r"(am|om)$")


# # добавление начальных данных
# if Order.objects.count() == 0:
#     Order.objects.create(datetime=datetime(2021, 12, 26, 11, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 5, 12, 12, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 5, 22, 13, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 8, 19, 14, 25, 34))
# # получаем заказы, сделанные в 5-м месяце
# orders = Order.objects.filter(datetime__month=5)
# for order in orders:
#     print(order.datetime)
# # получаем заказы, сделанные после 5-го месяца
# orders = Order.objects.filter(datetime__month__gt=5)
# for order in orders:
#     print(order.datetime)


# if Order.objects.count() == 0:
#     Order.objects.create(datetime=datetime(2021, 12, 26, 11, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 5, 12, 12, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 5, 22, 13, 25, 34))
#     Order.objects.create(datetime=datetime(2022, 8, 19, 14, 25, 34))
# # получаем заказы, сделанные 22 мая
# orders = Order.objects.filter(datetime__date=date(2022, 5, 22))
# for order in orders:
#     print(order.datetime)
# # получаем заказы, сделанные после 12 часов
# orders = Order.objects.filter(datetime__time__gt=time(12, 20, 0))
# for order in orders:
#     print(order.datetime)



# people = Person.objects.filter(name="Tom") & Person.objects.filter(age=22)  ## & это and
# people = Person.objects.filter(name="Tom") | Person.objects.filter(age=22)  ## | это or
# people = Person.objects.filter(name="Tom") ^ Person.objects.filter(age=22)  ## ^ это xor-В данном случае в базе данных будет идти поиск строки, в которой истинно либо условие name="Tom", либо поле условие age=22, но не одновременно оба условия. На уровне базы данных могут формироваться различные выражения в зависимости от поддержки оператора XOR.




# people=Person.objects.order_by('name')
# for person in people:
#     print(person.name)





# people=Person.objects.order_by('name','age')
# for person in people:
#     print(person.name,person.age)



# people=Person.objects.values()
# print(people)



# people=Person.objects.values('id','name')
# print(people)



# people=Person.objects.values_list()
# print(people)


# people=Person.objects.values_list('id','name')
# print(people)


# people=Person.objects.values_list('name',flat=True)
# print(people)


# people=Person.objects.values_list('name',flat=True).distinct()  #distinct убирает дубли
# print(people)



# toms=Person.objects.filter(name='Tom')
# bobs=Person.objects.filter(name='Bob')
# people=toms.union(bobs)
# print(people.values())



# toms=Person.objects.filter(name='Tom')
# bobs=Person.objects.filter(name='Bob')
# people=toms.values('name').union(bobs)
# print(people)



# toms=Person.objects.filter(name='Tom')
# less35=Person.objects.filter(age__lt=35)
# people=toms.intersection(less35)
# print(people.values())



# toms=Person.objects.filter(name='Tom')
# less35=Person.objects.filter(age__lt=35)
# people=toms.difference(less35)
# print(people)



# latest_person=Person.objects.latest('id')
# print(f'{latest_person.name}-{latest_person.age}')



# earliest_person=Person.objects.earliest('id')
# print(f'{earliest_person.name}-{earliest_person.age}')



# first_person=Person.objects.first()
# print(f'{first_person.name}-{first_person.age}')
# last_person=Person.objects.last()
# print(f'{last_person.name}-{last_person.age}')



# first_person=Person.objects.order_by('age').first()
# print(f'{first_person.name}-{first_person.age}')


# is_present=Person.objects.filter(name='Tom').exists()
# if is_present:
#     print('в наборе есть проекты')
# else:
#     print('объекты в наборе отсутствуют')


# last_person=Person.objects.last()
# is_present=Person.objects.filter(age__lt=35).contains(last_person)
# if is_present:
#     print("объект есть в наборе")
# else:
#     print('объект отсутствует')



# number=Person.objects.count()
# print(number)



# people=Person.objects.all()
# number=len(people)
# print(number)



# avg_age=Person.objects.aggregate(Avg('age'))
# print(f'Средний возраст: {avg_age}')
# min_age=Person.objects.aggregate(Min('age'))
# print(f'Минимальный возраст: {min_age}')
# max_age=Person.objects.aggregate(Max('age'))
# print(f'Максимальный возраст : {max_age}')
# sum=Person.objects.aggregate(Sum('age'))
# print(f'Сумма : {sum}')



# people=Person.objects.raw('SELECT id,name FROM myapp_person')
# for person in people:
#     print(person.name)



# name_for_filter='Tom'
# age_for_filter=35
# people=Person.objects.raw('SELECT * FROM myapp_person WHERE name=%s OR age>%s',[name_for_filter,age_for_filter])
# print(people)


# with connection.cursor() as cursor:
#     cursor.execute("UPDATE myapp_person SET name='Tomas' WHERE name='Tom' AND age=22")
#     cursor.execute("SELECT * FROM myapp_person WHERE name='Tomas'")
#     row=cursor.fetchone()
#     print(row)


# old_name='Tomas'
# new_name='Tom'
# with connection.cursor() as cursor:
#     cursor.execute("UPDATE myapp_person SET name=%s WHERE name=%s",[new_name,old_name])
#     cursor.execute("SELECT * FROM myapp_person WHERE name='Tom'")
#     rows=cursor.fetchall()
#     for row in rows:
#         print(row)



def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
def create(request):
    if request.method == 'POST':
        person = Person()
        person.name=request.POST.get('name')
        person.age=request.POST.get('age')
        person.save()
    return HttpResponseRedirect('/')
def edit(request,id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name=request.POST.get('name')
            person.age=request.POST.get('age')
            person.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
def delete(request,id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")