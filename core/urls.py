from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView

from myapp  import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



# urlpatterns = [
#     path('',views.index),
#     path('about',views.about),
#     path('contact',views.contact)
# ]



# urlpatterns = [
#     path('',views.index),
#     path(r'^about',views.about),
#     path(r'^contact',views.contact)
# ]



# urlpatterns = [
#     re_path(r'^about/contact/',views.contact),
#     re_path(r'^about/',views.about),
#     path('',views.index),
# ]


# urlpatterns = [
#     path('',views.index),
#     path('about',views.about,kwargs={'name':'Tom','age':38}),
# ]


# urlpatterns = [
#     path('index', views.index),
# ]


# urlpatterns = [
#     path('',views.index,)
# ]


# urlpatterns = [
#     path("", views.index),
#     path("user", views.user),
#     path("user/<name>", views.user),
#     path("user/<name>/<int:age>", views.user),
# ]


# urlpatterns = [
#     path("", views.index),
#     re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
#     re_path(r"^user/(?P<name>\D+)", views.user),
#     re_path(r"^user", views.user),
# ]


# product_patterns = [
#     path("", views.products),
#     path("new", views.new),
#     path("top", views.top),
# ]
# urlpatterns = [
#     path("", views.index),
#     path("products/", include(product_patterns)),
# ]


# product_patterns = [
#     path("", views.products),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]
# urlpatterns = [
#     path("", views.index),
#     path("products/<int:id>/", include(product_patterns)),
# ]



# urlpatterns = [
#     path("", views.index),
#     path("user/", views.user)
# ]



# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
#     path("details/", views.details),
# ]



# urlpatterns = [
#     path("index/<int:id>", views.index),
#     path("access/<int:age>", views.access),
# ]



# urlpatterns = [
#     path('',views.index),
# ]




# urlpatterns = [
#     path('set',views.set),
# ]



# urlpatterns = [
#     path('set',views.set),
#     path('get',views.get),
# ]


# urlpatterns = [
#     path('', views.index),
# ]



# urlpatterns = [
#     path("about/", TemplateView.as_view(template_name="about.html")),
#     path("contact/", TemplateView.as_view(template_name="contact.html")),
# ]


# urlpatterns = [
#     path("about/", TemplateView.as_view(template_name="about.html",
#         extra_context={"header": "О сайте"})),
#     path("contact/", TemplateView.as_view(template_name="contact.html")),
# ]


# urlpatterns = [
#     path("", views.index),
# ]



# urlpatterns = [
#     path("", views.index),
#     path('contacts/', views.contacts),
# ]



# urlpatterns = [
#     path("", views.index),
# ]



# urlpatterns = [
#     path("", views.index),
#     path('postuser/', views.postuser),
# ]



# urlpatterns = [
#     path("", views.index),
# ]


urlpatterns = [
]