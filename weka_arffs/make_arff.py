file_ = open("sys_attack.txt", "a")

file_.write("@RELATION sys_attack\n")

for x in range(0,325):
    file_.write("@ATTRIBUTE " + str(x) + " REAL\n")

file_.write("@ATTRIBUTE class {attack, normal}\n")
file_.write("@DATA\n")

file_.close()

