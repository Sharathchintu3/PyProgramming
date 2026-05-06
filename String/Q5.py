s = input()
# a = s.replace(" ", "-")
# print(a)

# or

res = ""
for i in s:
    if i == " ":
        res += "-"
    else:
        res += i
print(res)