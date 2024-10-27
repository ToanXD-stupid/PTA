# class Cat:
#     # name = ""
#     # age = ""
#     # weight = ""
#     # type = ""
#     # color = ""
#     # sex = ""

# # Ainmal1 = Cat()
# # Animal2 = Cat()
# # Cat.name = "Tom"
# # Cat.age = 3
# # Cat.weight = 4.5
# # Cat.type = "British Shorthair"
# # Cat.color = "Gray"
# # Cat.sex = "Male"

#     def __init__(self, name, age, weight, type, color, sex):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.type = type
#         self.color = color
#         self.sex = sex

# Animal1 = Cat("Tom", 3, 4.5, "British Shorthair", "Gray", "Male")
# print(Animal1.name

class vatnuoi:
    def __init__(self, giong, Mausac, tuoi, CanNang):
        self.giong = giong
        self.Mausac = Mausac
        self.tuoi = tuoi
        self.CanNang = CanNang

vat_nuoi1 = vatnuoi("Chó", "Đen", 3, 10)
print(vat_nuoi1.giong)
print(vat_nuoi1.Mausac)
print(vat_nuoi1.tuoi)
print(vat_nuoi1.CanNang)

vat_nuoi2 = vatnuoi("Mèo", "Trắng", 2, 5)
print(vat_nuoi2.giong)
print(vat_nuoi2.Mausac)
print(vat_nuoi2.tuoi)
print(vat_nuoi2.CanNang)

class people:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

people1 = people("Nguyễn Võ Trường Toản", 15, "Nam", 160, 75)
print(people1.name)
print(people1.age)
print(people1.gender)
print(people1.height)
print(people1.weight)


