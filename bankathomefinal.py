# Eric Gimbel Final Bank at Home
savingsAccount = 1000.00
checkingAccount = 1000.00


def currentAmount(savings, checking):   # Main function takes 2 arguments 
    global savingsAccount
    global checkingAccount
    print(f"Current Savings Amount: {savingsAccount}\nCurrent Checking Amount: {checkingAccount}" )
    account = choiceCheck('Which account would you like to use: ')
    user = input('Do you want to deposit, transfer, withdraw, or quit: ')
    
    

    if user == 'deposit':
        depositMoney(savings, checking, account)

    elif user == 'transfer':
        transfer(savings, checking, account)

    elif user == 'withdraw':
        withdrawMoney(savings, checking, account)

    elif user == 'quit':
        return False

    else:
        print('Invalid Selection')


    return True
    
    
def transfer(savings, checking, account):   # Function with 3 arguments that tranfers money and error checks to ensure that more money isn't transferred than is in account.
    global savingsAccount
    global checkingAccount
    user = float(input('How much money would you like to tranfer into this account: '))

    if user > savingsAccount or user > checkingAccount:
        print('Insufficient funds')
        return transfer(savings, checking, account)

    elif account == 'savings':
        checkingAccount -= user
        savingsAccount += user
        currentAmount(savingsAccount, checkingAccount)

    elif account == 'checking':
        savingsAccount -= user
        checkingAccount += user
        currentAmount(savingsAccount, checkingAccount)

        
        

def depositMoney(savings, checking, account):
    global savingsAccount
    global checkingAccount   # Function with 3 argument for depositing money logic that adds money to each respective account done with if, elif statements.
    user = float(input('How much money would you like to deposit: '))

    if account == 'savings':
        savingsAccount += user
        currentAmount(savingsAccount, checkingAccount)

    elif account == 'checking':
        checkingAccount += user
        currentAmount(savingsAccount, checkingAccount)
    
        
        

def withdrawMoney(savings, checking, account):     #Funtion 3 arguments to handle the logic for withdrawing with error handled by if, elif. 
    global savingsAccount                          #Declared global variables for the function to work with. 
    global checkingAccount      
    user = float(input('How much money would you like to withdraw: '))

    if user > savingsAccount or user > checkingAccount:
        print('Insufficient funds')
        return withdrawMoney(savings, checking, account)

    elif account == 'savings':
        savingsAccount -= user
        currentAmount(savingsAccount, checkingAccount)

    elif account == 'checking':
        checkingAccount -= user
        currentAmount(savingsAccount, checkingAccount)   


def validChoice(account):
    return account == 'savings' or account == 'checking'

def choiceCheck(check):
    account = input(check)

    if(not validChoice(account)):
        print('Invalid account selection, please choose checking or savings.')
        return choiceCheck(check)

    return account




        
  
if (__name__ == '__main__'):

    while  currentAmount(savingsAccount, checkingAccount):
        pass

    print('Thank you, have a nice day!')






   
   
       # Calling main function with the 2 paramenters used within the function. As an example of my understanding of functions now
# if you wanted to start the user out with different amounts other than the established account variables outside the functions you could pass those values instead of savings and checking within the function.
        

# I used a tutor from Fiverr his name is Micheal P. and he got on a call with me and helped me think about how to solve
# this program's logic. He guided while I coded. He never gave me answers and honestly was the best thing I could do outside your help
# I was able to solve and think about programming in general differently after his help. We plan on continuing even after the semester is 
# over. Both the withdraw and transfer error handling was entirely done by myself using the our textbook. 
# I also did both functions by myself for the deposit and withdraw. He helped me with the logic initially for the main function 
# at the top. He specifically helped me to think how to look at the problem in a broader perspective and stop focusing so narrowly on 
# each section. Many of the things he said echoed what you have taught. He also said, that I have the tools but just am not confident on
# where and when to use them. I still need a lot of work and I tried putting in additional error checking for string and float errors that 
# occur if the user types different strings other than what is presented or types strings when it should be a dollar amount.
# Regrettably, I was behind and couldn't spend the time I wanted on it to figure that part out. I am still getting used to functions
# but I now understand those parameters can be anything but if you use arguments in a function than they need to be passed to the function once 
# it is called. I also learned how to call functions within functions which is was awesome as it provided a way to keep the program running. I do 
# there are more elegant and proper ways to do that with while loops for example and then object oriented programming with classes. But I am still a 
# huge work in progress however because of this class I am now more determined than ever to continue with programming and networking as the main areas
# to study when I have free time. Our plan is to pick a security related project that incorporates networking with python and work on it together.


