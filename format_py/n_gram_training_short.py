import os
import glob

#####################################################
######Init the arff##################################
#####################################################

os.remove("ngram_short.arff")

file_ = open("ngram_short.arff", "a")

file_.write("@RELATION sys_attack\n")

file_.write("@ATTRIBUTE " + "POS_ONE" + " REAL\n")
file_.write("@ATTRIBUTE " + "POS_TWO" + " REAL\n")
file_.write("@ATTRIBUTE " + "POS_THREE" + " REAL\n")

file_.write("@ATTRIBUTE class {attack, normal}\n")
file_.write("@DATA\n")


#####################################################
########Format the arff##############################
#####################################################

path = "../Training_Data_Master/" #where the files are

new_file = "ngram_short.arff" #our weka file

attack_dir = os.listdir("../Attack_Data_Master")
training_files = glob.glob("../Training_Data_Master/*.txt")

print(training_files[0])


short_train = [0]*100
short_attack = [0]*10

for x in range(0,100):
    short_train[x] = (training_files[x])

for x in range(0,10):
    short_attack[x] = (attack_dir[x])

attack_files = []

for dirfile in short_attack:
    attack_files.extend(glob.glob("../Attack_Data_Master/"+str(dirfile)+"/*.txt"))

x = 0

print("# of training: " + str(len(short_train)))
print("# of attack: " + str(len(attack_files)))

for a_file in short_train:
    train_file = open(a_file, "r+")
    words = train_file.read().split()
    train_file.close()

    for x in range(0,len(words)-2):
        file_.write(str(words[x]) + "," + str(words[x+1]) + "," + str(words[x+2]) + ",normal\n")

for a_file in attack_files:
    train_file = open(a_file, "r+")
    words = train_file.read().split()
    train_file.close()

    for x in range(0,len(words)-2):
        file_.write(str(words[x]) + "," + str(words[x+1]) + "," + str(words[x+2]) + ",attack\n")




    
file_.close()

    
    
