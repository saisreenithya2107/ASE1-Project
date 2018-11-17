from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="accounts/logged_out.html"), name='logout'),
]
