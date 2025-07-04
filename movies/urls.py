from django.urls import path

from .views import RecommendationsView, MoviesListView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView, ProtectedView

urlpatterns=[
    path("movies/", MoviesListView.as_view(), name="movie_list"),
    path("recommend/<int:movie_id>/", RecommendationsView.as_view(), name="recommend"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    
]

