# 딕셔너리
a = {"김도한": "010-7321-7472"}
print(a["김도한"])
a["박지영"] = "010-9765-1234"

print(a["박지영"])
# 리스트
b = ["010-8477-84848"]
print("<<<<<<<<<<<<<<" + b[0])

# 딕셔너리- 키가 튜플
c = {("정유선", "성악"): "이태원"}
print(c[("정유선", "성악")])
# 키값이 달라서 못 불러옴
# print(c[("정유선")])

# 디셔너리 get
d = {"김도한": "맥주", "이광우": "소주", "정유선": "소주"}
print(d.get("김도한"))
print(d["김도한"])

is_jiyonng_exist = "박지영" in d
print(type(is_jiyonng_exist))
print(type(d))

# element 삭제
d.pop("김도한")
del d["이광우"]
print(d)
