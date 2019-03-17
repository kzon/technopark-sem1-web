from django.shortcuts import render

questions = [
    {
        'title': 'I cannot find emergency exit on soviet Soyuz TMA-M',
        'answers_count': 64,
        'votes_count': 103,
        'user': {'name': 'Podosinovik', 'avatar': 'man3.jpg'},
        'preview_text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                        'vero, vitae?',
        'tags': ['Soyuz', 'Soyuz TMA-M', 'emergency exit', 'soviet', 'coffee'],
        'updated_date': '2019-01-18'
    },
    {
        'title': 'How to be dominus maximus dolor sit amet?',
        'answers_count': 1,
        'votes_count': 56,
        'user': {'name': 'Max Maximus', 'avatar': 'man2.jpg'},
        'preview_text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                        'vero, vitae?',
        'tags': ['dominus', 'maximus', 'how to be', 'coffee'],
        'updated_date': '2019-01-18'
    },
    {
        'title': 'How to find magic stone?',
        'answers_count': 5,
        'votes_count': 27,
        'user': {'name': 'Andrey Rayel', 'avatar': 'man1.jpg'},
        'preview_text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                        'vero, vitae?',
        'tags': ['magic', 'stone', 'coffee'],
        'updated_date': '2019-01-18'
    },
    {
        'title': 'How to be dominus maximus dolor sit amet?',
        'answers_count': 1,
        'votes_count': 22,
        'user': {'name': 'Andrey Rayel', 'avatar': 'man2.jpg'},
        'preview_text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                        'vero, vitae?',
        'tags': ['coffee', 'dominus', 'maximus', 'how to be'],
        'updated_date': '2019-01-18'
    },
    {
        'title': 'How to be dominus maximus dolor sit amet?',
        'answers_count': 1,
        'votes_count': 10,
        'user': {'name': 'Andrey Rayel', 'avatar': 'man1.jpg'},
        'preview_text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                        'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                        'vero, vitae?',
        'tags': ['dominus', 'maximus', 'coffee', 'how to be'],
        'updated_date': '2019-01-18'
    },
]

is_authorized = True

authorized_user = {
    'name': 'Podosinovik',
    'avatar': 'man3.jpg',
}


def prepare_template_context(context):
    context['is_authorized'] = is_authorized
    context['authorized_user'] = authorized_user
    return context


def index(request):
    return render(request, 'questions/index.html', {'questions': questions})


def question(request):
    single_question = {
        'title': 'I cannot open emergency exit on soviet Soyuz TMA-M',
        'answers_count': 64,
        'votes_count': 103,
        'user': {'name': 'Podosinovik', 'avatar': 'man3.jpg'},
        'text': 'Really, I have no idea. Lorem ipsum dolor sit amet, consectetur adipisicing elit. '
                'Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora? Commodi '
                'vero, vitae? Aspernatur cupiditate mollitia provident qui similique? Eum itaque, tempora?'
                'Aspernatur blanditiis dolor doloremque eos facere nesciunt non obcaecati quasi, suscipit ut!',
        'tags': ['Soyuz', 'Soyuz TMA-M', 'emergency exit', 'soviet'],
        'created_date': '2019-01-10',
        'answers': [
            {
                'user': {'name': 'Andrey Rayel', 'avatar': 'man2.jpg'},
                'text': 'Hello! I think, you need to ask technical support center. Aspernatur cupiditate mollitia '
                        'provident qui similique? Eum itaque, tempora? Aspernatur cupiditate mollitia provident qui '
                        'similique? Eum itaque, tempora?',
                'votes_count': 6,
                'created_date': '2019-01-10'
            },
            {
                'user': {'name': 'Traktorist', 'avatar': 'man1.jpg'},
                'text': 'Provident qui similique? Eum itaque, tempora? Aspernatur cupiditate mollitia provident qui.'
                        'I think, you need to ask technical support center.',
                'votes_count': 6,
                'created_date': '2019-01-10'
            },
            {
                'user': {'name': 'Andrey Rayel', 'avatar': 'man2.jpg'},
                'text': 'Hello! I think, you need to ask technical support center. Aspernatur cupiditate mollitia '
                        'provident qui similique? Eum itaque, tempora? Aspernatur cupiditate mollitia provident qui '
                        'similique? Eum itaque, tempora?',
                'votes_count': 6,
                'created_date': '2019-01-10'
            }
        ],
    }
    return render(request, 'questions/question.html', prepare_template_context({'question': single_question}))


def ask(request):
    return render(request, 'questions/ask.html', prepare_template_context({'is_ask_page': True}))


def tag(request):
    return render(request, 'questions/tag.html', prepare_template_context({'tag': 'coffee', 'questions': questions}))


def profile(request):
    user = {
        'name': 'Podosinovik',
        'avatar': 'man3.jpg',
    }
    return render(request, 'questions/profile.html', prepare_template_context({'user': user}))


def login(request):
    return render(request, 'questions/login.html')


def signup(request):
    return render(request, 'questions/signup.html')
