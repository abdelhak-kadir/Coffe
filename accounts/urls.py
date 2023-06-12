from django.urls import path
from . import views
urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('profile', views.profile, name="profile"),
    # pro_id : id du product qui aura s'affecher
    path('product_fav/<int:pro_id>', views.product_fav, name="product_fav"),
    path('show_product_fav', views.show_product_fav, name="show_product_fav"),

]
