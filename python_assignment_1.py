import json


def save_user_data(user_data, filename='user_data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(user_data)
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def load_user_data(filename='user_data.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []



def main():
    print("Choose an option:")
    print("1. Sign up")
    print("2. Sign in")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        mobile_number = input("Enter your mobile number: ")

        user_data = {
        "username": username,
        "password": password,
        "mobile_number": mobile_number
        }

        save_user_data(user_data)
        print("Sign up successful!")
        
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        users = load_user_data()

        for user in users:
            if user['username'] == username and user['password'] == password:
                print(f"Welcome to the device, {username}!")
                print(f"Your mobile number is: {user['mobile_number']}")
                return
    
        print("Incorrect credentials. Program terminated.")
    else:
        print("Invalid choice. Program terminated.")

if __name__ == "__main__":
    main()
