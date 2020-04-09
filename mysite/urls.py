
from django.contrib import admin
from django.urls import path
from .

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze',views.analyze,name='analyze'),
    path('contact',views.contact,name='contact'),

]