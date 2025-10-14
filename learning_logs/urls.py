""" Define URL patterns for the learnings_logs app """

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name= 'new_topic'),
]
