#TODO: Create a letter using starting_letter.txt
with open("../Day 24 Mail Merge/Input/Letters/starting_letter.txt", "r") as f:
    f = f.read()
#for each name in invited_names.txt
with open("../Day 24 Mail Merge/Input/Names/invited_names.txt", "r") as file:
    name = file.readlines()
    for names in name:
        new_letter = f.replace("[name]", names.strip())
        print(new_letter)
        with open(f"../Day 24 Mail Merge/Output/ReadyToSend/letter_for_{names.strip()}.txt", "w") as output:
            output.write(new_letter)
