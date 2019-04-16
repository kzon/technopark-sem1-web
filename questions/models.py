from questions import model_managers
from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=50)


class UserProfile(models.Model):
    objects = model_managers.UserProfileManager()

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatars', null=True)

    def __str__(self):
        return self.user.username


class Vote(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    objects = model_managers.QuestionManager()

    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    votes = models.ManyToManyField(Vote)
    votes_count = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    objects = model_managers.AnswerManager()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    votes = models.ManyToManyField(Vote)
    votes_count = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
