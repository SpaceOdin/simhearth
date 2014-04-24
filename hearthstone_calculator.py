import sys
import random

#Step 1: Validate Input. We expect a float between 0 and 100
win_percent = sys.argv[1]
initial_star_count = sys.argv[2]

try:
	win_percent = float(win_percent)
	if(win_percent > 100) or (win_percent <= 0):
		raise(ValueError)
except ValueError:
	print "Oops! Win Percent argument was not a valid number. Please use a number between 0 and 100"	

try:
	initial_star_count = int(initial_star_count)
	if(initial_star_count > 95) or (initial_star_count < 0):
		raise(ValueError)
except ValueError:
	print "Oops! Current star count argument was not a valid number. Please use a number between 0 and 95"	

iterations = 100000
#Step 2, simulate the games. We assume that win % stays constant throughout. Every time a 

simulated_games_played = []
simulated_games_won = []
simulated_win_percent = []
simulated_bonus_stars = []

for x in range(0, iterations):
	
	simulated_games_played.append(0)
	simulated_games_won.append(0)
	simulated_win_percent.append(0.0)
	simulated_bonus_stars.append(0)
	win_streak = 0
	star_count = initial_star_count
	while (star_count < 96):
		
		random_number = random.random()
		random_number = random_number * 100
		if (win_percent >= random_number):
			simulated_games_won[x] += 1
			
			simulated_games_played[x] += 1
			win_streak += 1
			#do we add a win streak star?
			if(win_streak >= 3 and star_count < 71):
				star_count += 2
				simulated_bonus_stars[x] += 1
			else:
				star_count += 1
		else:
			
			simulated_games_played[x] += 1
			win_streak = 0
			#do we remove a star?
			if(star_count > 10):
				star_count -= 1
	
	simulated_games_won[x] = float(simulated_games_won[x])
	simulated_games_played[x] = float(simulated_games_played[x])
	
	
	simulated_win_percent[x] = simulated_games_won[x] / simulated_games_played[x]	
	
	

total_played_count = 0
for played_count in simulated_games_played:
	total_played_count += played_count

win_percent_sum = 0
for win_percent_elem in simulated_win_percent:
	#print win_percent_elem
	win_percent_sum += win_percent_elem
#print win_percent_sum	

total_bonus_stars = 0
for bonus_star in simulated_bonus_stars:
	total_bonus_stars += bonus_star

total_win_count = 0
for win_count in simulated_games_won:
	total_win_count += win_count

average_win_count = total_win_count / iterations
average_win_percent = win_percent_sum / iterations
average_played_count = total_played_count / iterations
average_bonus_stars = 0.0
average_bonus_stars = float(total_bonus_stars) / float(iterations)

print "average played count = " + str(average_played_count)
print "average simulated win rate = " + str(average_win_percent)
print "average win count = " + str(average_win_count)
print "average win streak stars = " + str(average_bonus_stars)
print "total bonus stars = " + str(total_bonus_stars)
print str(total_played_count) + " games played in " + str(iterations) + " iterations"	

#print "total played count = " + str(total_played_count)
#print "average played count = " + str(average_played_count)


#resources


# star_rank_dict = {
# 		0 : 25
# 		1 : 25
# 		2 : 25
# 		3 : 24
# 		3 : 24
# 		4 : 24
# 		5 : 23
# 		6 : 23
# 		7 : 22
# 		8 : 22
# 		9 : 21
# 		10 : 21
# 		11 : 20
# 		12 : 20
# 		13 : 20
# 		14 : 19
# 		15 : 19
# 		16 : 19
# 		17 : 18
# 		18 : 18
# 		19 : 18
# 		20 : 17
# 		21 : 17
# 		22 : 17
# 		23 : 16
# 		24 : 16
# 		25 : 16
# 		26 : 15
# 		27 : 15
# 		28 : 15
# 		29 : 15
# 		30 : 14
# 		31 : 14
# 		32 : 14
# 		33 : 14
# 		34 : 13
# 		35 : 13
# 		36 : 13
# 		37 : 13
# 		38 : 12
# 		39 : 12
# 		40 : 12
# 		41 : 12
# 		42 : 11
# 		43 : 11
# 		44 : 11
# 		45 : 11
# 		46 : 10
# 		47 : 10
# 		48 : 10
# 		49 : 10
# 		50 : 10
# 		51 : 9
# 		52 : 9
# 		53 : 9
# 		54 : 9
# 		55 : 9
# 		56 : 8
# 		57 : 8
# 		58 : 8
# 		59 : 8
# 		60 : 8
# 		61 : 7
# 		62 : 7
# 		63 : 7
# 		64 : 7
# 		65 : 7
# 		66 : 6
# 		67 : 6
# 		68 : 6
# 		69 : 6
# 		70 : 6
# 		71 : 5
# 		72 : 5
# 		73 : 5
# 		74 : 5
# 		75 : 5
# 		76 : 4
# 		77 : 4
# 		78 : 4
# 		79 : 4
# 		80 : 4
# 		81 : 3
# 		82 : 3
# 		83 : 3
# 		84 : 3
# 		85 : 3
# 		86 : 2
# 		87 : 2
# 		88 : 2
# 		89 : 2
# 		90 : 2
# 		91 : 1
# 		92 : 1
# 		93 : 1
# 		94 : 1
# 		95 : 1
# 		96 : 'legendary'
# 	}

# def stars_to_rank(star_count):
# 	return star_rank_dict[star_count]

