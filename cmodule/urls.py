from django.urls import path

from .views import CMappingAPI,ServiceAPI

urlpatterns = [
    path("template/" , CMappingAPI.get_map ),
    path("serviceuser/" , ServiceAPI.as_view({'post' : 'parse'}) )

]
