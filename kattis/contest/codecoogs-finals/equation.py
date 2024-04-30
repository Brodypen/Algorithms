
a, b, c, d = map(int, input().split())

operations = ['*', '+', '-', '/']

neverPrinted = False
for i in range(4):
    for j in range(4):
        if(int(eval(str(a) + operations[i] + str(b))) == int(eval(str(c) + operations[j] + str(d)))):
            neverPrinted = True
            print(str(a),operations[i], str(b) + " = " + str(c), operations[j], str(d))

if not neverPrinted:
    print("problems ahead")