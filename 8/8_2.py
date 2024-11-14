priests = 2
thickness = 1
columns = [1]
highPriests = 10
limit = 202400000000

# count the number of blocks until it goes over the max
# we only need to store half the list because it is mirrored
# still takes a while :/
while True:
    thickness = ((thickness * priests) % highPriests) + highPriests
    for i in range(len(columns)):
        columns[i] += thickness
    columns.append(thickness)
    print(columns[0])

    # calculate the total count with the removals in mind
    count = 0
    for i in range(len(columns)):
        if i == 0:
            count += columns[i] - ((priests * (len(columns) * 2 - 1) * columns[i]) % highPriests)
        elif i == len(columns) - 1:
            count += 2 * columns[i]
        else:
            count += 2 * (columns[i] - ((priests * (len(columns) * 2 - 1) * columns[i]) % highPriests))
    if count > limit:
        print(count - limit)
        break
