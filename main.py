from hashlib import sha256
from getpass import getpass
password = getpass("password: ")
thing = input("thing: ")
password = password + thing
password = sha256(password.encode('utf-8')).hexdigest()
print('your password is: ' , password)
