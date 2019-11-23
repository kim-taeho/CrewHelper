import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from datetime import datetime, timedelta
from django_seed import Seed
from projects import models as project_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command create many project jobs"

    def add_arguments(seld, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many project jobs do you want to create"
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        all_project = project_models.Project.objects.all()       
        seeder.add_entity(project_models.ProjectJob, number, {
            "name": lambda x: seeder.faker.address(),
            "project": lambda x: random.choice(all_project),
            "charger": lambda x: random.choice(all_user),
            "start": lambda x: datetime.now(),
            "due": lambda x: datetime.now() + timedelta(days=random.randint(2, 10)),
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} project jobs created!"))

