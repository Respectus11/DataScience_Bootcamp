# Function to count vowels in a string
def count_vowels():
    # Ask user to enter a string
    user_input = input("Please enter a string to count vowels: ")
    
    # Define what vowels are (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    
    # Initialize a counter to zero
    count = 0
    
    # Loop through each character in the string
    for char in user_input:
        # Check if the character is a vowel
        if char in vowels:
            # If it is a vowel, increase the count by 1
            count = count + 1
    
    # Print the final count
    print("The string contains", count, "vowel(s).")

# Call the function to run the program
count_vowels()