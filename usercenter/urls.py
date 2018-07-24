from django.conf.urls import url
from .views import usercenter_register
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    url(r'^register$', usercenter_register, name="usercenter_register"),
    url(r'^logout', logout_then_login, name="logout_then_login"),
]
