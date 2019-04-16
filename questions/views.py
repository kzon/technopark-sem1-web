from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from questions import models
from django.contrib.auth.models import User
from django.http import Http404

is_authorized = False

authorized_user_id = 3

paginator_objects_per_page = 4
paginator_page_number_request_param = 'page'


def paginate(objects, request):
    paginator = Paginator(objects, paginator_objects_per_page)
    page = request.GET.get(paginator_page_number_request_param)
    return paginator.get_page(page)


def prepare_template_context(context=None):
    if context is None:
        context = {}
    context['is_authorized'] = is_authorized
    user = User.objects.get(pk=authorized_user_id)
    context['authorized_user'] = models.UserProfile.objects.get(user=user)
    context['tags'] = models.Tag.objects.all()
    context['best_members'] = models.UserProfile.objects.best()
    return context


def index(request):
    questions_paginated = paginate(models.Question.objects.new(), request)
    return render(request, 'questions/index.html', prepare_template_context({'questions': questions_paginated}))


def hot(request):
    hot_questions = models.Question.objects.hot()
    hot_questions_paginated = paginate(hot_questions, request)
    return render(request, 'questions/hot.html', prepare_template_context({'questions': hot_questions_paginated}))


def question(request, question_id):
    try:
        single_question = models.Question.objects.get(pk=question_id)
    except models.Question.DoesNotExist:
        raise Http404()
    answers = models.Answer.objects.for_question(single_question)
    return render(request, 'questions/question.html',
                  prepare_template_context({'question': single_question, 'answers': answers}))


def ask(request):
    return render(request, 'questions/ask.html', prepare_template_context({'is_ask_page': True}))


def tag(request, tag):
    questions = models.Question.objects.by_tag(tag)
    questions_paginated = paginate(questions, request)
    return render(request, 'questions/tag.html',
                  prepare_template_context({'tag': tag, 'questions': questions_paginated}))


def profile(request):
    return render(request, 'questions/profile.html', prepare_template_context())


def login(request):
    global is_authorized
    is_authorized = True
    return render(request, 'questions/login.html', prepare_template_context())


def signup(request):
    return render(request, 'questions/signup.html', prepare_template_context())


def logout(request):
    global is_authorized
    is_authorized = False
    return redirect('index')
