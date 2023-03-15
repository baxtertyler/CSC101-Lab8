# CPE 101-01
# LAB 8: File i/o
# Name: Tyler Baxter
# Section: 03

# main function that runs the code
# none -> none
def main():
    file_r = open('std_info.txt', 'r')
    lst = read_file(file_r)
    file_w = open('student_avg.txt', 'w')
    write_average(file_w, write_file(lst, file_w))


# reads the file and puts the values into a list
# text file -> nested list
def read_file(file_r):
    lst = file_r.readlines()
    lst_new = []
    for i in range(len(lst)):
        x = lst[i].split()
        lst_new.append([])
        lst_new[i].append(x[0] + " " + x[1])
        lst_new[i].append(x[2])
        lst_new[i].append(float(x[3]))
    file_r.close()
    return lst_new


# writes the information from the old file as well class averages on the new file
# text file, text file -> list
def write_file(in_file, out_file):
    ee_avg = cpe_avg = total_avg = ee_cnt = cpe_cnt = total_cnt = 0
    for i in range(len(in_file)):
        out_file.write(str(in_file[i][0]) + ' ' + str(in_file[i][1]) + ' ' + str(in_file[i][2]) + '\n')
        if in_file[i][1] == "EE":
            ee_avg += in_file[i][2]
            total_avg += in_file[i][2]
            ee_cnt += 1
        elif in_file[i][1] == "CPE":
            cpe_avg += in_file[i][2]
            total_avg += in_file[i][2]
            cpe_cnt += 1
        else:
            total_avg += in_file[i][2]
        total_cnt += 1
    return [ee_avg, ee_cnt, cpe_avg, cpe_cnt, total_avg, total_cnt]


# this function computes and prints the averages to the new text file
# text file, list -> none
def write_average(out_file, averages):
    out_file.write('....' + '\n')
    out_file.write("EE average = " + str(averages[0] / averages[1]) + '\n')
    out_file.write("CPE average = " + str(averages[2] / averages[3]) + '\n')
    out_file.write("Total average = " + str(averages[4] / averages[5]) + '\n')
    out_file.close()


if __name__ == '__main__':
    main()
