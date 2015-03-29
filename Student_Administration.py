__author__ = 'liangdong'

all_students = ['Ellen', 'Sam', 'Victoria', 'Rachel', 'Austin']
all_majors = ['Information Library Science', 'English', 'Computer Science', 'History', 'Chemistry']

def main():
    # get the user's choice
    option = print_instructions()
    # if the user does not want to quit
    while option != 4:
        # if the user wants to add a student
        if option == 1:
            student_name = raw_input("What's the new student's name? ")
            student_major = raw_input("What's the new student's major? ")
            # if the major has already existed, it will not be added to the list
            if student_major in all_majors:
                print "Major: %s is already in the list. Please try again." % (student_major)
            # if the name has already existed, it will not be added to the list
            elif student_name in all_students:
                print "Name: %s is already in the list. Please try again." % (student_name)
            # if they are new name and major, add them to the lists
            else:
                all_students.append(student_name)
                all_majors.append(student_major)
                print "%s and %s have been added to the list." % (student_name, student_major)
        # if the user wants to print all students' names
        if option == 2:
            for name in all_students:
                print name
        # if the user wants to print all majors
        if option == 3:
            for major in all_majors:
                print major
        # if the user wants to look up a student's major by name
        if option == 0:
            student_name = raw_input("What's the new student's name? ")
            # if the name exists, get the index of it and use the index to find major
            if student_name in all_students:
                for sname in all_students:
                    if student_name == sname:
                        i = all_students.index(student_name)
                        result_major = all_majors[i]
                        print "%s's major is %s." % (sname, result_major)
            else :
                print "Sorry, %s does not exist." % (student_name)
        # keep prompting the user
        option = print_instructions()
    print "You've quitted."
    exit(0)

def print_instructions():
    # print instructions and get user's input
    print"\nPlease select an action:\n0. Look up a student's major by name\n1. Add a student\n2. Print all students\n3. Print all majors\n4. Quit\n"
    option = int(input("Please Choose an option: "))
    return option

main()
