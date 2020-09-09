from django.urls import path
from .views import feedback

urlpatterns = [
    # path('', home, name='home'),
    # path('features/', features, name='features'),
    # path('download/',download_video, name='download'),
    path('<str:thread>',feedback, name='feedback'),
]
