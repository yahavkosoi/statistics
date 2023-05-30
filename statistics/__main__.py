from tkinter import *
from .statistics_python import Statistics

root = Tk()
root.title("Statistics Calculator")
root.geometry("600x300")


def main():
    x_values = list(map(int, x_values_entry.get().split(" ")))
    f_values = list(map(int, f_values_entry.get().split(" ")))

    frequency_table_variable = {}
    for i, key in enumerate(x_values):
        frequency_table_variable[key] = f_values[i]

    x_label = x_label_entry.get()
    f_label = f_label_entry.get()

    stats = Statistics(frequency_table_variable, x_label, f_label)

    checkboxes = [do_median, do_average, do_frequent, do_pie_chart, do_bar_graph, do_frequency_table]
    checkboxes_indexes = ["median", "average", "frequent", "pie_chart", "bar_graph", "frequency_table"]
    dos = []
    for i, checkbox in enumerate(checkboxes):
        if checkbox.get() == 1:
            dos.append(checkboxes_indexes[i])

    for do in dos:
        print(do)
        exec(do + "(stats)")


def median(stats):
    m = stats.median

    median_text = f"median: {m}"
    median_label = Label(root, text=median_text)

    median_label.grid(row=4, column=1)


def average(stats):
    avg = stats.median

    average_text = f"average: {avg}"
    average_label = Label(root, text=average_text)

    average_label.grid(row=5, column=1)


def frequent(stats):
    f = stats.frequent

    frequent_text = f"frequent: {f}"
    frequent_label = Label(root, text=frequent_text)

    frequent_label.grid(row=6, column=1)


def pie_chart(stats):
    stats.show_pie_chart()


def bar_graph(stats):
    stats.show_bar_graph()


def frequency_table(stats):
    stats.show_frequency_table()


x_row_label = Label(root, text="x row: ")
f_row_label = Label(root, text="f row: ")

x_label_entry = Entry(root, width=10)
x_label_entry.insert(0, "Enter x label")

f_label_entry = Entry(root, width=10)
f_label_entry.insert(0, "Enter f label")

x_values_entry = Entry(root, width=28)
x_values_entry.insert(0, "Enter all x values separated by a space ' '")

f_values_entry = Entry(root, width=28)
f_values_entry.insert(0, "Enter all f values separated by a space ' '")

start_calculation_button = Button(root, text="Click to start calculation", command=main)

do_median = IntVar()
do_average = IntVar()
do_frequent = IntVar()
do_pie_chart = IntVar()
do_bar_graph = IntVar()
do_frequency_table = IntVar()

do_median_checkbox = Checkbutton(root, text="median", variable=do_median)
do_average_checkbox = Checkbutton(root, text="average", variable=do_average)
do_frequent_checkbox = Checkbutton(root, text="frequent", variable=do_frequent)
do_pie_chart_checkbox = Checkbutton(root, text="pie chart", variable=do_pie_chart)
do_bar_graph_checkbox = Checkbutton(root, text="bar graph", variable=do_bar_graph)
do_frequency_table_checkbox = Checkbutton(root, text="frequency table", variable=do_frequency_table)

x_row_label.grid(row=1, column=0)
f_row_label.grid(row=2, column=0)

x_label_entry.grid(row=1, column=1)
f_label_entry.grid(row=2, column=1)

x_values_entry.grid(row=1, column=2)
f_values_entry.grid(row=2, column=2)

start_calculation_button.grid(row=3, column=1)

do_median_checkbox.grid(row=4, column=0)
do_average_checkbox.grid(row=5, column=0)
do_frequent_checkbox.grid(row=6, column=0)
do_pie_chart_checkbox.grid(row=7, column=0)
do_bar_graph_checkbox.grid(row=8, column=0)
do_frequency_table_checkbox.grid(row=9, column=0)

root.mainloop()
