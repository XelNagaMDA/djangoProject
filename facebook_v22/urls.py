"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from facebook_v22.views import register_user, all_users_view, users_restered_today, regisration_one_day_sooner, \
    rename_user, make_post, list_posts, delete_user

urlpatterns = [
    path('register/', register_user),
    path('list/', all_users_view),
    path('list/today/', users_restered_today),
    path('change-date/lower/', regisration_one_day_sooner),
    path('rename-user/', rename_user),
    path('post/', make_post),
    path('list-posts/', list_posts),
    path('delete-user/', delete_user),

]