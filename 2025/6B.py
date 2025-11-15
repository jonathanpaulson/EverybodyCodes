data = input()
mentors = {}
ans = 0
for c in data:
    if 'A'<=c<='Z':
        if c.lower() not in mentors:
            mentors[c.lower()] = 0
        mentors[c.lower()] += 1
    else:
        ans += mentors[c]
print(ans)
