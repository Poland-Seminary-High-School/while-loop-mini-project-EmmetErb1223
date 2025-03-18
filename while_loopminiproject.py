'''Im going to make a code that lets you choose what food you want 
to order for your dinner while using breaks, while loops, and if statments'''
print("What special would you like from our menu sir.")

print("we have Breadsticks, ice cream, steak and burgers")
prompt = "\nEnter your speical food item."
prompt += "\nEnter 'quit' when you are finished. "

Speicals = []     

while True:
            Speical = input(prompt)
            if Speical == "quit":
                break
            if Speicals : print("We'll get these right away for you sir.")
print (f"I love those {Speical.title()}!")
Speicals.append(Speical)
print(f"{Speical.lower()} has been added.")


