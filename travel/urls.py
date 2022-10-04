import patterns as patterns
from django.contrib import admin
from django.urls import path, include

import routes
from routes.views import home, find_routes, add_route, save_route, RouteListView, RouteDetailView, RouteDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('trains/', include(('trains.urls', 'trains'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('', home, name='home'),
    path('find_routes/', find_routes, name='find_routes'),
    path('add_route/', add_route, name='add_route'),
    path('save_route/', save_route, name='save_route'),
    path('list/', RouteListView.as_view(), name='list'),
    path("select2/", include("django_select2.urls")),
    path('detail/<int:pk>/', RouteDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', RouteDeleteView.as_view(), name='delete'),
]

