import random
alpha_range = ("a", "b", "c", "d", "e")


for i in range(len(alpha_range)):
    random_number = random.randrange(0,len(alpha_range))
    print(alpha_range[random_number])