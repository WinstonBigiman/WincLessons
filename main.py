# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, tod, cowmilk_status, location_of_cows, season, slurry_tank, grass_status):
        
        if location_of_cows == "cowshed" and cowmilk_status == True:
             return "milk cows"

        elif (weather == "rainy" and location_of_cows == "pasture") or (tod == "night" and location_of_cows == "pasture"):
            #print("take cows to cowshed")
            return "take cows to cowshed" 
        
        #elif cowmilk_status == True and location_of_cows == "cowshed":
            #print("milk cows")

           

            
        elif cowmilk_status == True and location_of_cows == "pasture":
            #print("""Take cows to cowshed\nMilk cows\nBring cows back to pasture""")
            return '''Take cows to cowshed\nMilk cows\nTake cows back to pasture'''
            
        
        elif slurry_tank == True and location_of_cows == "cowshed" and weather != "sunny" and weather != "windy":
            #print("fertilize pasture")
            return "fertilize pasture"
        elif slurry_tank == True and location_of_cows == "pasture" and weather != "sunny" and weather != "windy":
            #print("""Bring cows tot cowshed\nFertilize pasture\nBring cows back to pasture""")
            return """Take cows to cowshed\nFertilize pasture\nTake cows back to pasture"""
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "cowshed":
            #print("mow grass")
            return "mow grass"
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture":
            #print("""Bring cows tot cowshed\nMow grass\nBring cows back to pasture""")
            return """Take cows to cowshed
                    Mow grass
                    Take cows back to pasture"""

        else: 
            #print("wait")
            return "wait"


print(farm_action("sunny", "day", True, "cowshed", "spring", False, True))
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
#print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
#$print(farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
#print(farm_action('bowling', 'night', False, 'cowshed', 'winter', False, True))
#print(farm_action('sunny', 'night', True, 'cowshed', 'summer', False, True))