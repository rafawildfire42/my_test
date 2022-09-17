from django.contrib import admin
from django.urls import path
from my_app.views import ClientView, CompanyView

urlpatterns = [
    path('admin/', admin.site.urls),
    ## views API
    path("client/<int:pk>", ClientView.as_view()),
    path("client/", ClientView.as_view()),

    path("company/<int:pk>", CompanyView.as_view()),
    path("company/", CompanyView.as_view()),
]