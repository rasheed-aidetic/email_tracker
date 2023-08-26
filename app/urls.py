from django.urls import path
from . import views

urlpatterns = [
    path('create-email/', views.CreateEmailData.as_view(), name="create"),
    path('send-email/', views.SendEmail.as_view(), name="sent"),
    path('v1/image/<str:uuid>/image.jpg', views.TrackOpenedMail.as_view(), name="track"),
]