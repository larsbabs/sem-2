# step 1
daft_punk = []
print("Step 1:", daft_punk)

# step 2
daft_punk.append("Thomas Bangalter")
daft_punk.append("Guy-Manuel")
print("Step 2:", daft_punk)

# step 3
for i in range(2):
    daft_punk.append(input())
print("Step 3:", daft_punk)

# step 4
del daft_punk[-1]
del daft_punk[-1]
print("Step 4:", daft_punk)

# step 5
daft_punk.insert(len(daft_punk) + 1, "Legends")
print("Step 5:", daft_punk)


# testing list legth
print("The Fab", len(daft_punk))
