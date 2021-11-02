
x = int(input("Enter a Value: "))

for i in range(2,x):
    if x % i == 0 :
        def notasal():
            print("Asal değil")
    elif not x % i == 0:
        def asal():
            print("Asal")
    else :
        print("The value is cannot defined")

#exeptions
if x ==2:
    print("Asal")
elif x ==1:
    print("Asal değil")
try:
    notasal()
except:
    asal()