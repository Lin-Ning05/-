foot = int(input())
inch = int(input())

mm = (12 * foot + inch) * 25
cm = mm // 10

print(str(mm) + ',' + str(cm))
