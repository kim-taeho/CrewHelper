import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from projects import models as project_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command create many projects"

    def add_arguments(seld, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many projects do you want to create"
        )

    def handle(self, *args, **options):

        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        seeder.add_entity(project_models.Project, number, {
            "name": lambda x: seeder.faker.address(),
            "host": lambda x: random.choice(all_user),
        })
        create_projects = seeder.execute()
        created_clean = flatten(list(create_projects.values()))

        categories = project_models.Category.objects.all()

        for pk in created_clean:
            project = project_models.Project.objects.get(pk=pk)
            all_user = user_models.User.objects.all()
            for a in categories:
                magic_number = random.randint(0, 15)
                if magic_number % 2 == 0:
                    project.categories.add(a)

        self.stdout.write(self.style.SUCCESS(f"{number} projects created!"))

