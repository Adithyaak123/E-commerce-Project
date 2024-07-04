from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login1,name='login1'),
    path('signup',views.signup,name='signup'),
    path('login1',views.login1,name='login1'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    # path('viewproducts/<int:category_id>',views.viewproducts,name='viewproducts'),
    path('delete_category/<int:category_id>',views.delete_category,name='delete_category'),
    path('category/<int:category_id>/',views.products_by_category, name='products_by_category'),
    path('product_detail/<int:product_id>',views.product_detail,name='product_detail'),
    path('cart',views.cart,name='cart'),
    path('add_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_cart/<int:cart_item_id>',views.remove_from_cart,name='remove_from_cart'),
    path('login',views.login1,name='login1'),
   path('view_category',views.view_category,name='view_category'),
    path('viewcart',views.view_cart,name='viewcart'),
    path('index',views.index,name='index'),
    path('view_wishlist',views.view_wishlist,name='view_wishlist'),
    path('add_wishlist/<int:product_id>',views.add_wishlist,name='add_wishlist'),
    path('remove_wishlist/<int:item_id>',views.remove_wishlist,name='remove_wishlist'),
    path('checkout',views.checkout,name='checkout'),
    path('orders',views.view_orders,name='orders'),
    path('account',views.account,name='account'),
    path('editaccount',views.editaccount,name='editaccount'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_category',views.add_category,name='add_category'),
    path('edit_category/<int:category_id>',views.edit_category,name='edit_category'),
    path('view_product',views.view_product,name='view_product'),
    path('add_products',views.add_products,name='add_products'),
    path('delete_product/<int:pid>',views.delete_product,name='delete_product'),
    path('edit_product/<int:eid>',views.edit_product,name='edit_product'),

 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
