from django.urls import path
from . import views


app_name = "home"
urlpatterns = [
    # path("", views.HomeView.as_view(), name="home"),
    # path("two/<int:id>/<str:name>/", views.Two.as_view(), name="two"),
    # path("create/", views.CarCreateView.as_view(), name="car_create"),
    # path("<slug:my_slug>/", views.CarDetail.as_view(), name="car_detail"),
    # path("login/", views.UserLogin.as_view(), name="user_login"),
    # path("logout/", views.UserLogout.as_view(), name="user_logout"),
    # path("delete/<int:pk>/", views.CarDelete.as_view(), name="car_delete"),
    # path("update/<int:pk>/", views.CarUpdate.as_view(), name="car_update"),
    # path("<int:year>/<int:month>/", views.MonthCar.as_view()),
    path("", views.CarListView.as_view(), name="home"),
    path("<int:pk>/", views.SingleCar.as_view()),
    
    
]