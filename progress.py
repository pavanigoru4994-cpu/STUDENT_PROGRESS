student_info = {}
# calcluting grades
def calculate_grade(avg):
    if avg >= 90 and avg <101:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "FAIL !"
#generating remarks(())
def remarks_gen(grade, status):
    if status == "FAIL":
        return "You failed in one or more subjects. Focus more and improve."

    if grade == "A":
        return "Excellent performance! Keep it up."
    elif grade == "B":
        return "Good job! You can do even better."
    elif grade == "C":
        return "Average performance. Improve your weak subjects."
    elif grade == "D":
        return "You passed, but you need more improvement."
    else:
        return "Invalid marks."
# mark calculation()
def mark_calc(name, roll_no, branch):
    sn = int(input("ENTER NUMBER OF SUBJECTS :: "))

    marks = []
    for i in range(sn):
        marks.append(int(input(f"Enter marks for Subject {i+1}: ")))
# marks input from user (student)
    avg = sum(marks) / sn
    grade = calculate_grade(avg)
    status = "PASS" if min(marks) >= 35 else "FAIL"
    percent = int(avg)
    rmk = remarks_gen(grade, status)
    rmk ="invalid marks! " if max(marks) >100 else rmk
    student_info[roll_no] = {
        "std_name": name,
        "std_branch": branch,
        "marks": marks,
        "avrg": avg,
        "grade": grade,
        "status": status,
        "percent": percent,
        "maxm": max(marks),
        "minm": min(marks),
        "remarks": rmk
    }


#primary data of student
def student_data_collection():
    name = input("ENTER STUDENT NAME :: ")
    roll_no = input("ENTER STUDENT ROLL NUMBER :: ")
    branch = input("ENTER STUDENT BRANCH (AIDS / CSC / AIML / CSD / CSM):: ").upper()
    mark_calc(name, roll_no, branch)
# marks updating module
def up_marks(roll):
    if roll not in student_info:
        print("ROLL NUMBER NOT FOUND!")
        return

    print("\n++++++ MODIFY MARKS ++++++")

    marks = student_info[roll]["marks"]
    print("Old Marks:", marks)

    print("Enter new marks (press ENTER to keep old mark):")

    for i in range(len(marks)):
        new = input(f"Subject {i+1} new marks: ")
        if new != "":
            marks[i] = int(new)
    avg = sum(marks) / len(marks)
    grade = calculate_grade(avg)
    status = "PASS" if min(marks) >= 35 else "FAIL"
    percent = int(avg)
    rmk = remarks_gen(grade, status)

    student_info[roll]["marks"] = marks
    student_info[roll]["avrg"] = avg
    student_info[roll]["grade"] = grade
    student_info[roll]["status"] = status
    student_info[roll]["percent"] = percent
    student_info[roll]["maxm"] = max(marks)
    student_info[roll]["minm"] = min(marks)
    student_info[roll]["remarks"] = rmk

    print("\nMarks Updated Successfully!")
#-- student prograss report
def student_P_R(roll):
    if roll not in student_info:
        print("ROLL NUMBER NOT FOUND.")
        return

    data = student_info[roll]

    print("\n\n  _-+=================================================================+-_")
    print("-::|:-:                   STUDENT PROGRESS REPORT                   :-:|::-")
    print("   +===================================================================+")

    print("\nSTUDENT ROLL NUMBER  ::", roll)
    print("STUDENT NAME         ::", data["std_name"])
    print("STUDENT BRANCH       ::", data["std_branch"])
    print("STUDENT AVERAGE MARKS::", data["avrg"])
    print("STUDENT GRADE        ::", data["grade"])
    print("STUDENT STATUS       ::", data["status"])
    print("STUDENT PERCENTAGE   ::", data["percent"])
    print("MAX MARK             ::", data["maxm"])
    print("MIN MARK             ::", data["minm"])

    print("\n--- REMARKS ---")
    print(data["remarks"])

    print("\nSUBJECT MARKS:")
    for i, m in enumerate(data["marks"], 1):
        print(f"Subject {i}: {m}")

    print("\n===========================::  THE END of student report::==============================")



# THIS IS MAIN BLOCK
if __name__ == "__main__":
    print("+======================================+")
    print("|   STUDENT PROGRESS TRACKING SYSTEM   |")
    print("+======================================+")

    student_data_collection()
# MENU FOR STUDENT
    while True:
        print("\n============:     MENU     :===============")
        print("ENTER [ 1 ] NEW STUDENT ENROLLMENT")
        print("ENTER [ 2 ] SHOW STUDENT PROGRESS REPORT")
        print("ENTER [ 3 ] MODIFY MARKS")
        print("ENTER [ 4 ] EXIT")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            student_data_collection()

        elif choice == 2:
             roll = input("ENTER STUDENT ROLL NO :: ")
             student_P_R(roll)

        elif choice == 3:
            roll = input("ENTER YOUR ROLL NO TO MODIFY :: ")
            up_marks(roll)

        elif choice == 4:
            print("\nTHANK YOU FOR USING MY PROGRAM!")
            break

        else:
            print("INVALID OPTION. TRY AGAIN.")
     