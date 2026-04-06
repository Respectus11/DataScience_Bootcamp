#level one 
def reverse_string():
    user_input=input("please enter string to reverse ")
    store=user_input[::-1]
    print(" the reversed output is "+ store)
#calling the function
reverse_string()