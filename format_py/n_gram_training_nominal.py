import os
import glob

#####################################################
######Init the arff##################################
#####################################################

os.remove("ngram_nominal.arff")

sys_calls = open("sys_call.txt", "r+")

sys_word = {}
x = 0
for func in sys_calls:
    sys_word[x] = func.rstrip()
    x += 1
    
print(sys_word)

sys_calls.close()
    

file_ = open("ngram_nominal.arff", "a")

file_.write("@RELATION sys_attack\n")

file_.write("@ATTRIBUTE " + "POS_ONE" + "{")
for x in range(0,325):
    if sys_word[x] != ("undef"):        
        if x == 324:
            file_.write(sys_word[x] + ",undef" + "}\n")
        else:
            file_.write(sys_word[x] + ",")
        
file_.write("@ATTRIBUTE " + "POS_TWO" + "{")
for x in range(0,325):
    if sys_word[x] != ("undef"):        
        if x == 324:
            file_.write(sys_word[x] + ",undef" + "}\n")
        else:
            file_.write(sys_word[x] + ",")
        
file_.write("@ATTRIBUTE " + "POS_THREE" + "{")
for x in range(0,325):
    if sys_word[x] != ("undef"):        
        if x == 324:
            file_.write(sys_word[x] + ",undef" + "}\n")
        else:
            file_.write(sys_word[x] + ",")
        

file_.write("@ATTRIBUTE class {attack, normal}\n")
file_.write("@DATA\n")


#####################################################
########Format the arff##############################
#####################################################

path = "../Training_Data_Master/" #where the files are

new_file = "ngram_nominal.arff" #our weka file

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

    for x in range(0,len(words)-2):
        n1 = "undef"
        n2 = "undef"
        n3 = "undef"
        if int(words[x]) < 325:
            n1 = sys_word[int(words[x])]
        if int(words[x+1]) < 325:
            n2 = sys_word[int(words[x+1])]
        if int(words[x+2]) < 325: 
            n3 = sys_word[int(words[x+2])]
        
        file_.write(n1 + "," + n2 + "," + n3 + ",normal\n")
        

for a_file in attack_files:
    train_file = open(a_file, "r+")
    words = train_file.read().split()
    train_file.close()

    for x in range(0,len(words)-2):
        n1 = "undef"
        n2 = "undef"
        n3 = "undef"
        if int(words[x]) < 325:
            n1 = sys_word[int(words[x])]
        if int(words[x+1]) < 325:
            n2 = sys_word[int(words[x+1])]
        if int(words[x+2]) < 325: 
            n3 = sys_word[int(words[x+2])]
        file_.write(n1 + "," + n2 + "," + n3 + ",attack\n")




    
file_.close()

    
    
