sys_word = {}

for x in range(0,325):
    sys_word[x] = 0

file = open("UAD-0015.txt", "r+")

words = file.read().split()

file.close()

for word in words:
    sys_word[int(word)] += 1

for x in range(0,325):
    sys_word[x] = sys_word[x]/int(325)

file_ = open("a_1.txt", "w")

for x in range(0,325):
    if x is 324:
        file_.write(str(sys_word[x]) + "\n")
    else:
        file_.write(str(sys_word[x]) + ",")

file_.close()
        



print(sys_word)
            
    




    
