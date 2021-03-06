import random

title = """
███╗░░░███╗░█████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗╚══██╔══╝██║░░██║
██╔████╔██║███████║░░░██║░░░███████║
██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║
██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝"""
end = """
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░██╗
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░██║
██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░██║
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗╚═╝
██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝"""
wrong = """
░██╗░░░░░░░██╗██████╗░░█████╗░███╗░░██╗░██████╗░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██╔════╝░██║
░╚██╗████╗██╔╝██████╔╝██║░░██║██╔██╗██║██║░░██╗░██║
░░████╔═████║░██╔══██╗██║░░██║██║╚████║██║░░╚██╗╚═╝
░░╚██╔╝░╚██╔╝░██║░░██║╚█████╔╝██║░╚███║╚██████╔╝██╗
░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝"""
correct = """
░█████╗░░█████╗░██████╗░██████╗░███████╗░█████╗░████████╗██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║
██║░░╚═╝██║░░██║██████╔╝██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║
██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░╚═╝
╚█████╔╝╚█████╔╝██║░░██║██║░░██║███████╗╚█████╔╝░░░██║░░░██╗
░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝"""
attempts = 3
score = 0

print(title)

def CheckAnswer(correctanwer):
    global attempts, score
    c = input("Ответ: ")
    if str(correctanwer) == c:
        print(correct)
        score = score + 1
        print(f"You have {score} score!")
    else:
        print(wrong)
        attempts = attempts - 1

def Plus():
    global attempts, score
    a = random.randint(1,50 + score)
    b = random.randint(1,50 + score)
    print(f"{a} + {b} = ?")
    CheckAnswer(a + b)

def Minus():
    global attempts, score
    a = random.randint(1,50 + score)
    b = random.randint(1,50 + score)
    if a < b:
        a,b = b,a
    
    print(f"{a} - {b} = ?")
    CheckAnswer(a - b)

def Multiplication():
    global attempts, score
    a = random.randint(1,10 + score)
    b = random.randint(1,10 + score)
    print(f"{a} * {b} = ?")
    CheckAnswer(a * b)

def Delenie():
    global attempts, score
    a = random.randint(1,10 + score)
    b = random.randint(1,10 + score)
    c = a * b
    a = c
    print(f"{a} : {b} = ?")
    CheckAnswer(int(c / b))

math = [Plus, Minus, Multiplication, Delenie]

while True:
    random.choice(math)()
    if attempts == 0:
        print(end)
        input("")
        break