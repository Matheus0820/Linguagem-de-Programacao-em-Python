n = int(input())
list_sequence = []

for i in range(n):
    list_sequence.append(int(input()))

for i in range(len(list_sequence)):
    for j in range(len(list_sequence) - 1, i, -1):
        if list_sequence[i] == list_sequence[j]:
            list_sequence.pop(j)

print(list_sequence)