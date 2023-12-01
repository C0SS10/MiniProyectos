def check_user(txt):
    invalid_users = []
    for line in txt:
        id, username, email, age, location = line.strip().split(",")
        if is_valid(id, username, email, age, location):
            pass
        else:
            print(f"User {line} is invalid ❌")
            invalid_users.append(username[0])
    return invalid_users

def is_valid(id, username, email, age, location):
    if id.isalnum() and username.isalnum() and is_valid_email(email):
        if age.isdigit() or age == "":
            if location.isascii() or location == "":
                return True
    return False

def is_valid_email(email):
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    with open("message_05.txt", "r") as txt:
        txt = txt.readlines()
        invalid_users = check_user(txt)

    hidden_message = "".join(invalid_users)
    print(f"\nHidden Message: {hidden_message}")
