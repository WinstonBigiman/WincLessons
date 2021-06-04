# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, tod, cowmilk_status, location_of_cows, season, slurry_tank, grass_status):
        
        

        if (weather == "rainy" and location_of_cows == "pasture") or (tod == "night" and location_of_cows == "pasture"):# or (location_of_cows == "pasture" and cowmilk_status ==True):
            print("Conditie 1")
            return "take cows to cowshed" 
        
        elif cowmilk_status == True and location_of_cows == "cowshed":
            print("Conditie 2")
            return "milk cows"

        elif cowmilk_status == True and location_of_cows == "pasture":
            print("Conditie 2-1")
            return '''Take cows to cowshed\nMilk cows\nTake cows back to pasture'''
                
        
        elif slurry_tank == True and location_of_cows == "cowshed" and weather != "sunny" and weather != "windy":
            print("Conditie 3")
            return "fertilize pasture"
        elif slurry_tank == True and location_of_cows == "pasture" and weather != "sunny" and weather != "windy":
            print("Conditie 3-1")
            return '''Take cows to cowshed\nFertilize pasture\nTake cows back to pasture'''
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "cowshed":
            print("Conditie 4")
            return "mow grass"
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture":
            print("Conditie 4-1")
            return '''Take cows to cowshed
                    Mow grass
                    Take cows back to pasture'''

        else: 
            print("Conditie 5")
            return "wait"


print(farm_action("sunny", "day", True, "pasture", "spring", False, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
print(farm_action('bowling', 'night', False, 'cowshed', 'winter', False, True))
print(farm_action('sunny', 'night', True, 'cowshed', 'summer', False, True))