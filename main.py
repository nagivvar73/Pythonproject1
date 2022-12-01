# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('HELOW')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

file_html = open("C:\\Users\\mahid\\PycharmProjects\\Pythonproject1\\Results\\demo1.html", "w")


# Adding the input data to the HTML file
file_html.write('''<html>
<head>
<title>HTML File1</title>
</head> 
<body>
<h1>Welcome Finxters</h1>           
<p>Example demonstrating How to generate HTML Files in Python</p> 
</body>
</html>''')
# Saving the data into the HTML file
file_html.close()
