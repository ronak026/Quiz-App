from django.contrib import admin
from .models import Quiz, Question, Answer, UserSubmission, UserAnswer, Event

# INLINE CLASSES
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2
    fields = ("text", "is_correct")
    show_change_link = True

# QUESTION INLINE
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ("text", "question_type")
    show_change_link = True

# QUIZ ADMIN
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    inlines = [QuestionInline]

    fieldsets = (
        ("Quiz Information", {
            "fields": ("title", "description"),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at")

# QUESTION ADMIN
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "question_type", "created_at")
    list_filter = ("quiz", "question_type", "created_at")
    search_fields = ("text",)
    ordering = ("quiz",)
    inlines = [AnswerInline]

    fieldsets = (
        ("Question Details", {
            "fields": ("quiz", "text", "question_type"),
        }),
        ("Timestamps", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at",)

# ANSWER ADMIN
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("text", "question", "is_correct")
    list_filter = ("is_correct", "question__quiz")
    search_fields = ("text",)
    ordering = ("question",)
    
# USER SUBMISSION ADMIN
@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ("user_name", "quiz", "score", "submitted_at")
    list_filter = ("quiz", "submitted_at")
    search_fields = ("user_name",)
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "score")

    fieldsets = (
        ("Submission Info", {
            "fields": ("user_name", "quiz", "score"),
        }),
        ("Timestamp", {
            "fields": ("submitted_at",),
            "classes": ("collapse",),
        }),
    )
    
# USER ANSWER ADMIN
@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("submission", "question", "is_correct")
    list_filter = ("is_correct", "question__quiz")
    search_fields = ("submission__user_name",)
    ordering = ("submission",)

# EVENTS ADMIN
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location")
    list_filter = ("date",)
    search_fields = ("title", "location")
    ordering = ("date",)

    fieldsets = (
        ("Event Details", {
            "fields": ("title","date", "location", "description"),
        }),
    )
