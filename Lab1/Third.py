def have_common_element(list1, list2):
    for element in list1:
        if element in list2:
            return True
    return False

list1 = list(map(int, input("Enter elements of the first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of the second list separated by space: ").split()))

if have_common_element(list1, list2):
    print("The lists have at least one common element.")
else:
    print("The lists do not have any common elements.")