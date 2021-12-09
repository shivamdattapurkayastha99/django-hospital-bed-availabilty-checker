
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.home,name='homepage'),
    path('hospital/<int:pk>', views.HospitalDetailView.as_view(),name='hospital_detail'),
]