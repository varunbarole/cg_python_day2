


# continue : will skip the current iteration
# break    : will come out of the loop.

# 1 to 10 expect 5 and 8
for val in range(1,11):
    if val == 5 or val == 8:
        continue
    print(val)



# 1 2 3 4
for val in range(1,11):
    if val == 5 or val == 8:
        break
    print(val)
