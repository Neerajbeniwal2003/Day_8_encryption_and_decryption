#TODO 8:print the logo
import art
print(art.ceaser_cipher)
print("**************************** WELCOM TO CEASAR CIPHER *************************")

abcd=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO 1: create a function called 'encrypt' that take original_text and shift_amount as 2 input
# def encrypt(original_text,shift_amount):
#     encrypted=""
# #TODO 2: inside the encrypt function shift each letter of the original_text towards the alphabets 
# #by shift_amount and print the encrypted text.
#     for i in original_text:
#         pos_in_abcd=abcd.index(i)
#         encrypt_pos=pos_in_abcd+shift_amount

#         #TODO 4: what happend if you shift letter "z" by 9?
#         encrypt_pos%=len(abcd)

#         encrypted+=abcd[encrypt_pos]
#     print(encrypted)


#TODO 5:create a function called 'decrypt' that take original_text and shift_amount as 2 input
# def decrypt(original_text,shift_amount):

#     #TODO 6:inside the decrypt function shift each letter of original_text forward in the alphabet 
#     #backward by the shift amount and print the decrypt alphabet

#     decrypted="" #
#     for i in original_text: #q
#         pos_in_abcd=abcd.index(i) #16
#         decrypt_pos=pos_in_abcd-shift_amount #16-9=7
#         decrypt_pos%=len(abcd)
#         decrypted+=abcd[decrypt_pos]
#     print(decrypted)

#TODO 7: combine the encrypt() and decrypt() function into a single fuction called ceasae()
#use the value of user choosen mode to determine the functinality to use
#call the ceasar function instead of encrypt decrypt and pass all three variables.

# def ceasar(mode,massage,shift):
#     if mode=="encode":
#         encrypt(original_text=massage,shift_amount=shift)
#     else:
#         decrypt(original_text=massage,shift_amount=shift)

#There is an other way of doing this here all of upper program is in less lines of code

def ceasar(mode,message,shift):
    output=""
    for i in message: #q
        #TODO 9: what happens if user added number,symbol and spaces
        if i in abcd:
            pos_in_abcd=abcd.index(i) #16
            if mode=="decode":
                # shift*=-1
                decrypt_pos=pos_in_abcd-shift
            # decrypt_pos=pos_in_abcd+shift #16-9=7
            elif mode=="encode":
                decrypt_pos=pos_in_abcd+shift
            # if decrypt_pos<0:
            #     decrypt_pos*=-1
            decrypt_pos%=len(abcd)
            output+=abcd[decrypt_pos]
        else:
            output+=i
    print(f"your {mode}d message is {output}")

    

#TODO 3: call the encrypt function and pass it in the user input 
#you should be able to test the code and encrypt the massage.
proceed=True
while proceed:
    mode=input("enter the mode 'encode' for encrypt 'decode' for decrypt\n").lower()
    if mode=="encode" or mode=="decode":    
        massage=input("enter message \n").lower()
        shift=int(input("enter shift amount\n"))
        ceasar(mode,massage,shift)
    else:
        print("i said enter encode or decode ")

    #TODO 10: can you figured out the way to restart the program
    is_continue=input("do you want to proceed type 'yes or no':").lower()
    if is_continue=='yes':
        proceed=True
    else:
        print("Good bye")
        proceed=False



        



