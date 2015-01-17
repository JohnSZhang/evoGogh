from PIL import Image

class Evo:

    def __init__(self, img_src):
        self.goal = Image.open('./../art/{0}'.format(img_src))
        self.create_first_gen()

    def create_first_gen(self):
        self.parent = Image.new(self.goal.mode, self.goal.size)
        self.parent.save("parent.jpg", "JPEG")

    def evolve(self):
        self.child = self.parent
        self.child.
        self.child.save("child.jpg", "JPEG")

new_evo = Evo('starry.jpg')
new_evo.create_test()
