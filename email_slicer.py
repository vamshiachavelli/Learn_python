# ask user for email
# using split function at @, first word is name,
# using split again at ., take first for domain, second for extension
# example; 
'''    enter email = "rahalu@gmail.com
        name = rahul
        domain = gmail
        extension = com'''

def main():
    print("Welcome to email slicer\n")
    email = input("enter email : ")
    if email == "exit":
        exit()
    else:
        (name, domain)= email.split("@")
        (domain, extension)= domain.split(".")
        print(f"name : {name}")
        print(f"Domain : {domain}")
        print(f"exension : {extension}\n")

while True:
    main()