from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('companies/',
         csrf_exempt(views.CompanyList.as_view()),
         name='company-list'),
    path('companies/<int:pk>/',
         csrf_exempt(views.CompanyDetail.as_view()),
         name='company-detail'),
])