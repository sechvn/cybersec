# Eric Gimbel -- Huge thanks goes to my tutor Micheal P. who did a tremendous job of helping how to think and solve problems with code. Also, a huge thanks to Nick G. my brother for encouraging and motivating me with solid advice.
savings = 1000
checking = 1000

def currentAmount(savings, checking):
	print(f"Current Savings Amount: {savings}\nCurrent Checking Amount: {checking}" )
	user = input('Do you want to deposit, transfer, or withdraw: ')
	account = input('Which account do you want to choose to complete this transaction: ')
	
	if user == 'deposit':
		depositMoney(savings, checking, account)

	elif user == 'transfer':
		transfer(savings, checking, account)

	elif user == 'withdraw':
		withdrawMoney(savings, checking, account)

	else:		
		print('Please choose one of the options')
		currentAmount(savings, checking)

def transfer(savings, checking, account):
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

def depositMoney(savings, checking, account):
	user = float(input('How much money would you like to deposit: '))
	if account == 'savings':
		savings += user
		currentAmount(savings, checking)
	elif account == 'checking':
		checking += user
		currentAmount(savings, checking)

def withdrawMoney(savings, checking, account):
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
		




