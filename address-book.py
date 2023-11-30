import os
class AddressBook:
    
    def creating_address_book(self,file_name):
        self.file_name=file_name
        try:
            open(f"{self.file_name}.txt","x")
        except FileExistsError:
            print(f"This person {self.file_name} is already exists in your list")
            getting_choice_for_edit =input("Do you want to overwrite this contact details..")
            if getting_choice_for_edit.lower()=="yes":
                pass
            elif getting_choice_for_edit.lower()=="no":
                exit_choice=input("Do you want to leave this page..")
                if exit_choice.lower()=="yes":
                    print("Exit!!")
                    exit()
            else:
                print("Enter a valid input!")
                exit()
                    
            
    def add_contact(self):
        while True:
            getting_name=input("Enter name...\n")
            if getting_name.isalpha():
                self.creating_address_book(getting_name)
                break
            else:
                print("Only characters are allowed...")
        while True:
            getting_phno=input("Enter phno...\n")
            if len(getting_phno)==10 and getting_phno.isdigit():
                break
            else:
                print("Only 10 numbers are allowed..")
        while True:
            getting_address=input("Enter address...\n")
            if getting_address.isalnum() and len(getting_address)<=20:
                with open(f"{self.file_name}.txt","w")as fptr:
                    print("Contact Details..")
                    fptr.write(f"NAME:{getting_name} \n")
                    fptr.write(f"PHNO:{getting_phno}\n")
                    fptr.write(f"ADDRESS:{getting_address}\n")
                    print(f"contact save succesfully")
                    break
            else:
                print("enter a valid input")
        
    def search_contact_and_view_contact(self):
        while True:
            getting_name_for_search=input("Enter name to search...")
            if getting_name_for_search.isalpha():
                try:
                    fptr=open(f"{getting_name_for_search}.txt","r")
                    value=fptr.read()
                    print(value)
                    
                except FileNotFoundError:
                    print(f"no such contact name in your contact..")
                break
            else:
                print("enter a valid input")
                
    def delete_contact(self):
        try:
            getting_name=input("Enter contact name to delete ...")
            os.remove(f"{getting_name}.txt")
            print(f"contact successfully deleted")
        except FileNotFoundError:
            print("No sucn contact name in your list..")
            
obj=AddressBook()
        
def main():        
    print(f"Hi! here are the options available for you..")
    option_list=["1.Add contact","2.Search contact","3.Delete contact"]

    for option in option_list:
        print(f"{option}")
        
    getting_choice=input("Enter your choice from the above option :")

    if getting_choice=="1":
        obj.add_contact()
    elif getting_choice=="2":
        obj.search_contact_and_view_contact()
    elif getting_choice=="3":
        obj.delete_contact()
    else:
        print(f"please enter  a valid input !")
main()
def sub_main():
    Getting_choice2=input("Do you want to continue this page..[yes\no]")
    if Getting_choice2.lower()=="yes":
        main()

    elif Getting_choice2.lower()=="no":
        print(f"Exit!")
        exit()
    else:
        print("Enter a  valid input")
        exit()
submain()
        


