class AquariumApp:
    
    PRIVATE_SWIM_COUNT = 0

    def __init__(self, fish_count, eye_color, skin_color):
        self.fish_count = fish_count
        self.eye_color = eye_color
        self.skin_color = skin_color
        self.protected_DEAD_FISH = 0


# Initialize an instance of the class and print some attributes
my_aquarium = AquariumApp(5, "blue", "red")

Fish_count= my_aquarium.fish_count
print(f"Fish_count {Fish_count}")
# or to make it shorter, we call the instance with its attribute

print(f"Eye_color: {my_aquarium.eye_color}")
print(f"Skin color: {my_aquarium.skin_color}")
