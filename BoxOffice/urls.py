
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.urls import path, include
from home.views import ShowIndex, RegisterView, LoginView,SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('', ShowIndex.as_view()),
    path('search/', SearchView.as_view(),name='search'),
    path('movies/', include('movie.urls',namespace='movie')),
    path('booking/', include('booking.urls',namespace='booking')),
    path('theatres/', include('theatre.urls',namespace='theatre')),
    path(r'register',RegisterView.as_view(),name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
