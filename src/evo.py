from PIL import Image, ImageDraw
from random import randint
import time
import json
import compare
import gene

class Evo:

    def __init__(self, img_src):
        self.goal = Image.open('./../art/{0}'.format(img_src))
        self.poly_count = 50
        gene.Gene.set_max(self.goal.size)
        self.compare = compare.FitnessCalculator(self.goal)
        self.create_first_gen()

    def create_first_gen(self):
        gene_list = []

        gene_list.append(self.create_random_gene())

        self.save_genes(gene_list)
        self.parent_genes = gene_list
        self.parent = self.render_genes(gene_list)
        self.parent.save("./../art/evo/parent.jpg", "JPEG")
        self.best_fit = self.compare.test_new_img(self.parent)

    def create_random_gene(self):
        return gene.Gene.get_random_gene()

    def render_genes(self, gene_list):
        canvas = self.get_blank_canvas()
        draw = ImageDraw.Draw(canvas)
        for gene in gene_list:
            layer = self.get_blank_canvas()
            layer_draw = ImageDraw.Draw(layer)
            (corners, fill) = (gene.dim, gene.color)
            layer_draw.polygon(corners, fill)
            canvas = Image.alpha_composite(canvas, layer)
        return canvas

    def get_blank_canvas(self):
        return Image.new(
            'RGBA',
            self.goal.size,
            (0, 0, 0, 80)
        )

    def evolve(self):
        if len(self.parent_genes) < self.poly_count:
            self.child_genes = list(self.parent_genes)
            mutate = self.create_random_gene()
            self.child_genes.append(mutate)

        else:
            pos = randint(0, len(self.parent_genes)-1)
            mutating_gene = self.parent_genes[pos:pos + 1]
            mutated_gene = mutating_gene[0].copy().mutate()

            self.child_genes = list(self.parent_genes)
            self.child_genes[pos] = mutated_gene

        layer = self.render_genes(self.child_genes)
        self.child = layer


    def fitness_test(self):
        fitness = self.compare.test_new_img(self.child)
        if fitness <= self.best_fit:
            self.parent_genes = self.child_genes
            self.best_fit = fitness

    def save_genes(self, gene_list):
        history = open('./../data/current.dna', 'w')

        for gene in gene_list:
            history.write("%s\n" % gene.to_JSON())

    def generations(self, x):
        for i in range(x):
            self.evolve()
            self.fitness_test()

        self.final = self.render_genes(self.parent_genes)
        self.final.save("./../art/evo/final.jpg", "JPEG")


new_evo = Evo('skull.jpeg')
start = time.time()
new_evo.generations(100000)
print time.time() - start
