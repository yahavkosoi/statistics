import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import math
import random


class Statistics:
    def __init__(self, frequency_table, x, f):
        self.frequency_percentages = None
        self.frequency_percentages_for_pie_chart = None
        self.frequency_percentages_for_frequency_table = None
        self.median_ready_list = None
        self.median = None
        self.frequency_table = frequency_table
        self.generate_list()
        self.length = len(self.median_ready_list)
        self.calculate_median()
        self.calculate_average()
        self.calculate_frequent()
        self.calculate_frequency_percentage()
        self.x = x
        self.f = f
        self.bar, self.pie = False, False
        self.calculate_standard_deviation()
        self.sigma_x = sum(self.median_ready_list)

    def generate_list(self):
        new_list = []
        for item in self.frequency_table.items():
            for _ in range(item[1]):
                new_list.append(item[0])
        self.median_ready_list = self.bubble_sort(new_list)

    @staticmethod
    def bubble_sort(l):
        for i in range(len(l)):
            for j in range(len(l) - 1):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
        return l

    def calculate_median(self):
        if self.length % 2 == 0:
            self.median = sum(
                (self.median_ready_list[self.length // 2 - 1], self.median_ready_list[self.length // 2])) / 2
        else:
            self.median = self.median_ready_list[(self.length + 1) // 2 - 1]

    def calculate_average(self):
        self.average = sum(self.median_ready_list) / len(self.median_ready_list)

    @staticmethod
    def find_all_indices_of_element(list_, element):
        indices = []
        for i, value in enumerate(list_):
            if value == element:
                indices.append(i)
        return indices

    def calculate_frequent(self):
        values = list(self.frequency_table.values())
        random_value = random.choice(values)
        same = True
        for value in values:
            if value != random_value:
                same = False
        if same:
            self.frequent = None
            return
        keys = list(self.frequency_table.keys())
        max_ = max(values)
        indices = self.find_all_indices_of_element(values, max_)
        frequents = []
        for i in indices:
            frequents.append(keys[i])
        self.frequent = frequents

    def calculate_frequency_percentage(self):

        self.frequency_percentages = []
        self.frequency_percentages_for_pie_chart = []
        self.frequency_percentages_for_frequency_table = {}
        for key in self.frequency_table.keys():
            percentage = str(round(self.frequency_table[key] / self.length * 100, 1))

            self.frequency_percentages_for_frequency_table[key] = float(percentage)
        for item in self.frequency_table.items():
            percentage = item[1] / self.length * 100
            self.frequency_percentages.append(f"{item[0]}: {percentage}%")
            self.frequency_percentages_for_pie_chart.append(percentage)

    def calculate_standard_deviation(self):
        average = self.average
        N = self.length
        sum_ = 0
        for key, value in self.frequency_table.items():
            sum_ += (key - average) ** 2 * value
        self.standard_deviation = math.sqrt(sum_ / N)

    def show_bar_graph(self):
        if self.pie:
            plt.figure(0)
        self.bar = True
        x = list(self.frequency_table.keys())
        f = list(self.frequency_table.values())
        plt.bar(x, f)
        if self.x:
            plt.xlabel(self.x)
        if self.f:
            plt.ylabel(self.f)
        plt.show()

    def show_pie_chart(self):
        if self.bar:
            plt.figure(1)
        self.pie = True
        labels = list(self.frequency_table.keys())
        sizes = self.frequency_percentages_for_pie_chart
        _, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.show()

    def show_frequency_table(self):
        number_of_values = len(self.frequency_table.keys())
        length_of_image = (number_of_values) * 50 + 150
        img = Image.new("RGB", (length_of_image, 100), (255, 255, 255))
        img_draw = ImageDraw.Draw(img)
        img_draw.line(((0, 50), (length_of_image, 50)), fill="black", width=0)
        for i in range(1, number_of_values + 1):
            img_draw.line(((i * 50, 0), (i * 50, 100)), fill="black")
        try:
            font = ImageFont.truetype("/fonts/NewYork.ttf", 20)
        except:
            font = ImageFont.truetype("fonts\\NewYork.ttf", 20)
        x_label = self.x
        img_draw.text((length_of_image - 150 + 10, 15), x_label, font=font, fill=(0, 0, 0))
        f_label = self.f
        img_draw.text((length_of_image - 150 + 10, 65), f_label, font=font, fill=(0, 0, 0))

        keys = list(self.frequency_table.keys())
        keys = self.bubble_sort(keys)
        for i, key in enumerate(keys):
            img_draw.text((50 * i + 10, 15), str(key), font=font, fill=(0, 0, 0))
            img_draw.text((50 * i + 10, 65), str(self.frequency_table[key]), font=font, fill=(0, 0, 0))
        img.show()

    def show_percentage_frequency_table(self):
        number_of_values = len(self.frequency_table.keys())
        length_of_image = (number_of_values) * 65 + 150
        img = Image.new("RGB", (length_of_image, 100), (255, 255, 255))
        img_draw = ImageDraw.Draw(img)
        img_draw.line(((0, 50), (length_of_image, 50)), fill="black", width=0)
        for i in range(1, number_of_values + 1):
            img_draw.line(((i * 65, 0), (i * 65, 100)), fill="black")
        try:
            font = ImageFont.truetype("/fonts/NewYork.ttf", 20)
        except:
            font = ImageFont.truetype("fonts\\NewYork.ttf", 20)
        x_label = self.x
        img_draw.text((length_of_image - 150 + 10, 15), x_label, font=font, fill=(0, 0, 0))
        f_label = self.f
        img_draw.text((length_of_image - 150 + 10, 65), f_label, font=font, fill=(0, 0, 0))

        keys = list(self.frequency_table.keys())
        keys = self.bubble_sort(keys)
        for i, key in enumerate(keys):
            img_draw.text((65 * i + 10, 15), str(key), font=font, fill=(0, 0, 0))
            img_draw.text((65 * i + 10, 65), str(self.frequency_percentages_for_frequency_table[key]) + "%", font=font,
                          fill=(0, 0, 0))
        img.show()


if __name__ == '__main__':
    frequency_table = {3: 2, 4: 4, 5: 7, 6: 2, 7: 3, 8: 7, 9: 7, 10: 1}
    stats = Statistics(frequency_table, x="grade", f="students")
    print(stats.median)
    print(stats.average)
    print(stats.frequent)
    stats.show_frequency_table()
    stats.show_pie_chart()
    stats.show_bar_graph()
