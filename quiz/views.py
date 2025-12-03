from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event, UserProfile
from .forms import QuizSubmissionForm
from django.db.models import Count, Avg
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import QuizForm, EventForm, AddUserForm
from django.http import JsonResponse
from django.db import transaction
import json
from django.contrib.auth.models import User
from .decorators import access_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

# Registration
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            profile = user.userprofile
            if profile.access_home:
                return redirect("home")
            if profile.access_quiz:
                return redirect("quiz_list")
            if profile.access_event:
                return redirect("event_list")
            if not (profile.access_home or profile.access_quiz or profile.access_event):
                logout(request)
                messages.error(request, "Your account does not have access to any pages. Contact admin.")
                return HttpResponse("Access Denied Because You Didn't Check Any Pages", status=403)
            messages.success(request, f"Welcome back, {user.username}!")
            
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

# Logout
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect("login")


# Home page view
@access_required("access_home")
def home(request):
    quizzes = Quiz.objects.all()[:3]
    events = Event.objects.all()[:3]
    context = {"quizzes": quizzes, "events": events}
    return render(request, "home.html", context)

# QUIZ LIST
@access_required("access_quiz")
def quiz_list(request):
    quizzes = Quiz.objects.all().order_by("-created_at")
    return render(request, "quizzes/quiz_list.html", {"quizzes": quizzes})

# QUIZ ATTEMPT PAGE
@staff_member_required
@login_required
def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related(
            Prefetch("questions", queryset=Question.objects.prefetch_related("answers"))
        ),
        id=quiz_id
    )

    questions = quiz.questions.all()
    form = QuizSubmissionForm()

    if request.method == "POST":
        form = QuizSubmissionForm(request.POST)
        if form.is_valid():

            user_name = form.cleaned_data["user_name"]

            # Create submission with the correct user
            submission = UserSubmission.objects.create(
                quiz=quiz,
                user=request.user,    
                user_name=request.user.username,       # Keep for display if needed
                score=0,
            )

            total_score = 0

            for q in questions:
                field_name = f"question_{q.id}"
                selected_answer = request.POST.get(field_name)

                if q.question_type == "MCQ":
                    ans_obj = Answer.objects.filter(id=selected_answer).first()
                    is_correct = ans_obj.is_correct if ans_obj else False
                    answer_text = ans_obj.text if ans_obj else "No answer"
                else:
                    user_text = selected_answer or ""
                    correct_answer = Answer.objects.filter(question=q, is_correct=True).first()
                    is_correct = (user_text.strip().lower() == correct_answer.text.lower())
                    answer_text = user_text

                UserAnswer.objects.create(
                    submission=submission,
                    question=q,
                    answer=answer_text,
                    is_correct=is_correct
                )

                if is_correct:
                    total_score += 1

            submission.score = total_score
            submission.save()

            return redirect("quiz_result", submission_id=submission.id)

    return render(request, "quizzes/quiz_attempt.html", {
        "quiz": quiz,
        "questions": questions,
        "form": form
    })


# QUIZ RESULT
@login_required
@staff_member_required
def quiz_result(request, submission_id):
    submission = get_object_or_404(
        UserSubmission.objects.select_related("quiz"),
        id=submission_id
    )

    return render(request, "quizzes/quiz_result.html", {
        "submission": submission,
    })

# QUIZ HISTORY
from django.db.models import Count, Avg

@login_required
@staff_member_required
def quiz_history(request):
    submissions = (
        UserSubmission.objects
        .filter(user=request.user)
        .select_related("quiz")
        .order_by("-submitted_at")
    )

    quiz_stats = (
        Quiz.objects
        .filter(submissions__user=request.user)
        .annotate(
            attempts_count=Count("submissions"),
            average_score=Avg("submissions__score"),
            total_questions=Count("questions", distinct=True)
        )
    )

    # Calculate avg_percentage per quiz
    stats_map = {}
    for q in quiz_stats:
        avg_percentage = 0
        if q.total_questions > 0 and q.average_score is not None:
            avg_percentage = (q.average_score / q.total_questions) * 100
        q.avg_percentage = avg_percentage
        stats_map[q.id] = q

    return render(request, "quizzes/quiz_history.html", {
        "submissions": submissions,
        "stats_map": stats_map,
    })

    
# EVENTS LIST
@access_required("access_event")
def event_list(request):
    events = Event.objects.all().order_by("date")
    return render(request, "events/event_list.html", {"events": events})

# EVENT DETAIL
@login_required
@staff_member_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, "events/event_detail.html", {"event": event})

@login_required
@staff_member_required
def quiz_dashboard(request):
    # Fetch quizzes created by this user
    quizzes = Quiz.objects.filter(created_by=request.user)
    
    # Fetch events created by this user
    events = Event.objects.filter(created_by=request.user).order_by("-date")

    context = {
        "quizzes": quizzes,
        "events": events,
    }
    return render(request, "quizzes/dashboard.html", context)


@login_required
@staff_member_required
def create_quiz(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
        except:
            return JsonResponse({"ok": False, "error": "Invalid JSON"}, status=400)

        title = data.get("title", "").strip()
        description = data.get("description", "").strip()
        questions = data.get("questions", [])

        errors = []

        if not title:
            errors.append("Quiz title is required.")
        if len(questions) == 0:
            errors.append("You must add at least one question.")

        for i, q in enumerate(questions, start=1):
            if not q.get("text", "").strip():
                errors.append(f"Question {i} text is required.")

            ans = q.get("answers", [])
            if len(ans) < 2:
                errors.append(f"Question {i} must have at least 2 answers.")

            correct_count = sum(a.get("is_correct") for a in ans)
            if correct_count != 1:
                errors.append(f"Question {i} must have exactly 1 correct answer.")

        if errors:
            return JsonResponse({"ok": False, "errors": errors}, status=400)

        # Save quiz + questions + answers
        with transaction.atomic():
            quiz = Quiz.objects.create(
                title=title,
                description=description,
                created_by=request.user,
            )

            for q in questions:
                question = Question.objects.create(
                    quiz=quiz,
                    text=q["text"],
                    question_type="MCQ"
                )
                for a in q["answers"]:
                    Answer.objects.create(
                        question=question,
                        text=a["text"],
                        is_correct=a["is_correct"]
                    )

        return JsonResponse({"ok": True, "redirect": "/dashboard/"})

    return render(request, "quizzes/create_quiz.html")

@login_required
@staff_member_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user  # assign logged-in user
            event.save()
            messages.success(request, "Event created successfully.")
            return redirect("dashboard")
    else:
        form = EventForm()
    return render(request, "events/create_event.html", {"form": form})

def user_list(request):
    users = User.objects.all()
    return render(request, "users/user_list.html", {"users": users})

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():

            # CREATE USER
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            # CREATE USER PROFILE
            profile = UserProfile.objects.create(
                user=user,
                access_home=form.cleaned_data["access_home"],
                access_event=form.cleaned_data["access_event"],
                access_quiz=form.cleaned_data["access_quiz"],
            )
            
            messages.success(request, "User added successfully.")
            return redirect("user_list")
    else:
        form = AddUserForm()
    
    return render(request, "users/add_user.html", {"form": form})

