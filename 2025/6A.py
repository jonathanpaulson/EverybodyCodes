data = input()
mentors = 0
ans = 0
for c in data:
    if c=='A':
        mentors += 1
    elif c=='a':
        ans += mentors
print(ans)
