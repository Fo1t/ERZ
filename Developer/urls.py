from django.urls import path
from Developer.views import MainPage, DeveloperPage, ObjectPage, ApargPage


urlpatterns = [
    path('developer/<int:developer_id>', DeveloperPage, name='DeveloperPage'),
    path('developer/object/<int:general_id>', ObjectPage, name='ObjectPage'),
    path('developer/object/apartment/<int:object_id>', ApargPage, name='ApargPage'),
    path('', MainPage, name='MainPage'),
]