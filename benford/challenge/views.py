import io
import math
import os

import matplotlib.pyplot as plt
import pandas as pd
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from challenge.models import DataTable

# set width of bar
barWidth = 0.25
numbers = range(1, 10)


def chisq_stat(O, E):
    for o, e in zip(O, E):
        print("o", o)
        print("e", e)
    return sum((o - e) ** 2 / e for (o, e) in zip(O, E))


class DataCreateView(CreateView):
    model = DataTable
    template = "upload.html"
    fields = ["data_file"]
    success_url = "/"

    # overwrite default post
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data_file = request.FILES["data_file"]
        if form.is_valid():
            # try read a file
            try:
                # get pandas dataframe
                df = pd.read_csv(data_file, sep="\t", decimal=".")
                # get counted values from defined column
                value_counts = df["7_2009"].value_counts(dropna=False, normalize=True)
            # return exception if file is invalid or file don't have valid header in column
            except Exception as msg:
                messages.add_message(request, messages.ERROR, "File is invalid, check format or file structure")
                return redirect("/upload/")
            leading_counts = value_counts[:9]
            print("list\n", list(leading_counts))
            expected = [math.log10(1 + 1 / n) for n in numbers]
            chisqr = chisq_stat(leading_counts, expected)
            # save object
            data_object = form.save()
            data_object.chisqr = round(chisqr, 2)
            # get image path
            image_path = os.path.join("static/graphs", f"{data_object.pk}.png")
            # create graphs directory if not exists
            directory = os.path.dirname(image_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Generat matplotlib plot
            # Set position of bar on X axis
            br1 = numbers
            br2 = [x + barWidth for x in br1]
            # Make the plot
            plt.bar(br1, expected, color="g", width=barWidth, edgecolor="grey", label="Expected")
            calculated = [100 * num for num in list(leading_counts)]
            print("calculated", calculated)
            plt.bar(br2, calculated, color="b", width=barWidth, edgecolor="grey", label="Observed")

            # Adding Xticks
            plt.xlabel("Liding numbers", fontweight="bold", fontsize=13)
            plt.ylabel("Normalized value", fontweight="bold", fontsize=13)
            plt.xticks([r + barWidth for r in numbers], numbers)

            plot_path = os.path.join("static/graphs", f"plot{data_object.pk}.png")
            plt.legend()
            plt.savefig(plot_path, dpi=300, format="png")
            plt.close()
            # generate plot for 9 leading digits
            plot = leading_counts.plot(kind="bar")
            # get plot figure
            figure = plot.figure
            # save image
            figure.savefig(image_path, dpi=300, format="png")
            return self.form_valid(form)

        else:
            return self.form_invalid(form)


class DataListView(ListView):
    model = DataTable


class DataDetailView(DetailView):
    model = DataTable
