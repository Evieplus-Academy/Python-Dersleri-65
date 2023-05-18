from models import Person, Post

person1 = Person(name="Mustafa Çolakoğlu", age=25)
print(person1)
person1.save()

person2 = Person(name="Ezgi Özgür", age=25)
print(person2)
person2.save()

person3 = Person(name="Nail Çolakoğlu", age=25)
print(person3)
person3.save()

person = Person.objects.get(pk=1)
person.age = 26
print(person)
person.save()

print()
persons = Person.objects.all()
for person in persons:
    print(person)

post1 = Post(title="Deneme Başlık", content="Deneme İçerik")
print(post1)
post1.save()