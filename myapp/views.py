from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseForbidden, \
    HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.template.response import TemplateResponse

from .forms import UserForm


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



def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


