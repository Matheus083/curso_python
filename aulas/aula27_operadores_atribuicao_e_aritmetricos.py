# counter  = 0 

# while counter <= 10:
#     counter += 1  # counter = counter + 1

#     print(counter)

#     if counter == 6:
#         continue

#     print(counter)
     
# print("Fim do loop")

counter = 0

while counter <= 100:

    counter += 1 

    if counter >= 5 and counter <= 20:
        print("Está entre 5 e 20")
        continue
    
    print(counter)

    if counter == 40:
        break
    

print("Fim do loop")
