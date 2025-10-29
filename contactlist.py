def add_person():
  name=input("name: ")
  age=int(input("age: "))
  email=input("email: ")

  person={"name":name,"age":age,"email":email}
  return person

def display_people(people):
  for i,person in enumerate(people):
   print(i+1,'-',person["name"],person["age"],'|',person["email"],'|',)
def delete_contact(people):
  display_people(people)

  while True:
   number=(input("enter number to delete:"))
   try:
      number=int(number)
      if number<=0 or number>len(people):
       print("invalid number,out of range")
      else:
       break
   except:
     print("invalid input")
  people.pop(number-1)
  print("contact deleted successfully")

def search_contact(people):
  search_name=input("search for name").lower()
  results=[]

  for person in people:
    name=person["name"]
    if search_name in name:
      results.append(person)

  display_people(results)



  
print("hi ,welcome to contact management system")
print()

people=[
    {"name":"kaushik","age":20,"email":"kajshsn"},
    {"name":"krivox","age":28,"email":"kajsn"},
    {"name":"krishna","age":27,"email":"kajshs"},
]

while True: 
    print()
    print("contact list size:",len(people))
    command=input("you can 'Add','Delete','search'or Q for quit:").lower()

    if command=="add":
      person=add_person()
      people.append(person)
      print("person added successfully")
    elif command=="delete":
      delete_contact(people)
    elif command=="search":
      search_contact(people)
    elif command=="q":
      break
    else:
      print("invalid command")

    print(people)