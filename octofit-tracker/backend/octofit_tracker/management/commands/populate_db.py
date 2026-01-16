from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        get_user_model().objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = get_user_model().objects.create_user(email='ironman@marvel.com', username='ironman', team=marvel)
        captain = get_user_model().objects.create_user(email='captain@marvel.com', username='captain', team=marvel)
        batman = get_user_model().objects.create_user(email='batman@dc.com', username='batman', team=dc)
        superman = get_user_model().objects.create_user(email='superman@dc.com', username='superman', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', distance=5)
        Activity.objects.create(user=batman, type='cycle', distance=20)

        # Create workouts
        Workout.objects.create(user=captain, name='Pushups', reps=50)
        Workout.objects.create(user=superman, name='Squats', reps=100)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
