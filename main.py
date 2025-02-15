from models.user import UserManager
from models.password import PasswordManager
from utils.password_gen import PasswordGenerator

def main():
    user_manager = UserManager()

    print("\n🔐 Welcome to Automated Password Manager 🔐\n")

    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter new username: ")
            password = input("Enter a master password: ")
            if user_manager.register(username, password):
                print("✅ Registration successful! Please log in.\n")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter master password: ")

            if user_manager.login(username, password):
                print("\n🔓 Login successful!\n")
                password_manager = PasswordManager(password)

                while True:
                    print("\n📌 Password Manager Menu:")
                    print("1. Add Password")
                    print("2. Retrieve Password")
                    print("3. Generate Strong Password")
                    print("4. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        site = input("Enter site name: ")
                        user = input("Enter username/email: ")
                        pwd = input("Enter password (or leave blank to auto-generate): ")

                        if not pwd:
                            generator = PasswordGenerator(16)
                            pwd = generator.generate()
                            print(f"🔑 Generated Password: {pwd}")

                        password_manager.add_password(site, user, pwd)
                        print(f"✅ Password for {site} saved successfully!")

                    elif user_choice == "2":
                        site = input("Enter site name: ")
                        retrieved_pwd = password_manager.retrieve_password(site)
                        if retrieved_pwd:
                            print(f"🔓 Retrieved Password for {site}: {retrieved_pwd}")
                        else:
                            print("❌ No password found!")

                    elif user_choice == "3":
                        length = int(input("Enter password length: "))
                        generator = PasswordGenerator(length)
                        print(f"🔑 Generated Password: {generator.generate()}")

                    elif user_choice == "4":
                        print("🔒 Logging out...\n")
                        break

                    else:
                        print("❌ Invalid choice! Please try again.")

        elif choice == "3":
            print("👋 Exiting Password Manager. Stay safe!")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
