#filewrite.py

f = open("myfile.txt", "w")
f.write("Hello, Welcome to Python\n")
f.write("This is second line\n")
f.write("This is third line\n")
f.write('''This is last line\n''')
f.close()
