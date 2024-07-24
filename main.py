import hashlib
import maskpass

logpath = 'C:\\Users\\avilu\\PycharmProjects\\PassManager\\logins'
passpath = 'C:\\Users\\avilu\\PycharmProjects\\PassManager\\pass\\passwords-'

def hash_string(s):                                              #hash encryption
    return hashlib.sha256(s.encode()).hexdigest()

def enter(passpath, user):                                       #user has entered filesystem
    while True:
        print("[1]Enter")
        print("[2]Find")
        print("[3]Exit")
        x = input('>')
        if x == '1':
            print("Name of Entry")
            name = input(">")
            print("Password")
            passw = input(">")
            entry = "*" + name + '*' + user + '*' + passw         #hash
            with open(passpath + user, 'a') as f:
                f.write(entry)
        elif x == '2':
            try:
                with open(passpath + user, 'r') as f:
                    y = f.readlines()
                y = ''.join(y)
                position = y.split("*")
                print("Name of Entry")
                i = input(">")
                if i in position:
                    index = position.index(i)
                    print('Username: ' + position[index + 1])
                    print('Password: ' + position[index + 2])
                else:
                    print("Invalid Entry")
            except FileNotFoundError:
                print("No entries found for this user.")
        elif x == '3':
            signinthing(passpath)
            break
        else:
            print("Invalid option, please try again.")

def signin(position, passpath):
    print("Enter Username")
    user = input(">")
    user_hash = hash_string(user)
    print("Enter Password")
    p = maskpass.askpass(prompt='>')
    pass_hash = hash_string(p)

    for i in range(len(position)):                              #cycle through all known users untill match/no match
        if position[i] == user_hash:
            if position[i + 1] == pass_hash:                    #check if the inputed pass is == to pass next to entered usersnames location
                print("Signed in As " + user)
                enter(passpath, user_hash)
                return
            else:
                print("Log in Incorrect")                       #failed
                signinthing(position)
                return
        i += 2
    print("Log In Incorrect")
    signinthing(position)

def signinthing(passpath):
    while True:
        print('[1]Sign in')
        print('[2]Register')
        question = input(">").lower()

        if question == '2':                                     #register
            print("Enter a New Username")
            user = input('>')
            print("Enter a New Password")
            passw = maskpass.askpass(prompt='>')
            user_hash = hash_string(user)
            pass_hash = hash_string(passw)
            entry = "*" + user_hash + '*' + pass_hash
            with open(logpath, 'a') as f:
                f.write(entry)
            with open(passpath + user_hash, 'a') as f:          #prob bc not always used but idk(figure out lated)(possibly no workie :()
                pass
            with open(logpath, 'r') as f:
                position = f.read().split("*")                  #prob bc not always used but idk(figure out later)
            signinthing(passpath)
            break
        elif question == "1":                                   #sign in
            with open(logpath, 'r') as f:
                position = f.read().split("*")
            signin(position, passpath)
            break
        else:
            print('Invalid Value')

signinthing(passpath)

#to do: rego over code logic, encrypt users user'/pass', interface?, finish making comments explaining code(dont overdo), figure out issue with making users and pass', add delays

