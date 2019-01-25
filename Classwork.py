# KEY: Don't forget your comments :-(

def main():
    # prob1()
    prob2()
    # chall1()
    # chall2()

def prob1():
    while 1==1:
        user = input("Enter a word: ")
        if user == "q":
            break
        else:
            print(user)

def prob2():
    num1 = 2
    num2 = 8
    num3 = 5
    while 1 == 1:
        help = input("SUM, AVG,or PROD! ")
        if help == "SUM":
            allSum = num1 + num2 + num3
            print("The SUM of", num1, num2, num3, "is", allSum)
            break
        elif help == "PROD":
            allProd = num1 * num2 * num3
            print("The PROD of", num1, num2, num3, "is", allProd)
            break
        elif help == "AVG":
            allAvg= (num1 + num2 + num3) / 3
            print("The AVG of", num1, num2, num3, "is", allAvg)
            break
        else:
            print("ERROR")

def chall1():
    star = "*"
    a = 1
    number = int(input("Enter Star count: "))
    while a <= number:
        print(star * a)
        a += 1

def chall2():
    print("Observing Driver")
    while 1 == 1:
        speed = int(input("How fast are you going?"))
        if speed <= 70:
            print("OK")
        else:
            find = speed - 70
            d = 0
            if find % 5 ==0:
                d += 1
            else:
                break


if __name__ == '__main__':
    main()