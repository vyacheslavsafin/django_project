from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from django.urls import path
from catalog import views

from catalog.views import HomeView, ContactsView, categories, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomeView.as_view(), name='home'),
                  path('contacts/', ContactsView.as_view(), name='contacts'),
                  path('categories/', categories, name='categories'),
                  path('catalog/<int:pk>/', ProductListView.as_view(), name='products'),
                  path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
                  path('product_view/<int:pk>', cache_page(60)(views.ProductDetailView.as_view()), name='product_view'),
                  path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
                  path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
