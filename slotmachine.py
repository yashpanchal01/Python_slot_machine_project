MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines")
        if lines.isdigit() and lines <= MAX_LINES:
            lines = int(amount)
            if lines > 0:
                break
            else:
                print("lines must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return lines 

def get_bet():
    while True:
        bet = input("How much money you want to bet? $")
        if bet.isdigit() and MIN_BET <= bet <= MAX_BET :
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return bet

def withdraw():
    pass 

def main():
    balance = deposit()
    if balance > 0:
        get_number_of_lines()
        get_bet()
        
