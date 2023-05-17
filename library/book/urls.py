from django.urls import path
from . import views
from library.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns =[
    path('', views.home,name='home'),
    #path('library', views.Library,name='library'),
    path('upload',views.Upload,name='upload'),
    path('update/<int:book_id>', views.update_book,name='update'),
    path('delete/<int:book_id>', views.delete_book,name='delete'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)