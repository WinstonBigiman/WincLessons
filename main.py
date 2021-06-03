# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, tod, cowmilk_status, location_of_cows, season, slurry_tank, grass_status):
        if (weather == "rainy" and location_of_cows == "pasture") or (tod == "night" and location_of_cows == "pasture"):
            print("take cows to cowshed")
            return "take cows to cowshed" 
        
        if cowmilk_status == True and location_of_cows == "cowshed":
            print("milk cows")
            return "milk cows"

        elif cowmilk_status == True and location_of_cows == "pasture":
            #print("""Take cows tot cowshed\nMilk cows\nBring cows back to pasture""")
            return """Take cows tot cowshed\nMilk cows\nTake cows back to pasture""" 
            
        
        elif slurry_tank == True and location_of_cows == "cowshed" and weather != "sunny" and weather != "windy":
            print("fertilize pasture")
            return "fertilize pasture"
        elif slurry_tank == True and location_of_cows == "pasture" and weather != "sunny" and weather != "windy":
            print("""Bring cows tot cowshed\nFertilize pasture\nBring cows back to pasture""")
            return """Bring cows tot cowshed\nFertilize pasture\nBring cows back to pasture"""
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "cowshed":
            print("mow grass")
            return "mow grass"
        elif grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture":
            print("""Bring cows tot cowshed\nMow grass\nBring cows back to pasture""")
            return """Bring cows tot cowshed
                    Mow grass
                    Bring cows back to pasture"""

        else: 
            print("wait")
            return "wait"


print(farm_action("sunny", "day", True, "pasture", "spring", False, True))