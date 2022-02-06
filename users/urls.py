from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('employeeList', views.employeeList, name='employeeList'),
    path('processLogin', views.processLogin, name='processLogin'),
    path('logout', views.processLogout, name='processLogout'),
    path('addUser', views.addUser, name='addUser'), 
    path('proccessAddUser', views.processAddUser, name='processAddUser'),
    path('<int:profile_id>/userDetails/', views.userDetails, name = 'userDetails'),
    path('<int:profile_id>/deleteUser/', views.deleteUser, name = 'deleteUser'),
    path('<int:profile_id>/editUser/', views.editUser, name = 'editUser'),
    path('<int:profile_id>/processEditUser/', views.processEditUser, name = 'processEditUser'),
    path('searchForUser', views.searchForUser, name='searchForUser'),


    path('inventorySummary', views.inventorySummary, name='inventorySummary'),
    path('searchForProduct', views.searchForProduct, name='searchForProduct'),
    path('<int:product_id>/productDetails/', views.productDetails, name = 'productDetails'),
    path('addProduct', views.addProduct, name='addProduct'), 
    path('proccessAddProduct', views.processAddProduct, name='processAddProduct'),
    path('<int:product_id>/deleteProduct/', views.deleteProduct, name = 'deleteProduct'),
    path('<int:product_id>/editProduct/', views.editProduct, name = 'editProduct'),    
    path('<int:product_id>/processEditProduct/', views.processEditProduct, name = 'processEditProduct'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)