from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index.as_view()),
    path('student/', views.StudentCreateView.as_view(), name='studentdata'),
    path('thanku/', views.Thanku.as_view(), name='datasuccess'),
]