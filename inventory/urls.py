from django.urls import path
from .import views

# for media folder
from django.conf import settings
from django.conf.urls.static import static


app_name = 'inventory'

urlpatterns = [
    path('',views.inventory_display,name="display"), 
    path('update/<slug:slug>/',views.article_update,name="article_update"),
    path('delete/<slug:slug>/',views.article_delete_confirm,name="delete_confirm"),
    path('delete/confirm/<slug:slug>/',views.article_delete,name="delete"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)