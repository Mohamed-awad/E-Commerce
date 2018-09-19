from django.conf.urls import url
from django.contrib.auth import views as auth_view
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as core_view

app_name = 'accounts'

urlpatterns = [
  url(r'^login/$', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  url(r'^logout/$', auth_view.LogoutView.as_view(), name='logout'),
  url(r'^signup/$', core_view.signup, name='signup'),
  url(r'^$', core_view.UserList.as_view(), name='list_user_api'),
  url(r'^(?P<pk>[0-9]+)/$', core_view.UserDetail.as_view(), name='detail_user_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
