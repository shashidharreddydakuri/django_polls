from django.urls import path, include

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('searchlens/', views.searchlens_page, name='searchlens_page'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path("", views.listing, name="listing"),
    # path("view_blog/<int:blog_id>/", views.view_blog, name="view_blog"),
    
]