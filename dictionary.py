#dictionary.py
dict = {}
dict['one'] = 'This is one'
dict[2] = "This is two"

tinydict = { 'name': 'john', 'deptt': 'sales', 'salary': '100'}

print (dict[2])  #prints "This is two"
print(dict)      #prints {'one': 'This is one', '2': 'This is two'}
print(tinydict)  #prints { 'name': 'john', 'deptt': 'sales', 'salary': '100'}

print(tinydict.keys())   #prints ['name', 'deptt', 'salary']
print(tinydict.values()) #prints ['john', 'sales', '100]