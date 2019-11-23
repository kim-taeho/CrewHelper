from django.core.management.base import BaseCommand
from projects.models import Category


class Command(BaseCommand):

    help = "This command create categories"

    def handle(self, *args, **options):
        categories = [
            "공모전",
            "인문",
            "기획/아이디어",
            "디자인",
            "광고/마케팅",
            "문학/시나리오",
            "영상/UCC/사진",
            "슬로건/네이밍",
            "논문/리포트",
            "캐릭터/만화/게임",
            "음악/미술/무용",
            "건축/인테리어",
            "과학/공학",
            "취업/창업",
            "장학금",
            "전시/페스티발",
            "봉사활동",
            "해외",
            "인턴/정규직 채용",
        ]

        for a in categories:
            Category.objects.create(name=a)
        
        self.stdout.write(self.style.SUCCESS("Categories created!"))

