from django.urls import path, include

urlpatterns = [
    path('competitions/', include('competitions.api') )
]
