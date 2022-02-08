class Atm(object):
    def __init__(self, atm_number, pin_number):
        self.atm_number= atm_number
        self.pin_number= pin_number

    def CheckBalance(self):
        balance = 100000000
        print('your balance is '+ str(balance))

    def CashWithdrawl(self, amount):
        new_balance= 100000000- amount
        print('you have withdrawn'+ str(amount)+'. Your new balance is ' + str(new_balance))

def main():
    cardNumber= input('insert your card number:')
    pinCode= input('insert your pin code:')

    newUser= Atm(cardNumber, pinCode)

    print('choose your activity')
    print('1. Balance Enquiry   2.Withdrawl')
    activity= int(input('enter activity code:'))

    if(activity==1):
        newUser.CheckBalance()
    elif(activity==2):
        amount= int(input('enter the amount to be withdrawn:'))
        newUser.CashWithdrawl(amount)
    else:
        print('please enter a valid number')

main()
