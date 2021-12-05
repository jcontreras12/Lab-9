# Jose Contreras
# 12/2/21
#
count = 0
tens = []
while count < 51:
    if count % 10 == 0:
        tens.append(count)
    count += 1
print("Tens:", tens)