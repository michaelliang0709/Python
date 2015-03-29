__author__ = 'liangdong'

def main():
    file_name = raw_input("Enter the name of your file: ")
    file = open(file_name, "r")
    # read the file line by line
    file_contents = file.readlines()
    num_of_uppercase = num_of_lowercase = num_of_digits = num_of_whitespace = num_of_lines = 0
    # loop through each line of the file
    for line in file_contents:
        # count the number of lines
        num_of_lines+=1
        # loop through each character of each line
        for char in line:
            if char.isupper():
                # count the number of uppercase letters
                num_of_uppercase += 1
            if char.islower():
                # count the number of lowercase letters
                num_of_lowercase += 1
            if char.isdigit():
                # count the number of digits
                num_of_digits += 1
            if char == " " or char == "\t" or char == "\n":
                # count the number of whitespace characters
                num_of_whitespace += 1
    file.close()
    print "Uppercase count: %d" % (num_of_uppercase)
    print "Lowercase count: %d" % (num_of_lowercase)
    print "Digit count: %d" % (num_of_digits)
    # each line contains a "\n" except the last line
    print "Space count: %d" % (num_of_whitespace + num_of_lines - 1)

main()
