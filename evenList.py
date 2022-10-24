a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# def evenList(list):
#     for item in list:
#         if item % 2 == 0:
#             print(item)
#
# evenList(a)

b = [item for item in a if item % 2 == 0]
print(b)