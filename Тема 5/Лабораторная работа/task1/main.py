import pprint
d = [[{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(16)]]
# TODO решить с помощью list comprehension и распечатать его
for i in d:
    pprint.pprint(i)
