import csv
from adoptable import Adoptable
from redis_om import Migrator


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
    data = Adoptable.find(
        (Adoptable.name == 'Charlic')
        & (Adoptable.age > 9)
        & (Adoptable.children is True)
        & (Adoptable.description % 'play')
        & ~(Adoptable.description % 'anxious')
    ).sort_by('age')


if __name__ == '__main__':
    load()
