a = {"김도한": "010-7321-7472", "ㅎㅎㅎ": "010-4847-5858"}

for name in a:
    print(name)

    for key in a.keys():
        print(key)

        for item in a.items():
            print(item)

# range 함수를 이용하여 List 생성
a = range(10)

for i in a:
    print(i)

