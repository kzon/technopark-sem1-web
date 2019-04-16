from django.db import models


class UserProfileManager(models.Manager):
    def best(self):
        return self.order_by('-rating')[:5]


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-created_date')

    def hot(self):
        return self.order_by('-votes_count')

    def by_tag(self, tag):
        return self.filter(tags__name__exact=tag)


class AnswerManager(models.Manager):
    def for_question(self, question):
        return self.order_by('-is_correct').filter(question=question)
