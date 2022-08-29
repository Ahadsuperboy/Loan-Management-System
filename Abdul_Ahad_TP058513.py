# Abdul Ahad
# TP058513

# Importing Libraries
import datetime
import random

# Functions
# Main Menu
def mainmenu():
    print("\nWelcome to the Malaysia Bank Online Loan Management System")
    print("For New Customer, press 1")
    print("For Admin, press 2")
    print("For Registered Customer, press 3")
    print("To Exit, press 4")
    try:
        user_choice = int(input("Enter a choice: "))
    except ValueError:
        user_choice = 0
    return user_choice

# (1) New Customer
def new_customer():
    print("\nTo Check Loan Detail, press 1", )
    print("To Use Loan Calculator to check Loan Amount, press 2")
    print("Do Registration, press 3")
    print("Exit, press 4 ")
    try:
        new_customer_choice = int(input("Enter a choice: "))
    except ValueError:
        new_customer_choice = 0
    return new_customer_choice

# (2) Admin
def admin():
    print("\nShow the New Customer's Request, Give Approval,Unique Loan ID/Installment Date/Installment Amount press 1")
    print("Show Transaction of Specific Customer, press 2")
    print("Show Transaction of Specific Loan type , press 3")
    print("Show Transaction of All Customer, press 4")
    print("Show Transaction of All Types Loan, press 5")
    print("Exit, press 6")
    try:
        admin_control = int(input("Enter a choice: "))
    except ValueError:
        admin_control = 0
    return admin_control

# (3) Registered Customer
def registered_customer():
    print("\nCheck Loan Detail, press 1")
    print("Can pay loan installment, press 2")
    print("Can view the own transactions, press 3")
    print("Can check the status of Loan, press 4")
    print("Exit, press 5 ")
    try:
        customer_register = int(input("Enter a choice: "))
    except ValueError:
        customer_register = 0
    return customer_register

# (4) Exit Program
def exitprogram():
    print("Thank you Bye ")
    exit()

# 1(a) Loan Detail: It shows the Loan Requirements for all the 4 loan types.
def loan_detail():
    print("\nWhich type of loan detail you want to see")
    print("For Education Loan, press 1")
    print("For Car Loan, press 2")
    print("For Home Loan, press 3")
    print("For Personal Loan, press 4")
    try:
        loan_detail_choice = int(input("Enter a choice: "))
    except ValueError:
         loan_detail_choice = 0
    return loan_detail_choice

# 1(b) Education Loan Detail: Shows Loan Requirements for the Education Loan.
def education_loan_detail():
    print("Loan Eligibility: Malaysian Citizen \nFull-time students age between 18-25 years old ")
    print("Part-time students age between 18-35 years old")
    print("Loan Amount : Minimum 10000 RM, Maximum 5000000 RM")
    print("Interest Rate: 3.5%")
    print("Number of Year: 3-10")

# 1(c) Car Loan Detail: Shows Loan Requirements for the Car Loan.
def car_loan_detail():
    print("Loan Eligibility: Malaysian Citizen \nMinimum age between 21 to 30 years old \nMinimum Income: 10000 RM")
    print("Loan Amount : Minimum 9999 RM, Maximum 4000000 RM")
    print("Interest Rate: 3.4%")
    print("Number of Year: 1-9")

# 1(d) Home Loan Detail: Shows Loan Requirements for the Home Loan.
def home_loan_detail():
    print("Loan Eligibility: Malaysian Citizen \nMinimum age between 21 to 70 years old \nMinimum Income: 30000 RM")
    print("Loan Amount : Minimum 100000 RM, Maximum 349999 RM")
    print("Interest Rate: 4.55%")
    print("Number of Year: 5-35")

# 1(d) Personal Loan Detail: Shows Loan Requirements for the Personal Loan.
def personal_loan_detail():
    print("Loan Eligibility: Malaysian Citizen,Self-Employed")
    print("Minimum age between 21 to 58 years old \nMinimum Income: 24000 RM")
    print("Loan Amount : Minimum 2000 RM, Maximum 100000 RM")
    print("Interest Rate: 6.88%")
    print("Number of Year: 2-5")

# 1(e) Loan Calcu Ask: It asked user which type of loan they want to calculator.
def loan_calu_ask():
    print("\nWhich type of loan calculator you want to see")
    print("For Education Loan, press 1")
    print("For Car Loan, press 2")
    print("For Home Loan press 3")
    print("For Personal Loan press 4")
    try:
        loan_calu_choice = int(input("Enter a choice: "))
    except ValueError:
         loan_calu_choice = 0
    return loan_calu_choice

# 1(f) Education Loan: Calculate the Loan for Education loan type.
def education_loan():
    interest = 5.50
    no_of_year = 0

    while True:
            try:
                amount_taken = int(input("Enter the Amount taken as a loan: "))

            except ValueError:
                amount_taken = 0
                # return amount_taken
            if amount_taken >= 10000 and amount_taken < 5000000:
                pass
            else:
                print("The input is incorrect")
                continue

            try:
                no_of_year = int(input("Enter number of years to repay : "))
            except ValueError:
                no_of_year = 0
                # return no_of_year
            if no_of_year in range(5, 20):
                break
            else:
                print("The input is incorrect")
                continue

    # Total
    total_interest = interest / 100 * amount_taken * no_of_year

    monthly_loan_installment = (amount_taken + total_interest) / (no_of_year * 12)
    total_loan_installment = (amount_taken + total_interest)

    print("Total Amount is " + "{:.2f}".format(total_loan_installment), "RM")
    print("Monthly Repayment is " + "{:.2f}".format(monthly_loan_installment), "RM")
    return monthly_loan_installment, total_loan_installment

# 1(g) Education Loan: Calculate the Loan for Car loan type.
def car_loan():
    need_to_give = 0
    no_of_year = 0
    interest = 3.4

    while True:
        try:
            amount_taken = int(input("Enter the Amount taken as a loan: "))

        except ValueError:
            amount_taken = 0
            # return amount_taken
        if amount_taken > 9999 and amount_taken < 4000000:
            pass
        else:
            print("The input is incorrect")
            continue

        try:
            down_payment = int(input("Enter the Down Payment : "))

        except ValueError:
            down_payment = 0
            # return down_payment
        if down_payment >= 1000 and down_payment < 400000:
            pass
        else:
            print("The input is incorrect")
            continue

        # Substracing Both
        need_to_give = amount_taken - down_payment
        try:
            no_of_year = int(input("Enter number of years to repay : "))
        except ValueError:
            no_of_year = 0
            # return no_of_year
        if no_of_year in range(1, 10):
            break
        else:
            print("The input is incorrect")
            continue

    # Total
    total_interest = interest / 100 * need_to_give * no_of_year

    monthly_loan_installment = (need_to_give + total_interest) / (no_of_year * 12)
    total_loan_installment = (need_to_give + total_interest)
    print("Total Amount is " + "{:.2f}".format(total_loan_installment), "RM")
    print("Monthly Repayment is " + "{:.2f}".format(monthly_loan_installment), "RM")

    return monthly_loan_installment, total_loan_installment

# 1(h) Home Loan: Calculate the Loan for Home loan type.
def home_loan():
    interest = 4.55
    no_of_year = 0

    while True:
        try:
            amount_taken = int(input("Enter the Amount taken as a loan: "))

        except ValueError:
            amount_taken = 0
            # return amount_taken
        if amount_taken >= 100000 and amount_taken < 349999:
            pass
        else:
            print("The input is incorrect")
            continue

        try:
            no_of_year = int(input("Enter number of years to repay : "))
        except ValueError:
            no_of_year = 0
            # return no_of_year
        if no_of_year in range(5, 36):
            break
        else:
            print("The input is incorrect")
            continue

    # Total
    total_interest = interest / 100 * amount_taken * no_of_year

    monthly_loan_installment = (amount_taken + total_interest) / (no_of_year * 12)
    total_loan_installment = (amount_taken + total_interest)

    print("Total Amount is " + "{:.2f}".format(total_loan_installment), "RM")
    print("Monthly Repayment is " + "{:.2f}".format(monthly_loan_installment), "RM")
    return monthly_loan_installment, total_loan_installment

# 1(i) Personal Loan: Calculate the Loan for Personal loan type.
def personal_loan():
    interest = 6.88
    no_of_year = 0

    while True:
        try:
            amount_taken = int(input("Enter the Amount taken as a loan: "))

        except ValueError:
            amount_taken = 0
            # return amount_taken
        if amount_taken > 2000 and amount_taken < 100000:
            pass
        else:
            print("The input is incorrect")
            continue

        try:
            no_of_year = int(input("Enter number of years to repay : "))
        except ValueError:
            no_of_year = 0
            # return no_of_year
        if no_of_year in range(2, 6):
            break
        else:
            print("The input is incorrect")
            continue

    # Total
    total_interest = interest / 100 * amount_taken * no_of_year

    monthly_loan_installment = (amount_taken + total_interest) / (no_of_year * 12)
    total_loan_installment = (amount_taken + total_interest)

    print("Total Amount is " + "{:.2f}".format(total_loan_installment), "RM")
    print("Monthly Repayment is " + "{:.2f}".format(monthly_loan_installment), "RM")
    return monthly_loan_installment, total_loan_installment

# 1(j) Registration: It will ask user about their personal details for registration.
def registration():
    reg_file = open("Registration.txt", "a")

# Asking Details for registration
    fname = input("Enter your First Name: ").upper()
    lname = input("Enter your Last Name: ").upper()
    address = input("Enter the Address: ")
    email = input("Enter your Email ID: ")
    contact_no = input("Enter the Contact Number: ")
    gender = input("Enter your Gender: ").upper()
    date_of_birth = input("Enter your Date of Birth in format 'yy-mm-dd' : ")
    loan_type = input("Enter the Loan Type: ").upper()
    loan_terms = input ("Enter the Loan Years: ").upper()
    installment_amount = input("Enter the Installment Amount: ").upper()
    user_id = input("Enter your User ID: ").upper()
    pw = input("Enter password: ")
    reconfirm_pw = input("Rewrite the password for confirmation: ")

# Writing the details for registration
    reg_file.write(fname + " ")
    reg_file.write(lname + ",")
    reg_file.write(address + ",")
    reg_file.write(email + ",")
    reg_file.write(contact_no + ",")
    reg_file.write(gender + ",")
    reg_file.write(date_of_birth + ",")
    reg_file.write(loan_type + ",")
    reg_file.write(loan_terms + ",")
    reg_file.write(installment_amount + ",")
    reg_file.write(user_id + ",")
    reg_file.write(pw + ",")
    reg_file.write(reconfirm_pw )
    reg_file.write("\n")
    reg_file.close()
# Showing the details
    print(fname, lname)
    print(address)
    print(email)
    print(contact_no)
    print(gender)
    print(date_of_birth)
    print(loan_type + "LOAN")
    print(loan_terms + "YEARS")
    print(installment_amount + " RM ")

# 2(a) Admin Login: Used for the admin to login to the system.
def adminlogin():
    while True:
        username = input("Enter your username (Must be all capital letters) : ")
        pw = input("Enter the password: ")
        admincheck = False
        for line in open("admin.txt", "r").readlines():
            login_check = line.strip().split()
            if username == login_check[0] and pw == login_check[1]:
                if username.isupper():
                    print("Welcome Admin")
                    admincheck = True
                    break
        if admincheck:
            break
        else:
            print("Incorrect Details")
    return 1

# 2(b) New Customer Registration: Shows the people who have applied for the registration.
def new_Customer_req():
    new_customer_request = open("Registration.txt", "r")
    print("The Customers who have applied for registration with their details are :\n" + new_customer_request.read())
    approve_disapprove()
    new_customer_request.close()

# 2(c) Approve Disapprove: It asked the admin whether they want to approve registration requests one by one.
def approve_disapprove():
    print("\nIf you want to use Approve OR Disapprove Requests one by one enter the button, press 1")
    try:
        disa_appr = int(input("Enter a choice: "))
    except ValueError:
        disa_appr = 0
    return disa_appr

# 2(d) Unique Loan ID: Used to generate Special 8 Digit Unique Loan ID.
def unique_loan_id():
    from random import randint
    idloan= ""
    for i in range(8):
        idloan += str(randint(0,9))
    return idloan

# 2(e) Random Date: Used to generate Random Date.
def random_date():
    start_date = datetime.date(2021, 3, 15)
    end_date = datetime.date(2021, 12, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


# 2(f) Approval: It Approves or Disapprove the registration request and after approve/disapprove it shows their details in approved/disapproved customer text file.
def approval():
    new_customer_request = open("Registration.txt", "r")
    approving = open("approvedcustomer.txt", "a")
    disapproving = open("disapprovedcustomer.txt", "a")
    countapp = 0
    countdis = 0
    for line in new_customer_request.readlines():
        print(line)
        print("To Approve and Provide Education Loan Installment, Press 1")
        print("To Approve and Provide Car Loan Installment, Press 2")
        print("To Approve and Provide Home Loan Installment, Press 3")
        print("To Approve and Provide Personal Loan Installment, Press 4")
        print("To Disapprove Press 5")
        print("To Skip Press 6")
        try:
            decision = int(input("Enter your decision: "))

            if decision == 1:
                countapp += 1
                approving.write(str("Approve Customer") + str(countapp) + str(": ") + str(line) + str(" ") + str(unique_loan_id()) + str(" ") + str(random_date()) + str(" ") + str(education_loan()) +str(" RM") +str("\n"))
                new_customer_request.read()
            elif decision == 2:
                countapp += 1
                approving.write(str("Approve Customer") + str(countapp) + str(": ") + str(line) + str(" ") + str(unique_loan_id()) + str(" ") + str(random_date()) + str(" ") + str(car_loan())+ str(" RM") + str("\n"))
                new_customer_request.read()
            elif decision == 3:
                countapp += 1
                approving.write(str("Approve Customer") + str(countapp) + str(": ") + str(line) + str(" ") + str(unique_loan_id()) + str(" ") + str(random_date()) + str(" ") + str(home_loan()) + str(" RM") + str("\n"))
                new_customer_request.read()
            elif decision == 4:
                countapp += 1
                approving.write(str("Approve Customer") + str(countapp) + str(": ") + str(line) + str(" ") + str(unique_loan_id()) + str(" ") + str(random_date()) + str(" ") + str(personal_loan()) + str(" RM") + str("\n"))
                new_customer_request.read()
            elif decision == 5:
                countdis += 1
                disapproving.write(str("DisApprove Customer") + str(countdis) + str(": ") + str(line))
                new_customer_request.read()
            elif decision == 6:
                print("Skipped")
        except ValueError:
            decision = 0
            return decision

    new_customer_request.close()
    approving.close()
    disapproving.close()

# 2(g) Transaction of Specific Customer: Shows transaction of specific customer by asking their ID.
def transactionspecificcustomer():

    transspecicusto = open("customer_transactions.txt", "r")
    try:
        id = input("Enter the Customer ID: ")
        checking = transspecicusto.readlines()
        for word in checking:
            checkz = word.strip().split()
            if id == checkz[0]:
                print(word)
    except ValueError:
        id = 0
        return id
    transspecicusto.close()

# 2(h) Transaction of Specific Loan: Shows transaction of specific customer by asking Loan Type.
def transactionspecificloantype():
    transspeciloan = open("customer_transactions.txt", "r")
    try:
        name = input("Enter the Loan Type(First Word Capital): ")
        checking = transspeciloan.readlines()
        for word in checking:
            checkz = word.strip().split()
            if name == checkz[2]:
                print(word)
    except ValueError:
        name = 0
        return name
    transspeciloan.close()

# 2(i) Transaction of All Customer and Loan: Shows all the transaction of Both Customer and Loan Type.
def alltransactions_customer_loan():
    custo_loan_trans_all = open("customer_transactions.txt", "r")
    checking = custo_loan_trans_all.read()
    print("\n" + checking )
    custo_loan_trans_all.close()


# 3(a) User Login New: Used for the registered customer to login.
def userloginnew():
    while True:
        username = input("Enter your username (Must be all capital letters) : ")
        pw = input("Enter the password (First Alphabet Capital) : ")
        adminchecking = False
        for line in open("userlogindetail.txt", "r").readlines():
            login_check = line.strip().split()
            if username == login_check[0] and pw == login_check[1]:
                if username.isupper():
                    print("Welcome User")
                    adminchecking = True
                    break
        if adminchecking:
            break
        else:
            print("Incorrect Details")
    return 1, username

# 3(b) Registered Customer Details Check: Shows the details of registered customer.
def registered_customer_detail_check(username1):
    while True:
        reg_custo_check_detail = open("registeredcustomer.txt", "r")

        detail_check = False
        for line in reg_custo_check_detail.readlines():
            check = line.strip().split(",")
            if username1 == check[9]:
                print(check)
                detail_check = True
                break
        if detail_check:
            break
        else:
            print("Incorrect Details")
            break
    reg_custo_check_detail.close()

# 3(c) Loan Installment Pay: Used for register customer to pay their loan by putting their details.
def loan_installments_pay(username1):
    while True:
        paying_installment = open("testing_details.txt", "r")
        payment_history = open("customer_transactions.txt ", "a")

        loanid = (input("Enter your 8 Digit Loan ID: "))
        loantype = (input("Enter the Loan Type: "))
        amounttopay = (input("Enter the Amount to pay: "))
        installpaydate = input("Enter the Installment date: yy-mm-dd: ")

        detail_check = False

        for line in paying_installment.readlines():
            check = line.strip().split()

            if loanid == check[1]:
                print("Loan ID Exist")
                detail_check = True
                payment_history.write(str("\n") + str(username1) + " " + str(loanid) + " " + str(loantype) + " " + str(amounttopay) + "RM " + "Paid " + str(installpaydate))
                paying_installment.read()
                break
        if detail_check:
            break
        else:
            print("Incorrect Details")
            break
    paying_installment.close()
    payment_history.close()

# 3(d) Customer View Transactions: Registered Customer can see their all transactions
def customer_view_transactions(username1):
    while True:
        view_transactions = open("customer_transactions.txt", "r")

        detail_check = False
        for line in view_transactions.readlines():
            check = line.strip().split()
            if username1 == check[0]:
                print(check)
                detail_check = True
                break
        if detail_check:
            break
        else:
            print("Incorrect Details")

        view_transactions.close()

# 3(e) Loan Status: Used to show the loan status for registered customer.
def loan_status(username1):
    while True:
        view_loan_status = open("loan_status.txt", "r")

        detail_check = False
        for line in view_loan_status.readlines():
            check = line.strip().split(",")
            if username1 == check[0]:
                print(check)
                detail_check = True
                break
        if detail_check:
            break
        else:
            print("Incorrect Details")

        view_loan_status.close()

# New Customer Menu
def mainmenuall():
    while True:
        user_choice = mainmenu()
        if user_choice == 1:
            while True:
                user_choice1 = new_customer()
                if user_choice1 == 1:
                    loan_detail_choice1 = loan_detail()
                    if loan_detail_choice1 == 1:
                        education_loan_detail()
                    elif loan_detail_choice1 == 2:
                        car_loan_detail()
                    elif loan_detail_choice1 == 3:
                        home_loan_detail()
                    elif loan_detail_choice1 == 4:
                        personal_loan_detail()
                elif user_choice1 == 2:
                    loan_calu_choice1 = loan_calu_ask()
                    if loan_calu_choice1 == 1:
                        education_loan()
                    elif loan_calu_choice1 == 2:
                        car_loan()
                    elif loan_calu_choice1 == 3:
                        home_loan()
                    elif loan_calu_choice1 == 4:
                        personal_loan()
                elif user_choice1 == 3:
                    registration()
                    print("Congratulations ! Your Registration is Complete", )
                elif user_choice1 == 4:
                    exitprogram()
                    break

    # Admin Menu
        if user_choice == 2:
            user_choice1 = adminlogin()
            while True:
                user_choice2 = admin()
                if user_choice1 == 1:
                    if user_choice2 == 1:
                        new_Customer_req()
                        if user_choice2 == 1:
                            approval()
                    elif user_choice2 == 2:
                        transactionspecificcustomer()
                    elif user_choice2 == 3:
                        transactionspecificloantype()
                    elif user_choice2 == 4:
                        alltransactions_customer_loan()
                    elif user_choice2 == 5:
                        alltransactions_customer_loan()
                    elif user_choice2 == 6:
                        exitprogram()
                        break

    # Register Customer Menu
        if user_choice == 3:
            user_choice1, useriddd = userloginnew()
            while True:
                user_choice2 = registered_customer()
                if user_choice1 == 1:
                    if user_choice2 == 1:
                        registered_customer_detail_check(useriddd)
                    elif user_choice2 == 2:
                        loan_installments_pay(useriddd)
                    elif user_choice2 == 3:
                        customer_view_transactions(useriddd)
                    elif user_choice2 == 4:
                        loan_status(useriddd)
                    elif user_choice2 == 5:
                        exitprogram()
                        break
    # Exit Menu
        if user_choice == 4:
                exitprogram()
mainmenuall()
