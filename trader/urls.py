from django.urls import path
from . import views

urlpatterns = [
   # path('register/',views.register, name="register"),
    path('', views.about, name ="aboutpage"),
    path('myshopgrid', views.myshop, name ="myshopgrid"),
    path('myshop', views.myshoplist, name ="myshoplist"),
    path('shop', views.shop, name ="shopgrid"),
    path('shoplist', views.shoplist, name ="shoplist"),
    path('addproductpage', views.addproduct, name ="addproductpage"),
    path('addproduct', views.addproduct, name ="addproduct"),
    path('delete/<str:x_id>', views.delete, name ="delete"),
    path('productpage/<str:x_ownerName>', views.productpage, name ="productpage"),
    path('product_detail/<str:pro_name>', views.product_detail, name ="product_detail"),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('myfavorite', views.myfavorite, name ="myfavorite"),
    path('addmyfavorite/<str:x_id>', views.addmyfavorite, name ="addmyfavorite"),
    path('deletefavorite/<str:x_id>', views.deletefavorite, name ="deletefavorite"),
    path('buy/<str:x_id>', views.buy, name ="buy"),
    path('mydeal', views.mydeal, name ="mydeal"),
    path('canceldeal/<str:x_id>', views.canceldeal, name ="canceldeal"),
    path('confirmdeal/<str:x_id>', views.confirmdeal, name ="confirmdeal"),
    path('previoustrades/<str:x_id>', views.previoustrades, name ="previoustrades"),
    path('myprevioustrades', views.myprevioustrades, name ="myprevioustrades"),
    path('updatepic/<str:x_id>', views.updatepic, name ="updatepic"),
    ]

