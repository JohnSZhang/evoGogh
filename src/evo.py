from PIL import Image, ImageDraw
from random import randint
import time
import compare

class Evo:

    def __init__(self, img_src):
        self.goal = Image.open('./../art/{0}'.format(img_src))
        (self.goal_x, self.goal_y) = self.goal.size
        self.compare = compare.FitnessCalculator(self.goal)
        self.create_first_gen()

    def create_first_gen(self):
        self.parent = Image.new(self.goal.mode, self.goal.size)
        self.parent.save("./../art/evo/parent.jpg", "JPEG")
        self.best_fit = self.compare.test_new_img(self.parent)

    def evolve(self):
        self.child = self.parent
        draw = ImageDraw.Draw(self.child)
        corners = self.create_poly()
        fill = self.random_color()
        draw.polygon(corners, fill)

    def create_poly(self):
        corners = []
        for _ in range(4):
            corners.append(self.random_pt())
        return corners

    def random_pt(self):
        return (
            randint(0, self.goal_x-1),
            randint(0, self.goal_y-1))

    def random_color(self):
        return (randint(0,255), randint(0,255), randint(0,255))

    def fitness_test(self):
        fitness = self.compare.test_new_img(self.child)
        if fitness >= self.best_fit:
            self.parent = self.child
            self.best_fit = fitness

    def generations(self, x):
        for i in range(x):
            self.evolve()
            self.fitness_test()
        self.parent.save("./../art/evo/final.jpg", "JPEG")


new_evo = Evo('starry.jpg')
new_evo.create_first_gen()
start = time.time()
new_evo.generations(50000)
print time.time() - start
