
from django.urls import path
from rest_framework import routers
from .views import StuView,MarkView,ReportView
from . import views

router =routers.DefaultRouter()



urlpatterns = [
    path('student/', views.StuView.as_view(actions={'get': 'list'}), name='student'),
    path('student/add/', views.StuView.as_view(actions={'post': 'create'}), name='student'),
    path('student/<id>/', views.StuView.as_view(actions={'get': 'retrieve'}), name='student'),
    path('student/<id>/add-mark/', views.MarkView.as_view(actions={'post': 'create'}), name='marks'),
    path('student/<id>/mark/', views.MarkView.as_view(actions={'get': 'retrieve'}), name='marks'),
    path('students/results/', StuView.as_view() ,name='StuView'),
]+router.urls