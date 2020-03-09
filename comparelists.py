from collections import defaultdict

def comparelist(l1[], l2[])

# return elements not in l2 
# fl = list(set(l2) - set(l1))

# return elements in both lists
#fl = list(set(l2) & set(l1))
#fl = [x for x in l2 if x in l1]
fl = set(l2).intersection(l1)

print (fl)