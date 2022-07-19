from django.urls import path,include
from .views import*


urlpatterns=[
    path('register/', RegisterView.as_view(),name='register'),
    # path('login/', RegisterView.as_view(),name='login'),
    # path('logout/', RegisterView.as_view(),name='logout'),
]