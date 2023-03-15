# CPE 101-01
# LAB 8: File i/o
# Name: Tyler Baxter
# Section: 03

# main function to run the other functions and open the file
# none -> none
def main():
    input_file = open('in.txt', 'r')
    list_info = read_file(input_file)
    print_info(list_info)


# reads through the file and creates a nested list with [[line #, line length, line)]]
# text file -> nested list
def read_file(f_name):
    lst = f_name.readlines()
    lst_new = []
    for i in range(len(lst)):
        lst_new.append([])
        lst_new[i].append(str(i + 1))
        lst_new[i].append(str(len(lst[i])))
        lst_new[i].append(str(lst[i]))
    f_name.close()
    return lst_new


# prints the information from the new created lst
# nested list -> none
def print_info(lst):
    for i in range(len(lst)):
        print("Line " + lst[i][0] + ": (" + lst[i][1] + " chars): " + lst[i][2], end = "")


if __name__ == '__main__':
    main()
