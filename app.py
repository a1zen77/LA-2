import sys
from jinja2 import Template
import matplotlib.pyplot as plt

zsh_input = sys.argv[1:]
parameter_1 = zsh_input[1]
error_html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Something Went Wrong</title>
</head>

<body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
</body>

</html>"""


data_array = []
f = open("data.csv","r")
for i in f.readlines()[1:]:
    data_array.append(i.strip().split(", "))
f.close()


out=""""""
if zsh_input[0]=="-s":
    dict = {}
    total_marks = 0
    for i in data_array:
        if i[0]==parameter_1:
            dict[i[1]] = i[2]
            total_marks += int(i[2])
    if len(dict)>0:
        stu = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Data</title>
</head>

<body>
    <h1>Student Details</h1>
    <table border="1">
        <tr>
            <th>Student ID</th>
            <th>Course ID</th>
            <th>Marks</th>
        </tr>
        {% for i in dict %}
        <tr>
            <td>{{ parameter_1 }}</td>
            <td>{{ i }}</td>
            <td>{{ dict[i] }}</td>
        </tr>
        {% endfor %}
        <tr>
            <td colspan="2" style="text-align: center;">Total Marks</td>
            <td>{{ total_marks }}</td>
        </tr>
    </table>
</body>

</html>
"""
        TEMP = Template(stu)
        out = TEMP.render(dict=dict,parameter_1=parameter_1,total_marks=total_marks)
    else:
        TEMP = Template(error_html)
        out = TEMP.render()

elif zsh_input[0]=="-c":
    marks = []
    for i in data_array:
        if i[1]==parameter_1:
           marks.append(int(i[2]))

    if len(marks)>0:
        avg_marks = round(sum(marks)/len(marks),1)
        max_marks = max(marks)

        crs = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Data</title>
</head>

<body>
    <h1>Course Details</h1>
    <table border="1">
        <tr>
            <th>Average Marks</th>
            <th>Maximum Marks</th>
        </tr>
        <tr>
            <td>{{ avg_marks }}</td>
            <td>{{ max_marks }}</td>
        </tr>
    </table>
    <img src="histo.png" alt="Histogram">
</body>

</html>
        """

        plt.hist(marks)
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("histo.png")
        TEMP = Template(crs)
        out = TEMP.render(avg_marks=avg_marks,max_marks=max_marks)
    else:
        TEMP = Template(error_html)
        out = TEMP.render()

else:
    TEMP = Template(error_html)
    out = TEMP.render()

outer = open("output.html","w")
outer.write(out)
outer.close()