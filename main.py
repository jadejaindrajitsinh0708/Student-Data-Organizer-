print("Welcome to the  Student Data Orgnazer ")
print()
students = []
while True :
    print()
    print("Select an Opstion ")
    print("1 Add Student ")
    print("2 Show Student ")
    print("3 Update Student Information ")
    print("4 Remove Student ")
    print("5 Show Subject ")
    print("6 Exit ")
    print()

    choice = int(input("Enter Your Choice:-"))

    if choice == 1 :
        print()
        id = int(input("Enter Student ID:-"))
        name = input("Enter Student Name:-")
        age = int(input("Enter Student Age:-"))
        grade = input("Enter Student Grade:-")
        dob = input("Enter Date Of Birth (YYYY-MM-DD) :-")
        subject = input("Enter Subject (comma - separate):-")

        id_dob = (id,dob)
        s = set(subject.split(","))

        student_dict = {
            "name": name,
            "Age": age,
            "grade": grade,
            "subject": s,
            "info": id_dob
        }
        students.append(student_dict)
        print("Student Added Successfully !")

    elif choice == 2 :
        print()
        if len(students) != 0 :
            print("--- Student List ---")
            
            for std in students:
                print(f"Student Name is: {std['name']} | "
                      f"Student age is: {std['Age']} | "
                      f"Student Grade is: {std['grade']} | "
                      f"Student subjects: {std['subject']} | "
                      f"Student id {std['info'][0]} | "
                      f"Student dob {std['info'][1]}")
        else:
            print("Student Not Found ")

    elif choice == 3 :
        print()
        id = int(input("Enter Student ID:-"))
        for std in students :
            if std["info"][0] == id :
                while True :
                    print("\n1 Update Name")
                    print("2 Update Age ")
                    print("3 Update Subject")
                    print("4 Update Grade")
                    print("5 Stop Update ")

                    ch = int(input("Enter Your Choice:-"))

                    if ch == 1 :
                        name = input("New Name:-")
                        std["name"]= name
                        print("update successfully")

                    elif ch == 2 :
                        age = int(input("Update Age:-"))
                        std["Age"] = age
                        print("update successfully")

                    elif ch == 3 :
                        sub = input("New Subjects (comma - separate):-")
                        std["subject"] = set(sub.split(","))
                        print("update successfully")

                    elif ch == 4 :
                        grade = input("Update Grade:-")
                        std["grade"]= grade
                        print("update successfully")

                    elif ch == 5 :
                        print("exiting 🔚 ")
                        break
                    else :
                        print("Enter Valid Choice")
                break
        else :
            print("Student Data Not Found ")

    elif choice == 4 :
        print()
        if len(students) != 0 :
            id = int(input("Enter Student ID:-"))
            for std in students :
                if std["info"][0] == id :
                    students.remove(std)
                    print("Student Removed Successfully!")
                    break
            else:
                print("Student Not Found ")
        else:
            print("Data Not Found")

    elif choice == 5 :
        print()

        sett = set()
        for std in students:
            std_subject = std["subject"]
            for i in std_subject :
                sett.add(i)
        print("all subject ")
        for subject in sett  :
            print(subject)

     
             
    elif choice == 6 :
        print("Thank You For Using Student Data Organizer project ! ")
        break
