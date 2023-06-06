from tkinter import *
from .statistics_python import Statistics
from .login import login


def main():
    def median(stats):
        m = stats.median
        median_text = f"median: {m}"
        median_label.config(text=median_text)

    def average(stats):
        avg = stats.average
        average_text = f"average: {avg}"
        average_label.config(text=average_text)

    def frequent(stats):
        f = stats.frequent
        if not f:
            frequent_text = "No frequent values"
        elif len(f) == 1:
            frequent_text = f"frequent: {f[0]}"
        else:
            frequent_text = "frequent values: "
            for value in f:
                frequent_text += f"{value}, "
            frequent_text = frequent_text[:-2:]
        frequent_label.config(text=frequent_text)

    def standard_deviation(stats):
        S = stats.standard_deviation
        standard_deviation_text = f"standard deviation: {S}"
        standard_deviation_label.config(text=standard_deviation_text)

    def pie_chart(stats):
        stats.show_pie_chart()

    def bar_graph(stats):
        stats.show_bar_graph()

    def frequency_table(stats):
        stats.show_frequency_table()

    def frequency_table_percentage(stats):
        stats.show_percentage_frequency_table()

    root = Tk()
    root.title("Statistics Calculator")
    root.geometry("600x300")

    def calculate():
        x_values = list(map(float, x_values_entry.get().split(" ")))
        f_values = list(map(int, f_values_entry.get().split(" ")))

        frequency_table_variable = {}
        for i, key in enumerate(x_values):
            frequency_table_variable[key] = f_values[i]

        x_label = x_label_entry.get()
        f_label = f_label_entry.get()

        stats = Statistics(frequency_table_variable, x_label, f_label)
        sigma = stats.sigma_x
        sigma_text = f"∑x: {sigma}"
        sigma_label.config(text=sigma_text)

        checkboxes = [do_median, do_average, do_frequent, do_pie_chart, do_bar_graph, do_frequency_table,
                      do_frequency_table_percentage, do_standard_deviation]
        functions = [median, average, frequent, pie_chart, bar_graph, frequency_table, frequency_table_percentage,
                     standard_deviation]
        checkboxes_indexes = ["median", "average", "frequent", "pie_chart", "bar_graph", "frequency_table",
                              "frequency_table_percentage", "standard_deviation"]
        dos = []
        for i, checkbox in enumerate(checkboxes):
            if checkbox.get() == 1:
                dos.append(functions[i])

        for do in dos:
            do(stats)

    x_row_label = Label(root, text="x row: ")
    f_row_label = Label(root, text="f row: ")

    sigma_label = Label(root, text='')
    median_label = Label(root, text='')
    average_label = Label(root, text='')
    frequent_label = Label(root, text='')
    standard_deviation_label = Label(root, text='')

    x_label_entry = Entry(root, width=10)
    x_label_entry.insert(0, "Enter x label")

    f_label_entry = Entry(root, width=10)
    f_label_entry.insert(0, "Enter f label")

    x_values_entry = Entry(root, width=28)
    x_values_entry.insert(0, "Enter all x values separated by a space ' '")

    f_values_entry = Entry(root, width=28)
    f_values_entry.insert(0, "Enter all f values separated by a space ' '")

    start_calculation_button = Button(root, text="Click to start calculation", command=calculate)

    do_median = IntVar()
    do_average = IntVar()
    do_frequent = IntVar()
    do_standard_deviation = IntVar()
    do_pie_chart = IntVar()
    do_bar_graph = IntVar()
    do_frequency_table = IntVar()
    do_frequency_table_percentage = IntVar()

    do_median_checkbox = Checkbutton(root, text="median", variable=do_median)
    do_average_checkbox = Checkbutton(root, text="average", variable=do_average)
    do_frequent_checkbox = Checkbutton(root, text="frequent", variable=do_frequent)
    do_standard_deviation_checkbox = Checkbutton(root, text="standard deviation", variable=do_standard_deviation)
    do_pie_chart_checkbox = Checkbutton(root, text="pie chart", variable=do_pie_chart)
    do_bar_graph_checkbox = Checkbutton(root, text="bar graph", variable=do_bar_graph)
    do_frequency_table_checkbox = Checkbutton(root, text="frequency table", variable=do_frequency_table)
    do_frequency_table_percentage_checkbox = Checkbutton(root, text="frequency table percentage",
                                                         variable=do_frequency_table_percentage)

    x_row_label.grid(row=1, column=0)
    f_row_label.grid(row=2, column=0)

    sigma_label.grid(row=4, column=2)
    median_label.grid(row=4, column=1)
    average_label.grid(row=5, column=1)
    frequent_label.grid(row=6, column=1)
    standard_deviation_label.grid(row=7, column=1)

    x_label_entry.grid(row=1, column=1)
    f_label_entry.grid(row=2, column=1)

    x_values_entry.grid(row=1, column=2)
    f_values_entry.grid(row=2, column=2)

    start_calculation_button.grid(row=3, column=1)

    do_median_checkbox.grid(row=4, column=0)
    do_average_checkbox.grid(row=5, column=0)
    do_frequent_checkbox.grid(row=6, column=0)
    do_standard_deviation_checkbox.grid(row=7, column=0)
    do_pie_chart_checkbox.grid(row=8, column=0)
    do_bar_graph_checkbox.grid(row=9, column=0)
    do_frequency_table_checkbox.grid(row=10, column=0)
    do_frequency_table_percentage_checkbox.grid(row=11, column=0)

    root.mainloop()


app = ""


def choose_app():
    root = Tk()
    root.geometry("250x65")
    root.title("choose app")

    def choose_mashov():
        global app
        app = "mashov"
        root.destroy()

    def choose_statistics():
        global app
        app = "statistics"
        root.destroy()

    choose_mashov_button = Button(root, command=choose_mashov, text="Choose grade statistics app")
    choose_statistics_button = Button(root, command=choose_statistics, text="Choose general purpose statistics")

    choose_statistics_button.grid(row=0, column=0)
    choose_mashov_button.grid(row=1, column=0)
    if app:
        return
    root.mainloop()


def mashov():
    grades = statistics_yahav.wrapper.get_grades_list()
    grade_table = {}
    for grade in grades:
        if grade not in grade_table:
            grade_table[grade] = 1
        else:
            grade_table[grade] += 1
    stats = Statistics(grade_table, "grade", "exams")
    root = Tk()
    root.geometry("280x210")
    root.title("Grade statistics")

    average_label = Label(root, text=f"average grade: {stats.average}")
    median_label = Label(root, text=f"median grade: {stats.median}")

    f = stats.frequent
    if not f:
        frequent_text = "No frequent values"
    elif len(f) == 1:
        frequent_text = f"frequent: {f[0]}"
    else:
        frequent_text = "frequent values: "
        for value in f:
            frequent_text += f"{value}, "
        frequent_text = frequent_text[:-2:]
    frequent_label = Label(root, text=frequent_text)

    standard_deviation_label = Label(root, text=f"standard deviation: {stats.standard_deviation}")

    average_label.grid(row=0, column=0)
    median_label.grid(row=1, column=0)
    frequent_label.grid(row=2, column=0)
    standard_deviation_label.grid(row=3, column=0)

    show_frequency_table_button = Button(root, text="show frequency table", command=stats.show_frequency_table)
    show_percentage_frequency_table_button = Button(root, text="show percentage frequency table",
                                                    command=stats.show_percentage_frequency_table)
    show_pie_chart_button = Button(root, text="show pie chart", command=stats.show_pie_chart)
    show_bar_graph_button = Button(root, text="show bar graph", command=stats.show_bar_graph)

    show_frequency_table_button.grid(row=4, column=0)
    show_percentage_frequency_table_button.grid(row=5, column=0)
    show_pie_chart_button.grid(row=6, column=0)
    show_bar_graph_button.grid(row=7, column=0)
    root.mainloop()


if __name__ == '__main__':
    choose_app()
    if app == "statistics":
        main()
    elif app == "mashov":
        login()
        import statistics_yahav.wrapper
        mashov()
