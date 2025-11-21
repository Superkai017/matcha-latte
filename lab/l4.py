import l3
def check_student_email():
    email = input("Enter your student email: ").strip()
    try:
        domain = l3.extact_domain(email)
        if domain.lower() == "student.univ.edu":
            print("verified student.")
        else:
            print("please use your university email.")
    except ValueError as e:
        print(e)
check_student_email()