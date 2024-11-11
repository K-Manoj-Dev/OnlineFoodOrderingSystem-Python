from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu

class LoginSystem:
    
    def Login(self):
        mailid = input("Email Id: ")
        password = input("Password: ")

        user = UserManager.FindUser(mailid, password)

        if user is not None:
            print("Login Successful...")
            menu = MainMenu()
            menu.Start()
        else:
            print("Invalid Email Id or Password. Please try again.")

    def Register(self):
        while True:
            name = input("Name: ")
            mobile = input("Mobile No: ")
            
            # Mobile number validation
            if len(mobile) != 10 or not mobile.isdigit():
                print("Invalid Mobile Number. It must be exactly 10 digits.")
                continue

            mailid = input("Email Id: ")
            
            # Email validation
            if "@" not in mailid:
                print("Invalid Email Id. It must contain '@'.")
                continue

            password = input("Password: ")
            
            # Password validation
            if len(password) < 8 or not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
                print("Invalid Password. It must be at least 8 characters long and include both letters and numbers.")
                continue

            user = User(name, mobile, mailid, password)
            UserManager.AddUser(user)
            print("Registration Successful! You can now log in.")
            break  

    def GuestLogin(self):
        print("Logged in as Guest. Limited features available.")
        menu = MainMenu()
        menu.Start()

    def Exit(self):
        print("Thank you for using our food app. Goodbye!")
        exit()

    def ValidationOptions(self, option):
        if hasattr(self, option):
            getattr(self, option)()
        else:
            print("Invalid Choice. Please try again.")

class FoodApp:
    LoginOptions = {1: "Login", 2: "Register", 3: "GuestLogin", 4: "Exit"}

    @staticmethod
    def Init():
        print("<< Welcome to Online Food Ordering >>")

        loginSystem = LoginSystem()
        
        while True:
            for option, action in FoodApp.LoginOptions.items():
                print(f"{option}. {action}", end="  ")
            print()

            try:
                choice = int(input("Please Enter Your Choice: "))
                loginSystem.ValidationOptions(FoodApp.LoginOptions[choice])
            except (ValueError, KeyError):
                print("Invalid Input. Please enter a valid choice.")
