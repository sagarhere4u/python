#fileread.py

f = open("myfile.txt", "r")
#read function reads complete contents of the file
print(f.read())
f.close()

print("##############################")

f = open("myfile.txt", "r")
#for loop reads the file line by line
for x in f:
    print("----------------------")
    print(x)
f.close()

print("##############5-6################")

#reading line number 5 and 6
f = open("myfile.txt", "r")
cnt = 1
for x in f:
    if cnt == 5 or cnt == 6:
        print("----------------------")
        print(x)
    cnt = cnt + 1
f.close()
