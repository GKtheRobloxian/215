# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

goodUserAndPass = False

while (goodUserAndPass == False):
    user = input ("Username: ")
    password = input ("Password: ")
    if (len(list(user)) > 8 and len(list(user)) < 24 and len(list(password)) > 8 and len(list(user)) < 24):
        my_auth.set_authorization(user,password)
        goodUserAndPass = True

# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
