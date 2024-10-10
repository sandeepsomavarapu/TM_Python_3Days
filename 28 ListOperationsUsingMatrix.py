ids=[[12,45,55],[78,99,56],[45,66,39]]
print(ids)
for row  in ids:
    print(max(row))
for i in range(len(ids)):
    for j in range(len(ids[i])):
        print(ids[i][j],end=' ')
    print()