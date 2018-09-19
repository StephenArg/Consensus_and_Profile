import os

os.chdir("/Users/BasicallySteve/Desktop")

file = open('data.txt', 'r')
label_list = []
DNA_list = []
DNA_combined = ""
A_storage = []
C_storage = []
G_storage = []
T_storage = []
most_likely_seq = ""

for DNA in file.readlines():
    if DNA[0] == ">":
        DNA_list.append(DNA_combined)
        DNA_combined = ""
        DNA = DNA.replace("\n", "")
        DNA = DNA.replace(">", "")
        label_list.append(DNA)
    else:
        DNA = DNA.replace("\n", "")
        DNA_combined += DNA

DNA_list.append(DNA_combined)

del DNA_list[0]

total_Strands = len(DNA_list)

i = 0
l = 0
length = len(DNA_list[0])

while l < length:
    A_storage.append(0)
    C_storage.append(0)
    G_storage.append(0)
    T_storage.append(0)
    i = 0
    while i < total_Strands:
        strand = DNA_list[i]
        x = strand[l]
        if x == "A":
            A_storage[l] += 1
            i += 1
        elif x == "C":
            C_storage[l] += 1
            i += 1
        elif x == "G":
            G_storage[l] += 1
            i += 1
        else:
            T_storage[l] += 1
            i += 1
    l += 1

j = 0

while j < length:
    if A_storage[j] >= G_storage[j]:
        if A_storage[j] >= C_storage[j]:
            if A_storage[j] > T_storage[j]:
                most_likely_seq = most_likely_seq + "A"
                j +=1
            else:
                most_likely_seq = most_likely_seq + "T"
                j +=1
        elif C_storage[j] > T_storage[j]:
            most_likely_seq = most_likely_seq + "C"
            j += 1
        else:
            most_likely_seq = most_likely_seq + "T"
            j += 1
    elif G_storage[j] >= C_storage[j]:
        if G_storage[j] > T_storage[j]:
            most_likely_seq = most_likely_seq + "G"
            j += 1
        else:
            most_likely_seq = most_likely_seq + "T"
            j += 1
    elif C_storage[j] > T_storage[j]:
        most_likely_seq = most_likely_seq + "C"
        j += 1
    else:
        most_likely_seq = most_likely_seq + "T"
        j += 1

A_storage.insert(0,'A:')
C_storage.insert(0,'C:')
G_storage.insert(0,'G:')
T_storage.insert(0,'T:')
with open("answer.txt", "w") as o:
    o.write(most_likely_seq)
    print(most_likely_seq)
    for a in A_storage:
        a = str(a)
        print(a,end=" ")
    print("")
    for c in C_storage:
        print(c,end=" ")
    print("")
    for g in G_storage:
        print(g,end=" ")
    print("")
    for t in T_storage:
        print(t,end=" ")
