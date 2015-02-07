import os

#####################################################
######Init the arff##################################
#####################################################

os.remove("fwv.arff")

file_ = open("fwv.arff", "a")

file_.write("@RELATION sys_attack\n")

for x in range(0,326):
    file_.write("@ATTRIBUTE " + str(x) + " REAL\n")

file_.write("@ATTRIBUTE class {attack, normal}\n")
file_.write("@DATA\n")


#####################################################
########Format the arff##############################
#####################################################

path = "../Training_Data_Master/" #where the files are

new_file = "fwv.arff" #our weka file

file_number = 1 #used to modify the file_path as we change files

sys_word = {} #dictionary of the system calls

for combo in range(0,800):#now we are going to read the files

    for x in range(0,326): #set up the dictionary
        sys_word[x] = 0

    if file_number < 10:
        data_file = open(path+"UTD-000"+str(file_number)+".txt", "r+")
    elif file_number < 100:
        data_file = open(path+"UTD-00"+str(file_number)+".txt", "r+")
    else:
        data_file = open(path+"UTD-0"+str(file_number)+".txt", "r+")

    words = data_file.read().split()
    data_file.close()

    for word in words:
        if int(word) > 324:
            sys_word[int(325)] += 1
        else:
            sys_word[int(word)] += 1

    for x in range(0,326):
        sys_word[x] = sys_word[x]/int(325)

    for x in range(0,326):
        if x == 325:
            file_.write(str(sys_word[x]) + ",normal\n")
        else:
            file_.write(str(sys_word[x]) + ",")

    file_number += 1
    
file_.close()

    
    
