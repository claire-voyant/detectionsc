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

file_a0 = "a0.txt"
file_a1 = "a1.txt"
file_a2 = "a2.txt"
file_a3 = "a3.txt"
file_a4 = "a4.txt"
file_a5 = "a5.txt"
file_a6 = "a6.txt"
file_a7 = "a7.txt"
file_a8 = "a8.txt"
file_a9 = "a9.txt"

format_a = [file_a0,file_a1,file_a2,file_a3,file_a4,file_a5,file_a6,file_a7,file_a8,file_a9]

file_n0 = "n0.txt"
file_n1 = "n1.txt"
file_n2 = "n2.txt"
file_n3 = "n3.txt"
file_n4 = "n4.txt"
file_n5 = "n5.txt"
file_n6 = "n6.txt"
file_n7 = "n7.txt"
file_n8 = "n8.txt"
file_n9 = "n9.txt"

format_n = [file_n0,file_n1,file_n2,file_n3,file_n4,file_n5,file_n6,file_n7,file_n8,file_n9]

file_v0 = "v0.txt"
file_v1 = "v1.txt"
file_v2 = "v2.txt"
file_v3 = "v3.txt"
file_v4 = "v4.txt"
file_v5 = "v5.txt"
file_v6 = "v6.txt"
file_v7 = "v7.txt"
file_v8 = "v8.txt"
file_v9 = "v9.txt"


format_v = [file_v0,file_v1,file_v2,file_v3,file_v4,file_v5,file_v6,file_v7,file_v8,file_v9]


##################################################
####Create the instances for validation testing###
##################################################
##################################################

def makeValidationInstance(fileName):
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

instance_a0 = makeFitInstance(file_a0)
instance_a1 = makeFitInstance(file_a1)
instance_a2 = makeFitInstance(file_a2)
instance_a3 = makeFitInstance(file_a3)
instance_a4 = makeFitInstance(file_a4)
instance_a5 = makeFitInstance(file_a5)
instance_a6 = makeFitInstance(file_a6)
instance_a7 = makeFitInstance(file_a7)
instance_a8 = makeFitInstance(file_a8)
instance_a9 = makeFitInstance(file_a9)

instance_n0 = makeFitInstance(file_n0)
instance_n1 = makeFitInstance(file_n1)
instance_n2 = makeFitInstance(file_n2)
instance_n3 = makeFitInstance(file_n3)
instance_n4 = makeFitInstance(file_n4)
instance_n5 = makeFitInstance(file_n5)
instance_n6 = makeFitInstance(file_n6)
instance_n7 = makeFitInstance(file_n7)
instance_n8 = makeFitInstance(file_n8)
instance_n9 = makeFitInstance(file_n9)

clf = svm.SVC()
print("Starting cross validation with 10 folds...")

###Fold 1
###

fit_data0 = instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0]
fit_classes0 = instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1]


vali0 = makeValidationInstance(file_v0) 

print("Fold 1....")
clf.fit(fit_data0,fit_classes0)
print("% correct: " + str(validateClass(clf,vali0)))

###Fold 2
###

fit_data1 = instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0]
fit_classes1 = instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1]

#vali1 = makeValidationInstance(file_a0) + makeValidationInstance(file_n0)

###Fold 3
###

fit_data0 = instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0]
fit_classes0 = instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1]

vali2 = makeValidationInstance(file_a1) + makeValidationInstance(file_n1)

###Fold 4
###

fit_data0 = instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0]
fit_classes0 = instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1]

vali3 = makeValidationInstance(file_a2) + makeValidationInstance(file_n2)


###Fold 5
###

fit_data0 = instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0]
fit_classes0 = instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1]


vali4 = makeValidationInstance(file_a3) + makeValidationInstance(file_n3)

###Fold 6
###

fit_data0 = instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_n5[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0]
fit_classes0 = instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_n5[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1]

vali5 = makeValidationInstance(file_a4) + makeValidationInstance(file_n4)

###Fold 7
###

fit_data0 = instance_a6[0] + instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_n6[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0]
fit_classes0 = instance_a6[1] + instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_n6[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1]

vali6 = makeValidationInstance(file_a5) + makeValidationInstance(file_n5)

###Fold 8
###

fit_data0 = instance_a7[0] + instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_n7[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0]
fit_classes0 = instance_a7[1] + instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_n7[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1]

vali7 = makeValidationInstance(file_a6) + makeValidationInstance(file_n6)

###Fold 9
###

fit_data0 = instance_a8[0] + instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_n8[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0]
fit_classes0 = instance_a8[1] + instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_n8[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1]

vali8 = makeValidationInstance(file_a7) + makeValidationInstance(file_n7)

###Fold 10
####

fit_data0 = instance_a9[0] + instance_a0[0] + instance_a1[0] + instance_a2[0] + instance_a3[0] + instance_a4[0] + instance_a5[0] + instance_a6[0] + instance_a7[0] + instance_n9[0] + instance_n0[0] + instance_n1[0] + instance_n2[0] + instance_n3[0] + instance_n4[0] + instance_n5[0] + instance_n6[0] + instance_n7[0]
fit_classes0 = instance_a9[1] + instance_a0[1] + instance_a1[1] + instance_a2[1] + instance_a3[1] + instance_a4[1] + instance_a5[1] + instance_a6[1] + instance_a7[1] + instance_n9[1] + instance_n0[1] + instance_n1[1] + instance_n2[1] + instance_n3[1] + instance_n4[1] + instance_n5[1] + instance_n6[1] + instance_n7[1]

vali9 = makeValidationInstance(file_a8) + makeValidationInstance(file_n8)


