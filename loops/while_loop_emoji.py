#for loop version 
for num in range(1,11):
    print("\U0001f600" * num)

#while loop
times = 1
while times < 11:
    print("\U0001f600" * times)
    times += 1

# nested loop
for x in range(3): 
    for num in range(1,11):
        print("\U0001f600" * num)

#gross loop
for num in range(1,11):
    count = 1 
    smileys = ""
    while count <= num:
        smileys += "\U0001f600" 
        count += 1
    print(smileys)

#tried to center the triangle to make pyramid
times = 1
while times < 20:
    print("\U0001f600" * times)
    times += 2