from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'send_message/', views.send_message, name='send_message'),
	url(r'register/', views.register, name='register'),
	url(r'login/', views.login, name='login'),
	url(r'logout/', views.logout_view, name='logout'),
	url(r'get_messages/', views.get_messages, name='get_messages'),
	url(r'get_python_output/', views.get_python_output, name='get_python_output'),
	url(r'user/(?P<username>\w{0,50})', views.user, name='user'),
	url(r'am_i_watched/', views.am_i_watched, name='am_i_watched'),
	url(r'get_user_code/', views.get_user_code, name='get_user_code'),
	url(r'get_problem/', views.get_problem, name='get_problem')
]