import sys

def list_details(lst):
    print("List:", lst)
    print("Length:", len(lst))
    print("Size:", sys.getsizeof(lst))

list_details([1, 2, 3])

list_details([1,2,3])