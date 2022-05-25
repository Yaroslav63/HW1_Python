String ="exexe exexexe"
a = String
count = 0
while "xex" in a:
    count += 1
    a = a.replace("xex", "x", 1)
print(count)