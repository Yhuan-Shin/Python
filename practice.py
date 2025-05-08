import re
# # check if odd or even numbers
# def checkOddEven():
#     num = 5 
#     if num % 2 == 0:
#         print("Even")
#         return True
#     elif num % 2 == 1:
#         print("Odd")
#         return False




# # Check the status

# # a = 1
# # b = 1
# # flag = True

# # if (a >= 0 != b >= 0) and not flag:
# #     print(True)
# # elif (a < 0 and b < 0) and flag:
# #     print(True)
# # else:
# #     print(False)

# def friends_in_trouble(a,b):
#     if a==True and b==True:
#         print("You're in trouble")
#     elif a==True or b ==False:
#         print("Your good")

# j_angry = True
# s_angry = True

# friends_in_trouble(j_angry, s_angry)


# string validation
 
pattern = '^(?=.*[0-9])[A-Z0-9][^ /]{3}$'
word = "He3p"
check = re.match(pattern,word)



def checkString():
    if check:
        print("Valid")
    else:
        print("not valid")


checkString()
    





     


