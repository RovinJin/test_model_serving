#urls 파일 생성 

from django.urls import path
from . import views

urlpatterns = [
    path('/',views.spacing_view, name='spacing_view'),
    path('/check_spacing',views.check_spacing, name='check_spacing'),
]
