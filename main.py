class Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print("Amount deposited.")
        else:
            print("Amount cannot be negative.")
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            print("Insufficient funds.")
    def check_amount(self):
        print(f"The amount in your account is ${self.__balance}")

def main():
        acc=Account("Prajwal Khatiwada",100)
        action=input("What would you like to do? D. Deposit, W. Withdraw, C. Check Balance\n").upper()
        if action=="D":
            d=int(input("What amount?"))
            acc.deposit(d)
        elif action=="W":
            w=int(input("What amount?"))
            acc.withdraw(w)
        elif action=="C":
            acc.check_amount()
        else:
            print("Invalid character.")
if __name__ == "__main__":
    main()
