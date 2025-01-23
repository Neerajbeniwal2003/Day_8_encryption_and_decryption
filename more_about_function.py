# def greet():
#     print("hii")
#     print("how are you")
#     print("how's going")

# greet()

#function that allowes for input

def meet(name): #here name is the parameter 
    print(f"hello {name}")
    print(f"how do you do {name}")

meet("neeraj") #so here neeraj is the argument

#PROGRAM for how many weeks left to become 90 year old
def life_in_weeks(age):
    total_weeks=90*52
    weeks_user_lived=age*52
    print(f"you have {total_weeks-weeks_user_lived} weeks left.")

life_in_weeks(21)

#Function with more than one input
def greet_with(name,loc): 
    print(f"hello{name}")
    print(f"what is it like in {loc}")

#there are two diffetent way to call that type of function
greet_with("neeraj","delhi") #here this is called positional argumant 
greet_with(loc="delhi",name="neeraj") #here this is called keyword argument

