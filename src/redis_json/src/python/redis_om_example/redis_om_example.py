import csv

from redis_om import Migrator

from adoptable import Adoptable


def load():
    # open csv file
    # TODO: provide data for load func
    with open(file='animals.csv', mode='r') as handler:
        # create csv reader
        reader = csv.DictReader(handler)
        for animal in reader:
            # create Adoptable instance
            adoptable = Adoptable(**animal)
            print(f'[+] Adoptable: {adoptable.name} loaded..')
            # save model
            adoptable.save()

    # create RedisSearch index
    Migrator().run()


def search_animals():
    data = (
        Adoptable.find(
            (Adoptable.name == "Charlic")
            & (Adoptable.age > 9)
            & (Adoptable.children.is_(True))
            & (Adoptable.description % "play")
            & ~(Adoptable.description % "anxious")
        )
        .sort_by("age")
    )
    return data


if __name__ == '__main__':
    load()
