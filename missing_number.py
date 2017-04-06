def find_missing(r1, r2):
    if len(r1)==0 or len(r2)==0:
        return 0
    if len(r1)==len(r2):
        return 0

# Set longer array to lst1, shorter to lst2
    if len(r1) > len(r2):
        list1 = r1
        list2 = r2
    else:
        list1 = r2
        list2 = r1
   for element in list1:
       if element not in list2:
           return element