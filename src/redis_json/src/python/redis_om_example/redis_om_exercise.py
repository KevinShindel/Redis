from typing import List

from pydantic import PositiveInt
from redis_om import JsonModel, EmbeddedJsonModel

# TODO: Create JSON Model and save data
data = {
    "title": "The Matrix",
    "released": 1999,
    "runtime": 137,
    "stars": [
        "Keanu Reeves",
        "Laurence Fishburne",
        "Carrie-Ann Moss"
    ],
    "summary": "A stranger leads computer hacker Neo to a forbidding underworld,"
               " he discovers the truth: the life he knows is the elaborate deception of an evil cyber-intelligence."
}


class ActorModel(EmbeddedJsonModel):
    first_name: str
    last_name: str


class FilmModel(JsonModel):
    title = str
    released: PositiveInt
    runtime: PositiveInt
    stars: List[ActorModel]  # separate model for actors
    summary: str

    class Meta:
        global_key_prefix = "ru204:redis-om"
        model_key_prefix = "film"


def main():
    actors = data.pop('stars')
    actors_list = []
    for actor in actors:
        first_name, last_name = actor.split(' ')
        actors_list.append(ActorModel(first_name=first_name, last_name=last_name))

    film_model = FilmModel(stars=actors_list, **data)
    # film_model.stars = actors_list
    film_model.save()


if __name__ == '__main__':
    main()
