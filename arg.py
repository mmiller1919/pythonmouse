import math

print "What is the x coordinate?",
x = float(raw_input())
print "What is the y?",
y = float(raw_input())

if x >= 328 and y >= 208:
    a = ((x - 328) ** 2 + (y - 208) ** 2)

if x < 328 and y >= 208:
    a = ((328 - x) ** 2 + (y - 208) ** 2)

if x >= 328 and y < 208:
    a = ((x - 328) ** 2 + (y - 208) ** 2)

if x < 328 and y < 208:
    a = ((x - 328) ** 2 + (y - 208) ** 2)

b = (a ** 0.5)

print b

if x > 328 and y > 208:
    print format(90 - ((math.acos((x - 328) / b)) * 180 / 3.14159265358))

if x < 328 and y > 208:
    print format((90 - ((math.acos((328 - x) / b)) * 180 / 3.14159265358)) * -1)

if x > 328 and y < 208:
    print format(((math.acos((x - 328) / b)) * 180 / 3.14159265358) + 90)

if x < 328 and y < 208:
    print format(((math.acos((328 - x) / b)) * 180 / 3.14159265358 * -1) - 90)

if x > 328 and y == 208:
    print format(90)

if x < 328 and y == 208:
    print format(-90)

if x == 328 and y > 208:
    print format(0)

if x == 328 and y < 208:
    print format(180)

if x == 328 and y == 208:
    print format(0)
# take the difference between the origin and new coordinate
# subtract origin from the new coordinate
# if new x was 140 then the dif would be 40, same if x was 60
# d would be the previous coordinate
# if d was 150 and new x was 90, then the dif would be -10
# -10 + 150 = 140, new coordinate, c, is 140
# c would have to become d in the next iteration
#c = (x - 100) + d
