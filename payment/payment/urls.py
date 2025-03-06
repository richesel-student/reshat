# from django.contrib import admin
# from django.urls import path, include
from django.http import HttpResponse
# # def home(request):
# #     return HttpResponse("Hello, world!")
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app_payment.urls')),  # всё из app_payment
#     # path('', home),
# ]
# payment/payment/urls.py
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app_payment.urls')),
# ]
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app_payment.urls')),
]