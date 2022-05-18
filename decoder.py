import re
import string

from cipher import FileDecoder

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " \n"

def main():
    print("Welcome To The Ferry Terminal Decoder")
    print("At any time you wish to exit the program enter: q\n")
    
    filename = get_file()
    password = get_pass()
    decoded_file = FileDecoder(password,filename,alphabet)


    delay_entries = [['Jan',0,0],['Feb',0,0],['Mar',0,0],['Apr',0,0],
                     ['May',0,0],['Jun',0,0],['Jul',0,0],['Aug',0,0],
                     ['Sep',0,0],['Oct',0,0],['Nov',0,0],['Dec',0,0]]

    startData = False
    for line in decoded_file:   
        if(startData==True):
            dataTab = line.split(',')
            if((dataTab[4] == dataTab[9]) and (dataTab[5] == dataTab[10])):
                hour_expected = int(dataTab[6])
                hour_departed = int(dataTab[11])
                hour_diff     = hour_departed - hour_expected
                
                min_expected = int(dataTab[7])
                min_departed = int(dataTab[12])
                min_diff     = min_departed - min_expected

                if(hour_diff > 0 or min_diff > 0):
                    entry = int(dataTab[4]) - 1
                    delay_entries[entry][1] = delay_entries[entry][1] + (hour_diff * 60) + (min_diff)
                    delay_entries[entry][2] = delay_entries[entry][2] + 1
                else:
                    entry = int(dataTab[4]) - 1
                    delay_entries[entry][2] = delay_entries[entry][2] + 1
        
        startData = True

    print("RESULTS")
    print(decoded_file)
    out_print(delay_entries)
    print("Lines - " + str(len(decoded_file)))
    print("END")
                

            
def get_file():
    passed = False
    while(passed==False):
        try:
            file = input("What is the filename you wish to decode: ")
            if(file == 'q'):
                exit()
            open(file,"r")
            return file
        except FileNotFoundError:
            print("Could not find file - Enter a valid filename")


def get_pass():
    len_pass_pat     = r'^.{6,8}$'
    capital_pass_pat = r'^.*[A-Z].*$'
    digit_pass_pat   = r'^.*\d.*\d.*$'
    special_pass_pat = r'^[^\!\@\#\$\&\*\-\_\.]*[\!\@\#\$\&\*\-\_\.][^\!\@\#\$\&\*\-\_\.]*[\!\@\#\$\&\*\-\_\.][^\!\@\#\$\&\*\-\_\.]*$'
    passed = False
    while(passed==False):
        password = input("Enter Password: ")
        if (password == 'q'):
            exit()
        
        if(re.match(len_pass_pat,password) and re.match(capital_pass_pat,password) and re.match(digit_pass_pat,password) and re.match(special_pass_pat,password)):
            return password
        else:
            print("Please enter a valid password ...")

def out_print(delay_entries):
    for month in delay_entries:
        if(month[2] != 0):
            total_min = month[1] / month[2]
            minutes   = round((total_min % 60),2)
            print("  Average delay for " + month[0] + ": " + str(minutes))
            
        
if __name__ == '__main__':
    main()
