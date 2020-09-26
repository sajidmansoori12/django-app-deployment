from django.urls import path
from basic_app import views

#The below variable is used for template tagging
app_name = "basic_app" #Django will automatically look for this name when we use in html file for template tagging

urlpatterns=[
    path('relative',views.relative,name='relative'),
    path('other',views.other,name='other')
]