# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1
example_1 = "Ruud Gullit"
example_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = example_1 + " " + str(goal_0) + ", " + example_2 + " " + str(goal_1)
print (scorers)
#report = ((example_1) + "scored in the " + str(goal_0) + "nd minute, " + (example_2) + "scored in the " + str(goal_1) + "th minute")
report = example_1 + " scored in the " + str(goal_0) + "nd minute\n" + example_2 + " scored in the " + str(goal_1) + "th minute"
print (report)
# Part 2
player = "Gerald Vanenburg"
# a = player.find(" "[:])
first_name = player[0:(player.find(" "))]
#print (first_name)
# 2.3
last_name_len = len(player[(player.find(" "))+1:])
#print (last_name_len)
# 2.4
name_short = f'{player[0]}. {player[player.find(" ")+1:]}'
print(name_short)
# 2.5
chant = f'{player[0:player.find(" ")]}! '*player.find(" ")
chant = chant.rstrip()
print (chant)
good_chant = chant[-1] != " "
print (good_chant)



