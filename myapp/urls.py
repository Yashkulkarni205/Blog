from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'myapp/login.html'),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'myapp/logout.html'),name = 'logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='myapp/password_reset.html'),name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view( template_name='myapp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'), name='password_reset_complete'),
    path('my-articles/',views.my_articles,name='my-articles'),
    path('all-articles/',views.all_articles,name='all-articles'),
    path('create-article/',views.create_article,name='create-article'),
    path('update-article/<int:pk>/', views.update_article, name='update-article'),
    path('detail-article/<int:pk>/', views.DetailArticle.as_view(), name='detail-article'),
    path('delete-article/<int:pk>/', views.DeleteArticle.as_view(), name='delete-article'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)