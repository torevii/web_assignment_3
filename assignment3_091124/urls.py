from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь к админ-панели
    path('', views.PostListView.as_view(), name='post_list'),  # Список постов
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # Отдельный пост
    path('add/', views.add_post, name='add_post'),  # Страница добавления поста
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
