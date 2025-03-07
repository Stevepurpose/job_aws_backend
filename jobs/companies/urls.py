from django.urls import path
from companies import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('companies/',
        views.CompanyList.as_view(),
        name='company-list'),
    path('companies/<int:pk>/',
        views.CompanyDetail.as_view(),
        name='company-detail'),      
       
])