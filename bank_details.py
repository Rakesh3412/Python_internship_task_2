li=[]
def Bank():
	print("______________________Bank account creation ______________________\n")
	n=int(input("How many acoounts to create "))
	for i in range(n):
		ph_no=int(input("Enter phone number :"))
		add=input("Enter the address of bank :")
		adhar_no=int(input("Enter adhar number :"))
		pan_no=input("Enter pan number :")
		account_no=int(input("Enter account number :"))
		balance=500
		emp={"Bank_name":"SBI","Ifsc_code":"IFCA0214RB","phone_number":ph_no,"address":add,"adhar_no":adhar_no,"pan_no":pan_no,"account_no":account_no,"Balance":balance}
		li.append(emp)
		print("\n_______________________________Next person account details____________________________\n")
	print("___________________________________Bank book___________________________________________")
	print("_________________________________________________________________________________________________________________________________________________")
	print("Bank_name" "\t" "Ifsc_code" "\t" "Phone_number" "\t\t" "Address" "\t\t" "Adhar_no" "\t\t" "pan_no" "\t\t" "Account_no" "\t\t" "Balance" )
	print("_________________________________________________________________________________________________________________________________________________")
	for i in li:
		print(i["Bank_name"],"\t\t",i["Ifsc_code"],"\t\t",i["phone_number"],"\t\t",i["address"],"\t",i["adhar_no"],"\t",i["pan_no"],"\t\t",i["account_no"],"\t\t", i["Balance"] )
def deposit():
	print("_________________________Deposit_____________________________\n")
	acc=int(input("Select account "))
	for i in li:
		if acc == i["account_no"]  :
			amt=int(input("Enter amount to deposit "))
			i["Balance"]+=amt
		else:
			print("Account number invalid ")
def withdraw():
	print("_________________________Withdraw_____________________________\n")
	acc=int(input("Select account number "))
	for i in li:
		if acc == i["account_no"]:
			with_draw=int(input("Enter amount to withdraw: "))
			if with_draw<=i["Balance"]:
				print("Transaction successfull ")
				i["Balance"]-=with_draw
				print("current balance ")
				print(i["Balance"])
			else:
				print("Transaction faild ")
		else:
			print("Account number invalid ")

def check():
	print("________________________________Balance check______________________\n")
	acc=int(input("Select account number to check balance "))
	for i in li:
		if acc == i["account_no"]:
			print(i["Balance"])
	
print("______________________Menu____________________________________________\n")
print("Select options 1.account_creation 2.exit \n")
sel=int(input("Select which operation to form "))
if sel==1:
	Bank()  
	while True:
		print("Select options  1.deposit 2.withdraw 3.balance_check 4.exit \n")
		inp=int(input("Select which operation to form "))
		if inp==1:
			deposit()
		elif inp==2:
			withdraw()
		elif inp==3:
			check()
		elif inp==4:
			print("Thank you visit again ")
			break
elif sel==2:
	print("Thank you vist again")
	













	
	