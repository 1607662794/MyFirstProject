number = int(input().strip())
if number <= 1:
    print("{:.10f}".format(round(0)))
elif number == 2:
    print("{:.10f}".format(round(1)))
else:
    result = round(2/(number*(number-1)),10)
    print("{:.10f}".format(result))