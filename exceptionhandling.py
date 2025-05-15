#exceptionhandling.py

try:
    f = open("unknown.txt", "r")
    print(f.read())
    f.close()
except Exception:
    print("File unknown.txt does not exists!")