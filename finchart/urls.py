from django.urls import path

from .views import IndexView,CompanyView,FstatementView

app_name = 'finchart'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('company/<int:pk>', CompanyView.as_view(), name='company'),
    path('fstatement_detail/<int:pk>', FstatementView.as_view(), name='fstatement'), 
]