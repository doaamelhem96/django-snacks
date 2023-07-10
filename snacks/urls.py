from django.urls import path
from .views import Homeview,Aboutview
urlpatterns = [
    path('', Homeview.as_view(),name='home'),
    path('about', Aboutview.as_view(),name='about'),

    

]