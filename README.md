
# LAB-2

Open prob_statement.pdf to read the purpose of this project.

The frameworks used in this code are jinja2, matplotlib and sys. 
I recommend using the terminal on your system to run this code.
Any default terminal such as command prompt(windows), shell, or .zsh(macOS) will do.
When using jinja2 templates, it is recommended to use a virtual environment of the folder. Follow the steps given below:

1] Open a terminal. 

2] Navigate to the folder containing the python code.

3] Type in the following commands : 

```bash
python3 -m venv .random-env
```
followed by
 ```bash
source .random-env/bin/activate
 ```


4] Use pip freeze to make sure that the required frameworks are present, if not, use
```bash
 pip install jinja2/matplotlib
```

5] To run the python file, just use
```bash
python3 app.py arg1 arg2
```
Refer to the prob_statement.pdf for arg1 and arg2.


A data.csv file has been provided in this repository. The python code uses this data to generate a html file called output.html

I have also written a simple python code read_csv.py to read contents of a csv file without using any external libraries such as numpy or pandas. This code stores data from a csv file in a list of tuples.



