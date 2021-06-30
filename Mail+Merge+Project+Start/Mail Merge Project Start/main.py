#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt", mode="r") as file:
    template_of_the_letter = file.readlines()

with open("Input/Names/invited_names.txt", mode="r") as file:
    names_list = file.readlines()

for name in names_list:
    text = ""
    with open(f"Input/Names/{name}.txt", mode="w") as file:
        file.write(text.join(template_of_the_letter).replace("[name]", name.strip("\n")))




