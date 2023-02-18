
from django.urls import path,include
from sstech import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('webdevelopment',views.webDevelopment,name='web'),
    path('mobiledevelopment',views.mobileDevelopment,name='mobile'),
    path('digitalmarketing',views.digitalMarketing,name='dm'),
    path('usstaffing',views.usStaffing,name='us'),
    path('domesticstaffing',views.domesticStaffing,name='ds'),
    path('careers',views.careers,name='careers'),
    path('contact/',views.contact,name='contact')
]
