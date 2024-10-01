# home/management/commands/populate_db.py

import json
from django.core.management.base import BaseCommand
from django.apps import apps
from movie.models import Movie
from theatre.models import Theatre, Show
from django.conf import settings

User = apps.get_model(settings.AUTH_USER_MODEL)

class Command(BaseCommand):
    help = 'Populates the database with data from data.json'

    def handle(self, *args, **kwargs):
        with open('home/fixtures/data.json', 'r') as file:
            datas = json.load(file)
            for data in datas:

                if data.get("model") == "movie.movie":
                    Movie.objects.create(
                        pk=data["pk"],
                        name=data["fields"]["name"],
                        cast=data["fields"]["cast"],
                        director=data["fields"]["director"],
                        language=data["fields"]["language"],
                        run_length=data["fields"]["run_length"],
                        certificate=data["fields"]["certificate"],
                        popularity_index=data["fields"]["popularity_index"],
                        trailer=data["fields"]["trailer"],
                        image=data["fields"]["image"],
                    )
                elif data.get("model") == "theatre.theatre":

                    Theatre.objects.create(
                        name=data["fields"]["name"],
                        address=data["fields"]["address"],
                        city=data["fields"]["city"],
                        no_of_screen=data["fields"]["no_of_screen"],
                        admin_id=User.objects.get(pk=1)
                    )

                elif data.get("model") == "theatre.show":
                    Show.objects.create(
                        movie= Movie.objects.get(pk=data["fields"]["movie"]),
                        theatre= Theatre.objects.get(pk=data["fields"]["theatre"]),
                        screen = data["fields"]["screen"],
                        date = data["fields"]["date"],
                        time = data["fields"]["time"]
                    )

        print("Data populated successfully")
