from PIL import Image

class FitnessCalculator:

    def __init__(self, goal):
        self.goal = goal
        (self.goal_width, self.goal_height) = self.goal.size

    def calc_fit(self):
        total_diff = 0
        for x in range(0, self.goal_width):
            for y in range(self.goal_height):
                total_diff += self.compare_pixel(x, y)
        return total_diff

    def compare_pixel(self, x, y):
        test_pix = self.test.getpixel((x,y))
        goal_pix = self.goal.getpixel((x,y))
        diff = 0
        for i in range(0, 3):
            diff += abs(test_pix[i] - goal_pix[i])
        return diff

    def new_img(self, newtest):
        self.test = newtest
        return self

    def test_new_img(self, newtest):
        self.new_img(newtest)
        return self.calc_fit()
