import json
from random import randint

class Gene:

    max_x = 0
    max_y = 0

    def __init__(self, options):
        (self.dim, self.color) = options

    @classmethod
    def random_pt(cls):
        return (
            randint(0, cls.max_x -1),
            randint(0, cls.max_y -1))

    @classmethod
    def random_color(cls):
        return (
            randint(0,255),
            randint(0,255),
            randint(0,255),
            80)

    @classmethod
    def create_coord(cls):
        corners = []
        num_cor = randint(3,5)
        for _ in range(num_cor):
            corners.append(cls.random_pt())
        return corners


    @classmethod
    def set_max(cls, size):
        (cls.max_x, cls.max_y) = size

    @classmethod
    def get_random_gene(cls):
        color = cls.random_color()
        coord = cls.create_coord()
        return cls((coord, color))


    def mutate(self):
        chance = randint(0, 100)
        points = len(self.dim)

        if chance < 70:
            randpt = randint(0, points - 1)
            new_point = Gene.random_pt()
            self.dim[randpt] = new_point

        if chance <= 10:
            self.color = Gene.random_color()

        return self

    def copy(self):
        return Gene((self.dim, self.color))

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
