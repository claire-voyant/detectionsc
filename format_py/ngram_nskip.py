import os

import glob

#####################################################
######Init the files##################################
#####################################################
os.remove("a0.txt")
os.remove("a1.txt")
os.remove("a2.txt")
os.remove("a3.txt")
os.remove("a4.txt")
os.remove("a5.txt")
os.remove("a6.txt")
os.remove("a7.txt")
os.remove("a8.txt")
os.remove("a9.txt")

os.remove("n0.txt")
os.remove("n1.txt")
os.remove("n2.txt")
os.remove("n3.txt")
os.remove("n4.txt")
os.remove("n5.txt")
os.remove("n6.txt")
os.remove("n7.txt")
os.remove("n8.txt")
os.remove("n9.txt")

os.remove("v0.txt")
os.remove("v1.txt")
os.remove("v2.txt")
os.remove("v3.txt")
os.remove("v4.txt")
os.remove("v5.txt")
os.remove("v6.txt")
os.remove("v7.txt")
os.remove("v8.txt")
os.remove("v9.txt")

file_a0 = open("a0.txt", "a")
file_a1 = open("a1.txt", "a")
file_a2 = open("a2.txt", "a")
file_a3 = open("a3.txt", "a")
file_a4 = open("a4.txt", "a")
file_a5 = open("a5.txt", "a")
file_a6 = open("a6.txt", "a")
file_a7 = open("a7.txt", "a")
file_a8 = open("a8.txt", "a")
file_a9 = open("a9.txt", "a")

format_a = [file_a0,file_a1,file_a2,file_a3,file_a4,file_a5,file_a6,file_a7,file_a8,file_a9]

file_n0 = open("n0.txt", "a")
file_n1 = open("n1.txt", "a")
file_n2 = open("n2.txt", "a")
file_n3 = open("n3.txt", "a")
file_n4 = open("n4.txt", "a")
file_n5 = open("n5.txt", "a")
file_n6 = open("n6.txt", "a")
file_n7 = open("n7.txt", "a")
file_n8 = open("n8.txt", "a")
file_n9 = open("n9.txt", "a")

format_n = [file_n0,file_n1,file_n2,file_n3,file_n4,file_n5,file_n6,file_n7,file_n8,file_n9]

file_v0 = open("v0.txt", "a")
file_v1 = open("v1.txt", "a")
file_v2 = open("v2.txt", "a")
file_v3 = open("v3.txt", "a")
file_v4 = open("v4.txt", "a")
file_v5 = open("v5.txt", "a")
file_v6 = open("v6.txt", "a")
file_v7 = open("v7.txt", "a")
file_v8 = open("v8.txt", "a")
file_v9 = open("v9.txt", "a")


format_v = [file_v0,file_v1,file_v2,file_v3,file_v4,file_v5,file_v6,file_v7,file_v8,file_v9]


the_attack_files = glob.glob("../Basic_Attack/*.txt")
the_normal_files = glob.glob("../Normal_Data/*.txt")
the_vali_files   = glob.glob("../Vali_Data/*.txt")

#####################################################
########Format the files##############################
#####################################################

attack_words = []
normal_words = []
vali_words   = []


#####################################################
########Read in the sequences########################
#########separate them into 2D arrays################
#####################################################

for f in the_attack_files:
    e = open(f,"r+")
    attack_words.extend([e.read().split()])
    e.close()
for f in the_normal_files:
    e = open(f,"r+")
    normal_words.extend([e.read().split()])
    e.close()
for f in the_vali_files:
    e = open(f,"r+")
    vali_words.extend([e.read().split()])
    e.close()

files_a = len(attack_words)/10
files_n = len(normal_words)/10
files_v = len(vali_words)/10

print("Normal Words: " + str(len(normal_words)))
print("Average normal words per formatted file: "  + str(files_n))

print("Attack Words: " + str(len(attack_words)))
print("Average attack words per formatted file: " + str(files_a))

print("Validation Words: " + str(len(vali_words)))
print("Average validation words per formatted file: " + str(files_v))

input_n = raw_input("Please input a value for n: ")
print("Performing formatting with " + str(input_n) + " grams...")
n = int(input_n)
y = 0
index = 0
to_write = format_n[index]

for norm in normal_words:
    for x in range(0,len(norm) - (n-1)):
        for form in range(0, n):
            if(form < n-1):
                to_write.write(str(norm[x+form]) + " ")
            elif(form == n-1): 
                to_write.write(str(norm[x+form]) + " 0\n")
    to_write.write("new\n")
    y += 1   
    if(y % files_n == 0 and index < 9):	
        print( str(y) + " instances in norm_block...")
	#print("X: " + str(y))
	#print("Ending: " + str(index) + "\n Starting: " + str(index+1))
	to_write.close()
	index = index + 1
        to_write = format_n[index]

y = 0
index = 0
to_write = format_a[index]

for norm in attack_words:
    for x in range(0,len(norm) - (n-1)):
        for form in range(0, n):
            if(form < n-1):
                to_write.write(str(norm[x+form]) + " ")
            elif(form == n-1):
                to_write.write(str(norm[x+form]) + " 1\n")
    to_write.write("new\n")
    y += 1   
    if(y % files_a == 0 and index < 9):
        print( str(y) + " instances in att_block...")
	#print("Ending: " + str(index) + "\n Starting: " + str(index+1))
	to_write.close()
	index = index + 1
        to_write = format_a[index]

y = 0
index = 0
to_write = format_v[index]

for norm in vali_words:
    for x in range(0,len(norm) - (n-1)):
        for form in range(0,n):
            if(form < n-1):
                to_write.write(str(norm[x+form]) + " ")
            elif(form == n-1):
                to_write.write(str(norm[x+form]) + " 0\n")
    to_write.write("new\n")
    y += 1   
   
    if(y % files_v == 0 and index < 9):
        print( str(y) + " instances in vali_block...")
	#print("Ending: " + str(index) + "\n Starting: " + str(index+1))
	to_write.close()
	index = index + 1
        to_write = format_v[index]    


#####################################################
########Generate the n-gram##########################
#########and write that to the file##################
#####################################################

#n = 3

#for norm in normal_words:
 #   for x in range(0,len(norm)-(n-1)):
  #      file__.write(str(norm[x]) + " " + str(norm[x+1]) + " " + str(norm[x+2]) + " 0\n")

#for att in attack_words:
 #   for x in range(0,len(att)-(n-1)):
  #      file_.write(str(att[x]) + " " + str(att[x+1]) + " " + str(att[x+2]) + " 1\n")

#for vali in vali_words:
 #   for x in range(0,len(vali)-(n-1)):
  #      file_v.write(str(vali[x]) + " " + str(vali[x+1]) + " " + str(vali[x+2]) + " 0\n")
   # file_v.write("new\n")

print("Data Formatted...")

    
    
