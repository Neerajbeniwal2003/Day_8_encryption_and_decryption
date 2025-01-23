# def calculate_love_score(name1,name2):
#     true_list=["T","R","U","E"]
#     love_list=["L","O","V","E"]
#     total_1=0
#     for letter in true_list:
#         temp=0
#         for i in name1.upper():
#             if i==letter:
#                 temp+=1
#                 total_1+=1
#         for i in name2.upper():
#             if i==letter:
#                 temp+=1
#                 total_1+=1
#         print(f"{letter} occurs {temp}")
#     print(f"Total:{total_1}")

#     total_2=0
#     for letter2 in love_list:
#         temp1=0
#         for i in name2.upper():
#             if i==letter2:
#                 temp1+=1
#                 total_2+=1
#         for i in name1.upper():
#             if i==letter2:
#                 temp1+=1
#                 total_2+=1
#         print(f"{letter2} occurs {temp1}")
#     print(f"Total:{total_2}")

#     print(f"Love Score is:{total_1}{total_2}")
# calculate_love_score("Angela Yu","Jack Bauer")

#anothet way of doing this code
def calculate_love_score(name1,name2):
    combined_names=name1+name2
    lower_name=combined_names.lower()
    t=lower_name.count("t")
    r=lower_name.count("r")
    u=lower_name.count("u")
    e=lower_name.count("e")
    first_digit=t+r+u+e

    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")
    second_digit=l+o+v+e

    print(f"Love Score:{first_digit}{second_digit}")

calculate_love_score("Angela Yu","Jack Bauer")
