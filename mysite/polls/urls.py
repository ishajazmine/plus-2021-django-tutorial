from django.urls import path

from . import views

# urlpatterns = [
#     # polls
#     path('', views.index, name='index'),
#     # ex: /polls/34/
#     path('specifics/<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/34/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/34/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# OLD 29/01/22
# app_name = 'polls'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]