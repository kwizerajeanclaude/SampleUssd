import cgi

form = cgi.FieldStorage()

sessionId = form.getvalue('sessionId')
serviceCode = form.getvalue('serviceCode')
phoneNumber = form.getvalue('phoneNumber')

text = form.getvalue('text')

if text == "":
    response = "CON What would you like to check\n"
    response += "1. My Account\n"
    response += "2. My Phone Number"

elif text == "1":
    response = "CON choose account information you want\n"
    response += "1. My Account no\n"
    response += "2. My Balance"

elif text == "2":
    response = "END your phone Number is " + phoneNumber

elif text == "*1*1":
    accountNumber = "AC00122"
    response = "END Your Acc is " + accountNumber

elif text == "*1*2":
    balance = 324555
    response = "END Your Balance is " + str(balance)

print("Content-type:text/plain")
print()
print(response)
