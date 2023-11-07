class AquariumApp:

    PRIVATE_SWIM_COUNT = 0

    def __init__(self, fish_count, eye_color, skin_color):
        self.fish_count = fish_count
        self.eye_color = eye_color
        self.skin_color = skin_color
        self.protected_DEAD_FISH = 0


    def start(self):
        if self.fish_count == 0:
            print("There are no alive fish left.")
            return
        self.PRIVATE_SWIM_COUNT += 1

        print(
            f"{self.fish_count} fish are swimming. Their eyes are {self.eye_color} and their skin is {self.skin_color}."
        )
        print(
            f"There are {self.protected_DEAD_FISH} dead fish with them in the aquarium."
        )
        print(f"The fish have now been swimming {self.PRIVATE_SWIM_COUNT} times.")


    def die_fish(self, number):
        if self.fish_count == 0:
            return
       
        if number > self.fish_count:  
            number = self.fish_count 

        self.fish_count -= number
        self.protected_DEAD_FISH += number
            

# Initialize an instance of the class and print some attributes

# Initialize an instance of the class and print some attributes
my_aquarium = AquariumApp(5, "blue", "red")

# for _ in range(3):
#     my_aquarium.start()
#     my_aquarium.die_fish(2)

while my_aquarium.fish_count > 0:
    my_aquarium.start()
    my_aquarium.die_fish(2)
    
print("All fish are dead.")
print("GAME OVER")
#Fish_count= my_aquarium.fish_count
# print(f"Fish_count {Fish_count}")
# # or to make it shorter, we call the instance with its attribute

# print(f"Eye_color: {my_aquarium.eye_color}")
# print(f"Skin color: {my_aquarium.skin_color}")
# my_aquarium.start()
# my_aquarium.die_fish(2)