from django.urls import include, path
from rest_framework import routers
from people import views


router = routers.DefaultRouter()
router.register('people', views.PersonView, 'people')

#App
urlpatterns = [
    #nombre de la ruta de entrada api
    path('', include(router.urls))
]
