import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from questions.models import Question, Answer, UserProfile, Vote, Tag
from faker import Faker

fake = Faker()

tags = ['coffee', 'Russia', 'beer', 'comfort', 'aviasales', 'porn', 'MySQL', 'cup', 'like', 'beach', 'crazy', 'Germany',
        'iced', 'magic', 'USA', 'bomd', 'Node.js', 'idea', 'car', 'creature', 'forums', 'chess', 'god', 'weapon',
        '1xbet', 'cold brew', 'marazm', 'tea', 'sand', 'automation']


class Command(BaseCommand):
    help = ''

    def __init__(self):
        super().__init__()
        self.users = []
        self.profiles = []
        self.tags = []
        self.questions = []
        self.answers = []
        self.votes = []

    def get_random_profile(self):
        return self.profiles[random.randint(0, len(self.profiles) - 1)]

    def get_random_tags_for_question(self):
        yielded_tags_indices = set()
        for _ in range(random.randint(2, 5)):
            tag_index = None
            while (tag_index is None) or (tag_index in yielded_tags_indices):
                tag_index = random.randint(0, len(self.tags) // 3)
            yielded_tags_indices.add(tag_index)
            yield self.tags[tag_index]

    def clear(self):
        print('clearing existing data...')
        UserProfile.objects.all().delete()
        Vote.objects.all().delete()
        Tag.objects.all().delete()
        Answer.objects.all().delete()
        Question.objects.all().delete()

    def create_profiles(self):
        print('creating profiles...')
        i = 1
        for user in self.users:
            profile = UserProfile(user=user, rating=random.randint(0, 10))
            profile.avatar.name = 'avatars/man' + str(i) + '.jpg'
            i += 1
            profile.save()
            self.profiles.append(profile)

    def create_tags(self):
        print('creating tags...')
        for tag_name in tags:
            tag = Tag(name=tag_name)
            tag.save()
            self.tags.append(tag)

    def create_questions(self):
        print('creating questions...')
        for profile in self.profiles:
            print('creating questions for user', profile.user.username, '...')
            questions_created = 0
            for i in range(1, random.randint(1, 5)):
                question = Question(title=fake.text(60), text=fake.text(350), user=profile)
                question.save()
                for tag in self.get_random_tags_for_question():
                    question.tags.add(tag)
                questions_created += 1
                self.questions.append(question)
            print('created', questions_created, 'questions')

    def create_answers(self):
        print('creating answers...')
        for question in self.questions:
            print('creating answers for question', question.id)
            answers_created = 0
            is_correct_answer_created = False
            for i in range(random.randint(0, 15)):
                answer = Answer(question=question, text=fake.text(500), user=self.get_random_profile())
                if not is_correct_answer_created and random.randint(0, 1) == 1:
                    is_correct_answer_created = True
                    answer.is_correct = True
                answer.save()
                answers_created += 1
                self.answers.append(answer)
            question.answers_count += answers_created
            question.save()
            print('created', answers_created, 'answers')

    def create_votes(self):
        print('creating votes for questions...')
        for question in self.questions:
            votes_to_create = random.randint(0, 10)
            for i in range(votes_to_create):
                vote = Vote(user=self.get_random_profile())
                vote.save()
                question.votes.add(vote)
                self.votes.append(vote)
            question.votes_count += votes_to_create
            question.save()
            print('created', votes_to_create, 'votes for question', question.id)

        print('creating votes for answers...')
        for answer in self.answers:
            votes_to_create = random.randint(0, 10)
            for i in range(votes_to_create):
                vote = Vote(user=self.get_random_profile())
                vote.save()
                answer.votes.add(vote)
                self.votes.append(vote)
            answer.votes_count += votes_to_create
            answer.save()
            print('created', votes_to_create, 'votes for answer', answer.id)

    def handle(self, *args, **options):
        self.clear()
        self.users = User.objects.all()
        self.create_profiles()
        self.create_tags()
        self.create_questions()
        self.create_answers()
        self.create_votes()
        print('done.')
