from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('cat/<str:name>',views.products),
    path('login/',views.Login_user),
    path('logout/',views.logout_user),
    path('product-detail/<int:id>',views.product_detail),
    path('cart/<int:id>',views.add_cart,name="cart"),
    path('cart/',views.cart)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
