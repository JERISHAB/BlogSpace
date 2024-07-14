from django.urls import path
from .import views

# for media folder
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articles'

urlpatterns = [
    path('',views.article_list,name="list"), 
    path('create/',views.article_create,name="create"),
    path('<slug:slug>/',views.article_details,name="details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
