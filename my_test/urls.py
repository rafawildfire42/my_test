from django.contrib import admin
from django.urls import path
from my_app.views import ClientView, CompanyView, OffertView, BidView
from my_site.views import clients, clients_post, company, company_post, offert, offert_post, bid, bid_post

urlpatterns = [
    path('admin/', admin.site.urls),
    ## views API
    path("api/client/<int:pk>", ClientView.as_view()),
    path("api/client/", ClientView.as_view()),

    path("api/company/<int:pk>", CompanyView.as_view()),
    path("api/company/", CompanyView.as_view()),

    path("api/offert/<int:pk>", OffertView.as_view()),
    path("api/offert/", OffertView.as_view()),

    path("api/bid/<int:pk>", BidView.as_view()),
    path("api/bid/", BidView.as_view()),

    ##views frontend
    path("client/", clients),
    path("client/post/", clients_post),

    path("company/", company),
    path("company/post/", company_post),

    path("offert/", offert),
    path("offert/post/", offert_post),

    path("bid/", bid),
    path("bid/post/", bid_post)
]
