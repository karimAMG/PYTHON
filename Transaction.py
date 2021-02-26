import platform
# varables
discount = 0
interest = 0
down = 0
balance = 0
totalass = 0
change = 0
units = 0
rate = 0
athfee = 0
libfee = 0
labfee = 0
idfee = 0
uniform = 0
others = 0
cash = 0
courseN = ""
genderV = ""
reRun = 'Y'
mop = True
genderChckr = True

print (''.join(['-' for a in range(1, 41)]))
print("\n                 Reyna's \n")
print("            Enrollment System\n")
print (''.join(['-' for a in range(1, 41)]))
while(reRun == 'Y' or reRun == 'y'):  # for another enrollees
    try:
        studno = int(input('\nStudent No.: '))
    except:
        print ('[X] Only Numbers. Try Again !')
        try:
            studno = int(input('\nStudent No.: '))
        except:
            print ('[X] Only Numbers. Good Luck Next Time ;)')
            exit()
    if int(platform.python_version_tuple()[0]) == 2:
        studname = raw_input('Student Name: ')
    elif int(platform.python_version_tuple()[0]) == 3:
        studname = input('Student Name: ')
    print("\nAvailable Courses:")
    print(" [A] BSIT")
    print(" [B] BSIS")
    print(" [C] BSCS")
    print(" [D] BS Stat")
    print(" [E] BS Mathematics")
    print(" [F] BS Biology")
    print(" [G] BS Forestry")
    print(" [H] BS Geology")
    print(" [I] BS Physics")
    print(" [J] BS Applied Math")
    if int(platform.python_version_tuple()[0]) == 2:
        course = raw_input('\nYour Choosen Course: ').upper()
    elif int(platform.python_version_tuple()[0]) == 3:
        course = input('\nYour Choosen Course: ').upper()
    def switch(course):
        if course == 'A':
            units = 10
            rate = 1250
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 600
            uniform = 1500
            others = 2500
            courseN = "BSIT"
        elif course == 'B':
            units = 12
            rate = 1110
            athfee = 550
            libfee = 350
            labfee = 950
            idfee = 800
            uniform = 1300
            others = 2500
            courseN = "BSIS"
        elif course == 'C':
            units = 13
            rate = 1550
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 500
            uniform = 1400
            others = 2500
            courseN = "BSCS"
        elif course == 'D':
            units = 12
            rate = 1750
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 600
            uniform = 1500
            others = 2500
            courseN = "BS Stat"
        elif course == 'E':
            units = 11
            rate = 1250
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 600
            uniform = 1500
            others = 2500
            courseN = "BS Mathematics"
        elif course == 'F':
            units = 14
            rate = 1250
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 600
            uniform = 1500
            others = 2500
            courseN = "BS Biology"
        elif course == 'G':
            units = 14
            rate = 1250
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 680
            uniform = 2400
            others = 2500
            courseN = "BS Forestry"
        elif course == 'H':
            units = 15
            rate = 1350
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 690
            uniform = 1250
            others = 2500
            courseN = "BS Geology"
        elif course == 'I':
            units = 13
            rate = 1110
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 640
            uniform = 1450
            others = 2500
            courseN = "BS Physics"
        elif course == 'J':
            units = 15
            rate = 1250
            athfee = 500
            libfee = 350
            labfee = 850
            idfee = 600
            uniform = 1200
            others = 2500
            courseN = "BS Applied Math"
        else:
            print("[X] Invalid choice\n")
            exit()
    switch(course)
    print("\nYear Level: ")
    print(" [1]")
    print(" [2]")
    print(" [3]")
    print(" [4]")
    try:
        yrlevel = int(input(': '))
    except:
        print ('[X] Only Numbers. Try Again !')
        try :
            yrlevel = int(input(': '))
        except:
            print ('[X] Only Numbers. Good luck next time ;)')
            exit()
    print (''.join(['_' for a in range(1, 41)]))
    if int(platform.python_version_tuple()[0]) == 2:
        address = raw_input('\n\nAddress: ')
        bday = raw_input('Birthday: ')
    elif int(platform.python_version_tuple()[0]) == 3:
        address = input('\n\nAddress: ')
        bday = input('Birthday: ')
    while(genderChckr):
            if int(platform.python_version_tuple()[0]) == 2:
                gender = raw_input('Gender(M/F): ')
            elif int(platform.python_version_tuple()[0]) == 3:
                gender = input('Gender(M/F): ')
            if (gender == 'M' or gender == 'm'):
                genderV = "Male"
                genderChckr = False
            elif (gender == 'F' or gender == 'f'):
                genderV = "Female"
                genderChckr = False
            else:
                print("[Gender mismatch, try again]")
    if int(platform.python_version_tuple()[0]) == 2:
        contact = raw_input('Contact: ')
        email = raw_input('Email Address: ')
    elif int(platform.python_version_tuple()[0]) == 3:
        contact = input('Contact: ')
        email = input('Email Address: ')
    if '@' not in email:
        print ('[X] email Not Valid. Try Again')
        if int(platform.python_version_tuple()[0]) == 2:
            email = raw_input('Email Address: ')
        elif int(platform.python_version_tuple()[0]) == 3:
            email = input('Email Address: ')
        if '@' not in email:
            print ('[X] email Not Valid. Good Luck Next Time ;)')
            exit()
    if int(platform.python_version_tuple()[0]) == 2:
        mother = raw_input('Mother: ')
        father = raw_input('Father: ')
    elif int(platform.python_version_tuple()[0]) == 3:
        mother = input('Mother: ')
        father = input('Father: ')
    tuition = units * rate
    mscfee = labfee + libfee + athfee + idfee + uniform + others
    total = mscfee + tuition
    print (''.join(['=' for a in range(1, 41)]))
    print("\n\nStudent No.: " + str(studno))
    print("Student Name: " + studname)
    print("Course: " + str(courseN) + " | Year Level: " + str(yrlevel))
    print (''.join(['_' for a in range(1, 41)]))
    print("\n\nAddress: " + str(address))
    print("Birthday: " + str(bday) + " | Gender: " + genderV)
    print("Contact: " + str(contact))
    print("Email Address: " + email)
    print("Mother: " + mother)
    print("Father: " + father)
    print("\n   [Assessment]")
    print (''.join(['_' for a in range(1, 41)]))
    print("\n\nNo. of Units: " + str(units) + " | Rate Per Unit:" + str(rate))
    print("Tuition Fee: " + str(tuition))
    print("Athletic Fee: " + str(athfee) + " | Library Fee: " + str(libfee))
    print("Laboratory Fee: " + str(labfee))
    print("ID Fee: " + str(idfee) + " Uniform: " + str(uniform))
    print("Others: " + str(others))
    print("Misceleneous Fee: " + str(mscfee))
    print("Total: " + str(total))
    print (''.join(['_' for a in range(1, 41)]))
    while(mop == True):
        print("\n\n('C' - Cash , 'I' - Installment)")
        if int(platform.python_version_tuple()[0]) == 2:
            modeofpayment = raw_input('Payment: ')
        elif int(platform.python_version_tuple()[0]) == 3:
            modeofpayment = input('Payment: ')
        if ((modeofpayment == 'C') or (modeofpayment == 'c')):
            discount = tuition * .10
            interest = 0
            down = 0
            totalass = tuition - discount + mscfee
            balance = 0
            try:
                cash = int(input('Cash: '))
            except:
                print ('[X] Only Numbers. Try Again !')
                try:
                    cash = int(input('Cash: '))
                except:
                    print ('[X] Only Numbers. Good luck next time ;)')
                    exit()
            change = cash - totalass
            mop = False
        elif((modeofpayment == 'I') or (modeofpayment == 'i')):
            discount = 0
            interest = tuition * .5
            down = tuition * .50
            totalass = tuition + interest + mscfee
            balance = totalass - down
            try:
                cash = int(input('Cash: '))
            except:
                print ('[X] Only Numbers. Try Again !')
                try:
                    cash = int(input('Cash: '))
                except:
                    print ('[X] Only Numbers. Good luck next time ;)')
                    exit()
            change = cash - totalass
            mop = False
        else:
            print("Invalid choice")
    print("Discount(10%): " + str(discount))
    print("Interest(5%): " + str(interest))
    print("Downpayment: " + str(down))
    print("Total assessment: " + str(totalass))
    print("Balance: " + str(balance))
    print("Cash Tendered: " + str(cash) + " | Change: " + str(change))
    if int(platform.python_version_tuple()[0]) == 2:
        reRun = raw_input('\n\nAnother Transaction? (Y/N): ')
    elif int(platform.python_version_tuple()[0]) == 3:
        reRun = input('\n\nAnother Transaction? (Y/N): ')
