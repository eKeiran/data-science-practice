def cal_cgpa():
    allsem = int(input("\nEnter the number of total semesters: "))
    cgpa = 0
    sgpa_sum = 0
    for i in range(allsem):
        sg = float(input("Enter SGPA for semester {}: ".format(i + 1)))
        sgpa_sum += sg
    cgpa = sgpa_sum / allsem
    print("Your CGPA is:", cgpa)
    input()
def calculate_sgpa():
    num_subjects = int(input("Enter the number of subjects: ")) # Total number of subjects
    total_credits = 0
    total_weighted_grade = 0

    # Taking input for each subject
    for i in range(num_subjects):
        credit = int(input("\nEnter credits for subject {}: ".format(i + 1)))
        grade = float(input("Enter grade point (1-10) for subject {}: ".format(i + 1)))
        total_credits += credit
        total_weighted_grade += credit * grade

    sgpa = total_weighted_grade / total_credits
    print("Your SGPA is:", sgpa)
    input()
print("1. CGPA calculation")
print("2. SGPA calculation")
ch = int(input("\nEnter your choice: "))

if ch == 1:
    cal_cgpa()
elif ch == 2:
    calculate_sgpa()
else:
    print("\nError!")
