
def check_withdraw_amount(amt):
    if(amt % 100 == 0):
        print(f"Dispensing {amount}")
    else:
        print("Invalid amount")

amount=int(input("Enter withdrawal amount:"))
check_withdraw_amount(amount)