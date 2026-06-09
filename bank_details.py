li=[]
ph_num=[]
adh_no=[]
pan_noo=[]
acc_no=[]
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
		if ph_no in ph_num:
			print("number is already is existed ")
		elif adhar_no in adh_no:
			print("adhar no is existed ")
		elif account_no in acc_no:
			print("account number is existed ")
		elif pan_no in pan_noo:
			print("pan number is existed ")
		else:
			emp={"Bank_name":"SBI","Ifsc_code":"IFCA0214RB","phone_number":ph_no,"address":add,"adhar_no":adhar_no,"pan_no":pan_no,"account_no":account_no,"Balance":balance}
			li.append(emp)
			for j in li:
				ph_num.append(j["phone_number"])
				adh_no.append(j["adhar_no"])
				pan_noo.append(j["pan_no"])
				acc_no.append(j["account_no"])
			print("___________________________________Bank book___________________________________________")
			print("_________________________________________________________________________________________________________________________________________________")
			print(f"{'BANK NAME':<10} | {'IFSC CODE':<15} | {'PHONE NUMBER':<12} | {'ADDRESS':<15} | {'ADHAR NO':<12} | {'PAN NO':<12} | {'ACCOUNT NO':<10} | {'BALANCE':<10}")
			print("_________________________________________________________________________________________________________________________________________________")
			for i in li:
				print(f"{i['Bank_name']:<10} | {i['Ifsc_code']:<15} | {i['phone_number']:<12} | {i['address']:<15} | {i['adhar_no']:<12} | {i['pan_no']:<12} | {i['account_no']:<10} | {i['Balance']:<10}" )
def deposit():
	print("_________________________Deposit_____________________________\n")
	acc=int(input("Select account number: "))
	if acc in acc_no:
		print("valid account number ")
	else:
		print("Invalid account number ")

	for i in li:
		if acc == i["account_no"]  :
			amt=float(input("Enter amount to deposit must be positive "))
			if amt>0:
				i["Balance"]+=amt
			else:
				print("amt cannot be negative ")
def withdraw():
	print("_________________________Withdraw_____________________________\n")
	acc=int(input("Select account number "))
	if acc in acc_no:
		print("valid account number ")
	else:
		print("Invalid account number ")
	for i in li:
		if acc == i["account_no"]:
			with_draw=float(input("Enter amount to withdraw must be positive : "))
			if with_draw>0:
				if with_draw<=i["Balance"]:
					print("Transaction successfull ")
					i["Balance"]-=with_draw
					print("current balance ")
					print(i["Balance"])
				else:
					print("Transaction faield ")
			else:
				print("amount cannot be negative ")
def check():
	print("________________________________Balance check______________________\n")
	acc=int(input("Select account number to check balance :"))
	if acc in acc_no:
		print("valid account number ")
	else:
		print("Invalid account number ")
	for i in li:
		if acc == i["account_no"]:
			print(i["Balance"])	
print("______________________Menu____________________________________________\n")
print("\nSelect options 1.account_creation 2.exit \n")
sel=int(input("Select which operation to form "))
if sel==1:
	Bank()  
	while True:
		print("\nSelect options  1.deposit 2.withdraw 3.balance_check 4.exit \n")
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
		else:
			print("Invalid")
			break
elif sel==2:
	print("Thank you vist again")
else:
	print("Invalid choice ")
	













	
	