from django.contrib import admin
from django.urls import path
from my_app.views import ClientView, CompanyView, OffertView, BidView

urlpatterns = [
    path('admin/', admin.site.urls),
    ## views API
    path("client/<int:pk>", ClientView.as_view()),
    path("client/", ClientView.as_view()),

    path("company/<int:pk>", CompanyView.as_view()),
    path("company/", CompanyView.as_view()),

    path("offert/<int:pk>", OffertView.as_view()),
    path("offert/", OffertView.as_view()),

    path("bid/<int:pk>", BidView.as_view()),
    path("bid/", BidView.as_view()),
]