import random

user_choice = 0
user_score = 0
door = 5
ghost = 0

print("Правила,")
print("Задача гравця не попасти на очі привиду!.","Гравець не може обрати більще пяти дверей!")

while True:
  if user_choice > door:
    print("Error!")
  else:
# Виводимо наші двері
    for i in range(door):
     print("[" + str(i+1) + "]")
#Обираемо двері для привида
  ghost = random.randint(1,door)
#Користувач обирае двері!
  user_choice = int(input("Оберіть двері: "))
#Виводимо відкриті двері
  for i in range(1,door+1):
    if i != ghost:
      print("[ ]")

    else:
      print("[G]")
#Перевіряемо чи був привид за дверима
  if user_choice == ghost:
    print("Ви програли!")
  
    break
  else:
    user_score = user_score + 1
    print("----!New Match!----" )
    
print("________________________")
print(f"Ваш рахунок: {user_score}")
   