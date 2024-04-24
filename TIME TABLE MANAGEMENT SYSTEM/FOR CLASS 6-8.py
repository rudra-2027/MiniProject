import random 
import numpy as np
lst = []
d = 0
p = 0
print("YOU CAN USE THE FOLLOWING CODE FOR THE SUBJECTS :")
print("""[English                           :Eng \nHindi                              :Hin\nMaths                              :Maths\nSST                                :SST\nComputer                           :Comp\nScience                            :Sic\nLibrary                            :Lib\nPHE                                :PHE \nYoga                               :Yoga\nSanskrit                           :San\nA.E                                :A.E\nMusic                              :Music]""")
subnum = int(input("Enter number of subjects: "))
for i in range(0, subnum):
    sub = input("enter subject :")
    f = int(input("enter frequency :"))
    d = d + f
    for i in range(0, f):
        lst.append(sub)
if (d > 48):
    print("invalid input")
else:
    for i in range(0, 48 - d):
        ele = "CCA"
        lst.append(ele)
R = 6
C = 8
k = int(input("enter number of timetables"))
for p in range(k):
    lst1 = []
    matrix = []
    m = []
    time = ["MON  ","TUE  ","WED  ","THU  ","FRI  ","SAT  " ]
    for i in range(R):
        a = []
        for j in range(C):
            item = lst[0]
            a.append(item)
            lst.remove(item)
            lst1.append(item)
        matrix.append(a)
        m = np.array(matrix)
        matrix1 = m.T
        for e in range(5):
            random.shuffle(matrix1[e])
        m1 = np.array(matrix1)
        matrix2 = m1.T
    for m in range(30):
        lst.append(lst1[m])
    print("-----FE ", end="")
    print(p + 1, end="")
    print("------")
    print("TIME     P-1     P-2     P-3    P-4      P-5        P-6      P-7      P-8")
    for i in range(R):
        print(time[i], end="")
        for j in range(C):
            print(matrix2[i][j], end="         ")
        print()
