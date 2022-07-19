from django.urls import path,include
from .views import*

urlpatterns=[
    path('localite/', PostList.as_view(),name='list'),
    path('localited/<int:pk>/', PostDetail.as_view(),name='detail'),
    path('affectation/', AffecterList.as_view(),name='affecter'),
    path('detailaff/<int:pk>/', AffecterDetail.as_view(),name='daffecter'),
    path('conjoint/', ConjointList.as_view(),name='affecter'),
    path('dconjoint/<int:pk>/', ConjointDetail.as_view(),name='daffecter'),
    path('chefmenage/', ChefMenageList.as_view(),name='affecter'),
    path('recensement/', RecensementView.as_view(),name='affecter'),
    path('dchefmenage/<int:pk>/', ChefMenageDetail.as_view(),name='daffecter'),
    path('enfant/', EnfantList.as_view(),name='list'),
    path('denfant/<int:pk>/', EnfantDetail.as_view(),name='detail'),
    path('commodite/', CommoditeList.as_view(),name='list'),
    path('dcommodite/<int:pk>/', CommoditeDetail.as_view(),name='detail'),
    path('migrant/', MigrantList.as_view(),name='list'),
    path('dmigrant/<int:pk>/', MigrantDetail.as_view(),name='detail'),
    path('emigration/', EmigrationList.as_view(),name='list'),
    path('demigration/<int:pk>/', EmigrationDetail.as_view(),name='detail'),
    path('deces/', DecesList.as_view(),name='list'),
    path('ddeces/<int:pk>/', DecesDetail.as_view(),name='detail'),
    path('equipement/', EquipementList.as_view(),name='list'),
    path('dequipement/<int:pk>/', EquipementDetail.as_view(),name='detail'),
]