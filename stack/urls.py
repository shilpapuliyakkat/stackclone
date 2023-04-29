from django.urls import path
from stack import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("register",views.SignupView.as_view(),name="register"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("questions/<int:id>/answers/add",views.AddAnswerView.as_view(),name="add-answer"),
    path("answers/<int:id>/upvote/add",views.UpVoteView.as_view(),name="upvote"),
    path("profiles/add",views.UserProfileCreateView.as_view(),name="profile-add"),
    path("profiles/details",views.ProfileDetailView.as_view(),name="profile-detail"),
    path("profiles/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-edit"),
    path("questions/<int:pk>/remove",views.QuestionDeleteView.as_view(),name="question-delete"),
    path("answers/<int:id>/upvote/remove",views.UpVoteRemove.as_view(),name="downvote"),
    path("logout",views.SignoutView.as_view(),name="signout")



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)