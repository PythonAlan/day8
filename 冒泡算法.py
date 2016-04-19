#!/usr/bin/env python3
#antuor:Alan

# li = [13, 22, 6, 99, 11]
#
# for m in range(4):     # 等价于 #for m in range(len(li)-1):
#     if li[m]> li[m+1]:
#         temp = li[m+1]
#         li[m+1] = li[m]
#         li[m] = temp
# for m in range(3):     # 等价于 #for m in range(len(li)-2):
#     if li[m]> li[m+1]:
#         temp = li[m+1]
#         li[m+1] = li[m]
#         li[m] = temp
#
# for m in range(2):     # 等价于 #for m in range(len(li)-3):
#     if li[m]> li[m+1]:
#         temp = li[m+1]
#         li[m+1] = li[m]
#         li[m] = temp
#
# for m in range(1):     # 等价于 #for m in range(len(li)-4):
#     if li[m]> li[m+1]:
#         temp = li[m+1]
#         li[m+1] = li[m]
#         li[m] = temp
#
# print(li)
##############精简###############
li = [13, 22, 6, 99, 11]

for i in range(len(li)):
    for m in range(len(li)-1):
        if li[m] > li[m+1]:
            temp = li[m+1]
            li[m+1] = li[m]
            li[m] = temp
print(li)













