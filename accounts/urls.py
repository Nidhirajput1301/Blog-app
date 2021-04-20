from . import views
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.signup_view, name="signup"),
    url('login/', views.login_view, name="login"),
]
