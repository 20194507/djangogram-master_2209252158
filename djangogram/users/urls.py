from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
]



# from django.urls import path

# from djangogram.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

# app_name = "users"
# urlpatterns = [
#     path("~redirect/", view=user_redirect_view, name="redirect"),
#     path("~update/", view=user_update_view, name="update"),
#     path("<str:username>/", view=user_detail_view, name="detail"),
# ]


