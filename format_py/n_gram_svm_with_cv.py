##################################################
######scikit_learn to do the classifications######
##################################################
##################################################

from sklearn import svm
from sklearn import cross_validation

##################################################
#####Hard coded (currently) where the datasets####
#################are located######################
##################################################

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


##################################################
####Create the instances for validation testing###
##################################################
##################################################

def makeValiInstance(fileName):
    if isinstance(fileName,str):
        my_file = open(str(fileName),"r+")
        words = my_file.read().split("\n")
        my_file.close()
        words.remove('')
        
        num_instances = words.count("new")
        print("Number of Instances to Validate: " + str(num_instances))
     
        instance = []
        data = []
        for line in words:
            if line == "new":    
                my_data = [data]           
                instance += (my_data)
                data = []
            data.extend([line.split()])
            
        for i in instance:
            for entry in i:
                if '1' in entry:
                    entry.remove('1')
                if '0' in entry:
                    entry.remove('0')
            
        return instance    
    else:
        return -1

##################################################
#####Create the instances for training############
##################################################
##################################################

def makeFitInstance(fileName):
    if isinstance(fileName, str):
        my_file = open(str(fileName), "r+")
        words = my_file.read().split("\n")
        my_file.close()
        words.remove('')
    
        data = []
        for line in words:
            data.extend([line.split()])
    
        classi = []
        for entry in data:
            if entry[-1] == '1':
                classi.extend('a')
                entry.remove('1')
            else:
                classi.extend('n')
                entry.remove('0')         
    
        instance = {}
        instance[0] = data
        instance[1] = classi
        return instance
    else:
        return -1
    
##################################################
#######Calculates the class of the subsequences###
########as a ratio################################
##################################################

def calClass(svm,data):
    normal = ['n']
    attack = ['a']
    num = 0
    total_n = 0
    total_a = 0
    if ['new'] in data:
        data.remove(['new'])
    for x in data:
        num += 1
        if svm.predict(x) == attack:
            total_a += 1
        elif svm.predict(x) == normal:
            total_n += 1
        else:
            print("OOPS")
            return    
    nratio = (float(total_n)/float(num))
    aratio = (float(total_a)/float(num))    
    if nratio > 0.9:
        return 'normal'
    else:
        return 'attack'
    
##################################################
#########Percentage validation####################
###########of the validation data#################
##################################################

def validateClass(svm,validation_array):
    validate = 0.0
    num = 0.0
    print("length: " + str(len(validation_array)))
    for data in validation_array:
        num += 1
        if calClass(svm,data) == 'normal':
            validate += 1
        
        print("NUM: " + str(int(num)) + " CLASSIFIED AS: " + calClass(svm,data))
    return float((validate)/(num))

##################################################
################Main##############################
##################################################
##################################################

print("Creating the training data...")

##################################################
#############Create the attack and################
#################normal data and combine them#####
##################################################

instance_a = makeFitInstance(attack_file)
instance_n = makeFitInstance(normal_file)

fit_data = instance_a[0] + instance_n[0]
fit_classes = instance_a[1] + instance_n[1]

print("Training the model....")
print("Creating folds....")
##################################################
##############Train the Support Vector############
######################Machine#####################
##################################################

skf = cross_validation.StratifiedKFold(fit_classes, n_folds=10)

print("Folds created...")
print(str(len("Length of skf: " + str(skf))))


clf = svm.SVC()

print("Starting cross validation with 10 folds...")
        
  

#clf.fit(fit_data,fit_classes)

print("Model has been trained, building test dataset...")

###################################################
##############Create the validation data###########
###################################################
###################################################
#
#instance_v = makeValiInstance(test_file)
#
#print("Validating the test dataset...")
#
###################################################
#############Validate the data with the trained####
################Support Vector Machine#############
###################################################
#
#print("Percentage validated correctly: " + str(validateClass(clf,instance_v)))

