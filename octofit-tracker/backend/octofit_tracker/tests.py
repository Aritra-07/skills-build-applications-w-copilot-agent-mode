from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=ironman, type='run', distance=5)
        Workout.objects.create(user=batman, name='Pushups', reps=50)
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        user = User.objects.get(username='ironman')
        self.assertEqual(user.team.name, 'Marvel')

    def test_activity(self):
        activity = Activity.objects.get(type='run')
        self.assertEqual(activity.distance, 5)

    def test_workout(self):
        workout = Workout.objects.get(name='Pushups')
        self.assertEqual(workout.reps, 50)

    def test_leaderboard(self):
        leaderboard = Leaderboard.objects.get(team__name='Marvel')
        self.assertEqual(leaderboard.points, 100)
