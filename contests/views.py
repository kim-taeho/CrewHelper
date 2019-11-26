from django.shortcuts import render, redirect
import requests
from django.views.generic import ListView
from django.urls import reverse
from bs4 import BeautifulSoup
from . import models

url = "http://campusmon.jobkorea.co.kr/Contest/List"


def extract_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "paging"})
    pages = pagination.find_all("a")

    spans = []

    for page in pages[:-1]:
        spans.append(int(page.string))

    max_page = spans[-1]
    return max_page


def extract_job(html):
    title = html.find("p", {"class": "ti"}).find("a")["title"]
    company = html.find("p", {"class": "tx"}).get_text()
    day = html.find("td", {"class": "day"}).find("span")["title"]

    company = company.strip()
    day = day.strip()
    
    new_note = models.Contests.objects.create(
        title=title,
        company=company,
        day=day
    )
    new_note.save()


def scrape(request):
    last_page = extract_pages()
    for page in range(last_page):
        result = requests.get(f"{url}?_Page={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        extract_job(soup)
    return redirect(reverse("contests:contests"))


class ContestView(ListView):
    model = models.Contests
    paginate_by = 24
    paginate_orphans = 2
    context_object_name = "contests"
    template_name = "contests/contests_all.html"

