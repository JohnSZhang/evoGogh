from PIL import Image

class FitnessCalculator:

    def __init__(self, goal, test):
        self.goal = goal
        self.test = test
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

    def new_test(self, newtest):
        self.test = newtest
        return self

goal_img = Image.open('./../art/starry.jpg')
test_img = Image.open('./../art/starryrhone.jpg')

calc = FitnessCalculator(goal_img, test_img)
print calc.calc_fit()
test_img2 = Image.open('./../art/cat.jpg')
print calc.new_test(test_img2).calc_fit()
