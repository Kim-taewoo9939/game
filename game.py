print("퉁퉁이와 진구의 혈투...")
list_a = ["퉁퉁이의 쨉" ,"퉁퉁이의 원투", "진구의 위빙","진구의 원투","퉁퉁이의 라이트 훅" ]
print("1, 퉁퉁이의 쩁 2. 퉁퉁이의 원투 3. 진구의 위빙 4. 진구이 원투 5. 퉁퉁이의 라이트 훅")
dict_b = {
    "name" : "그만싸워"
}
i = 0
while i < 10:
    i = i+1
    number = input("오더를 해주세요 : ")
    if int(number) == 1:
        print(list_a[0])
    if int(number) == 2:
        print(list_a[1])
    if int(number) == 3:
        print(list_a[2])
    if int(number) == 4:
        print(list_a[3])
    if int(number) == 5:
        print(list_a[4])
    if i == 10:
        print(dict_b["name"])