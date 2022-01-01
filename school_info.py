import csv


def entry2csv(listdata):
    # enters list data to csv file
    with open("student_data.csv", 'a', newline = '') as datafile:
        entry = csv.writer(datafile)
        if datafile.tell() == 0:
            entry.writerow(['Name', 'Age', 'Ph No.', 'Email ID'])
        entry.writerow(listdata)

def lwrcase(txt):
    # converting in lowercase
    txt_l = ""
    for i in txt:
        if (ord(i) >= 65 and ord(i) <= 90):
            txt_l = txt_l + chr(ord(i) + 32)
        else:
            txt_l = txt_l + i
    return txt_l

def numsuffix(num):
    # adding suffix to number
    nS = ""
    n_l = num % 10
    if num % 100 >= 11 and num % 100 <= 19:
        nS = str(num)+"th"
    elif n_l == 1:
        nS = str(num)+"st"
    elif n_l == 2:
        nS = str(num)+"nd"
    elif n_l == 3:
        nS = str(num)+"rd"
    else:
        nS = str(num)+"th"
    return nS

def inptverif(txt):
    # checking for blank inputs
    verif = False
    while(not verif):
        inpt = input(f"\t{str(txt)}\t: ")
        if inpt == "":
            print("Entry cannot be blank, Please enter valid info.")
            verif = False
        else:
            verif = True
            return inpt


if __name__ == '__main__':
    # Taking entries
    entr = True
    n = 1
    while(entr):
        # filling info
        print(f"\nEnter {numsuffix(int(n))} student's following information:")
        s_name = inptverif("Name\t")
        typ_chk = False
        while(not typ_chk):
            try:
                s_age = int(inptverif("Age (In years)"))
                typ_chk = True
            except ValueError:
                print("Age should be a Whole Number, Please enter valid info.")
                typ_chk = False
        s_ph = inptverif("Phone number")
        s_email = inptverif("Email ID")

        info_list = [s_name, s_age, s_ph, s_email]  # listing info

        # condition to check entry
        print("\nPlease verify the info:")
        print(f"\tName:\t\t{info_list[0]}\n\tAge:\t\t{info_list[1]}\n\tPhone Number:\t{info_list[2]}\n\tEmail ID:\t{info_list[3]}")
        try_chk = False
        while(not try_chk):
            chk = input("\nIs the entered info correct? (y/n): ")
            chk = lwrcase(chk)
            if chk == "y":
                entry2csv(info_list)
                print("\nEntry Uploaded!\n")
                # condition to ask next entry
                try_info = False
                while(not try_info):
                    nN = int(n + 1)
                    rep = input(f"\nWish to enter {numsuffix(nN)} student's info? (y/n): ")
                    rep = lwrcase(rep)
                    if rep == "y":
                        n += 1
                        try_info = True
                    elif rep == "n":
                        entr = False
                        try_info = True
                    else:
                        print("Wrong Input!")
                        try_info = False
                try_chk = True
            elif chk == "n":            
                try_chk = True
            else:
                print("Wrong Input!")
                try_chk = False
