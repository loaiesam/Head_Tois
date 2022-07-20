import random
head_times = 0
tois_times = 0
while True:
    start_game = input("Do want to flip the Coin?: ").lower()
    if start_game == "yes":
        while True:
            random_number = random.randint(0, 1)
            if random_number == 1:
                print("Head")
                head_times += 1
            else:
                print("Tois")
                tois_times += 1
            break;
    elif start_game == "no":
        print("You got Head", head_times,"times.")
        print("You got Tois", tois_times,"times.")
        break
    else:
        print("Invalid Mode")
        pass
print("Thank you for playing")
