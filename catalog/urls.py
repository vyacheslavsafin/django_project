from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import home, contacts, categories, products

app_name = CatalogConfig.name

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('contacts/', contacts, name='contacts'),
                  path('categories/', categories, name='categories'),
                  path('<int:pk>/catalog/', products, name='products'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
