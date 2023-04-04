sel = int(input("진수를 입력하시오. (16/10/8/2) : "))
num = input("숫자입력 : ")

if sel == 16 :
    num10 = int(num, 16)
    print("16진법을 선택함.")
if sel == 10 :
    num10 = int(num, 10)
    print("10진법을 선택함.")
if sel == 8 :
    num10 = int(num, 8)
    print("8진법을 선택함.")
if sel == 2 :
    num10 = int(num, 2)
    print("2진법을 선택함.")
    
if sel != 16 and 10 and 8 and 2 :
    print("4가지 진법 중에서 선택하세요.")
    exit()
print("16진법 ==> ", hex(num10))
print("10진법 ==> ", num10)
print(" 8진법 ==> ", oct(num10))
print(" 2진법 ==> ", bin(num10))
