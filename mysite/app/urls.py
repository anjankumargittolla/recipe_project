from django.urls import path
from . import views
app_name = "app"
urlpatterns = [
    path('',views.home, name = "homepage"),
    path('create/',views.create, name = 'create'),
    path('data/',views.data, name = 'data'),
    path('recipe_list/',views.recipe_list, name = 'recipe_list'),
    path('<int:recipe_id>/details/',views.details, name = 'details'),
    path('<int:recipe_id>/delete/',views.delete, name = 'delete'),
    path('login/',views.login_data, name = 'login'),
    path('check/',views.check, name = 'check'),
    path('register/',views.register, name = 'register'),
    path('logout/',views.logout_data, name = 'logout'),
    path('myview/',views.my_view, name = 'myview'),
]