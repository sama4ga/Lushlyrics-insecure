from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    # path("login/", views.login, name='login'),
    path("signup/", views.signup, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name='user/user_login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/user_logout.html'), name='logout'),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='user/password_change.html'), name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path("password_reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path("password_reset/complete/", auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)