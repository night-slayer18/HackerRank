# there are 26 chairs that neeeds to be arranged for a ceremony. the chairs are made from a to z. every chair should be arranged according to the original number of letters in the 
# english alphabet, due to some misunderstanding the chairs are randomly arranged. given a string, the task here to find the number of chairs which are correctly placed as per the original 
# numbering of the letters.

# abcdodcnck

# 4

# abkjffgh

# 5




def count_chairs(chairs):
    count = 0
    for i in range(len(chairs)):
        if chairs[i] == chr(97+i):
            count += 1
    return count

chairs = input()
print(count_chairs(chairs))
