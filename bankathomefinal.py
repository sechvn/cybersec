# Eric Gimbel -- Huge thanks goes to my tutor Micheal P. who did a tremendous job of helping how to think and solve problems with code. Also, a huge thanks to Nick G. my brother for encouraging and motivating me with solid advice.
savings = 1000
checking = 1000

def currentAmount(savings, checking):   # Main function takes 2 arguments 

    print(f"Current Savings Amount: {savings}\nCurrent Checking Amount: {checking}" )
    user = input('Do you want to deposit, transfer, or withdraw: ')
    account = input('Which account do you want to choose to complete this transaction: ')
    

    if user == 'deposit':
        depositMoney(savings, checking, account)

    elif user == 'transfer':
        transfer(savings, checking, account)

    elif user == 'withdraw':
        withdrawMoney(savings, checking, account)
    elif user or account:
        print('Please enter correct values')
        currentAmount(savings, checking)

    
def transfer(savings, checking, account):   # Function with 3 arguments that tranfers money and error checks to ensure that more money isn't transferred than is in account.
    user = float(input('How much money would you like to tranfer: '))
    while user - savings or user - checking < 0:
        print('Insufficient funds, please transfer available amount')
        currentAmount(savings, checking)

    if account == 'savings':
        checking -= user
        savings += user
        currentAmount(savings, checking)
    elif account == 'checking':
        savings -= user
        checking += user
        currentAmount(savings, checking)

        
        

def depositMoney(savings, checking, account):   # Function with 3 argument for depositing money logic that adds money to each respective account done with if, elif statements.
    user = float(input('How much money would you like to deposit: '))
    if account == 'savings':
        savings += user
        currentAmount(savings, checking)
    elif account == 'checking':
        checking += user
        currentAmount(savings, checking)
    
        
        

def withdrawMoney(savings, checking, account):      #Funtion 3 arguments to handle the logic for withdrawing with error handled by while loop.
    user = float(input('How much money would you like to withdraw: '))
    while user - savings or user - checking < 0:
        print('Insufficient funds, please withdraw available amount')
        currentAmount(savings, checking)

    if account == 'savings':
        savings -= user
        currentAmount(savings, checking)
    elif account == 'checking':
        checking -= user
        currentAmount(savings, checking)
 
      
        
   
currentAmount(savings, checking)
		




