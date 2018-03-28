from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^login/$',views.LoginView),
    url(r'^signup/$',views.SignupView),
]
