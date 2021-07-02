from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home page'),
    path('find-blogs',views.post,name='Get data'),

]
