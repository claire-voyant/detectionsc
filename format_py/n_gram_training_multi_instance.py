import os
import glob

#####################################################
######Init the arff##################################
#####################################################

os.remove("ngram.arff")
file_ = open("ngram.arff", "a")

file_.write("@RELATION sys_attack\n")

file_.write("@RELATION bag relational\n")
file_.write("    @ATTRIBUTE " + "POS_ONE" + " REAL\n")
file_.write("    @ATTRIBUTE " + "POS_TWO" + " REAL\n")
file_.write("    @ATTRIBUTE " + "POS_THREE" + " REAL\n")
file_.write("@END bag")

file_.write("@ATTRIBUTE class {attack, normal}\n")
file_.write("@DATA\n")


#####################################################
########Format the arff##############################
#####################################################

path = "../Training_Data_Master/" #where the files are

new_file = "ngram.arff" #our weka file

attack_dir = os.listdir("../Attack_Data_Master")
training_files = glob.glob("../Training_Data_Master/*.txt")
attack_files = []

for dirfile in attack_dir:
    attack_files.extend(glob.glob("../Attack_Data_Master/"+str(dirfile)+"/*.txt"))

x = 0

print("# of training: " + str(len(training_files)))
print("# of attack: " + str(len(attack_files)))

for a_file in training_files:
    train_file = open(a_file, "r+")
    words = train_file.read().split()
    train_file.close()

    file_.write("\"")

    for x in range(0,len(words)-2):        
        file_.write(str(words[x]) + "," + str(words[x+1]) + "," + str(words[x+2]) + "\\n")
        
    file_.write("\",normal\n")
    

for a_file in attack_files:
    train_file = open(a_file, "r+")
    words = train_file.read().split()
    train_file.close()

    file_.write("\"")

    for x in range(0,len(words)-2):
        file_.write(str(words[x]) + "," + str(words[x+1]) + "," + str(words[x+2]) + "\n")

    file_.write("\",attack\n")



    
file_.close()

    
    
