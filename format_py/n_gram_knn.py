##################################################
######scikit_learn to do the classifications######
##################################################
##################################################
##test change


from sklearn import neighbors

##################################################
#####Hard coded (currently) where the datasets####
#################are located######################
##################################################

attack_file = 'single_ngram_attack.txt'
normal_file = 'single_ngram_normal.txt'
test_file   = 'single_ngram_vali.txt'

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

##################################################
##############Train the Support Vector############
######################Machine#####################
##################################################

clf = neighbors.KNeighborsClassifier(n_neighbors=3,weights='uniform',algorithm='ball_tree')
clf.fit(fit_data,fit_classes)

print("Model has been trained, building test dataset...")

##################################################
#############Create the validation data###########
##################################################
##################################################

instance_v = makeValiInstance(test_file)

print("Validating the test dataset...")

##################################################
############Validate the data with the trained####
###############Support Vector Machine#############
##################################################

print("Percentage validated correctly: " + str(validateClass(clf,instance_v)))

