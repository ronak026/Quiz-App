from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Auth section
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    
    # Quiz section
    path("quizzes/", views.quiz_list, name="quiz_list"),
    path("quiz/<int:quiz_id>/", views.quiz_attempt, name="quiz_attempt"),
    path("result/<int:submission_id>/", views.quiz_result, name="quiz_result"),
    path("quizzes/create-quiz/", views.create_quiz, name="create_quiz"),
    path("quizzes/create-event/", views.create_event, name="create_event"),

    # User quiz history and dashboard
    path("history/", views.quiz_history, name="quiz_history"),
    path("dashboard/", views.quiz_dashboard, name="dashboard"),

    # Event section
    path("events/", views.event_list, name="event_list"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
]
