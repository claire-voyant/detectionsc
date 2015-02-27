import os

import glob

#####################################################
######Init the files##################################
#####################################################
os.remove("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_vali.txt")
os.remove("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_normal.txt")
os.remove("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_attack.txt")

file__ = open("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_normal.txt", "a")
file_ = open("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_attack.txt", "a")
file_v = open("C:/Users/will_doyle/Documents/GitHub/datamining/format_py/single_ngram_vali.txt", "a")


the_attack_files = glob.glob("C:/Users/will_doyle/Documents/GitHub/datamining/att/*.txt")
the_normal_files = glob.glob("C:/Users/will_doyle/Documents/GitHub/datamining/norm/*.txt")
the_vali_files   = glob.glob("C:/Users/will_doyle/Documents/GitHub/datamining/vali/*.txt")

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


#####################################################
########Generate the n-gram##########################
#########and write that to the file##################
#####################################################

n = 3

for norm in normal_words:
    for x in range(0,len(norm)-(n-1)):
        file__.write(str(norm[x]) + " " + str(norm[x+1]) + " " + str(norm[x+2]) + " 0\n")

for att in attack_words:
    for x in range(0,len(att)-(n-1)):
        file_.write(str(att[x]) + " " + str(att[x+1]) + " " + str(att[x+2]) + " 1\n")

for vali in vali_words:
    for x in range(0,len(vali)-(n-1)):
        file_v.write(str(vali[x]) + " " + str(vali[x+1]) + " " + str(vali[x+2]) + " 0\n")
    file_v.write("new\n")

file__.close()
file_.close()
file_v.close()

print("Data Formatted...")

    
    
