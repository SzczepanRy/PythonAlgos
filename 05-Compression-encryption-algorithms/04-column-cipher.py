message = "uga buga fuga"
meaasgeArr = list(message)
columns = 4
lengthArr = len(meaasgeArr)

rows = int(lengthArr /4 )+1

table2D =[]
for i in range(rows):
    row1D=[]
    for j in range(columns):
        row1D.append(meaasgeArr[i+j])

    table2D.append(row1D)

print(table2D)