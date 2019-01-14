import csv


experienced_players = []
non_experienced_players = []
teams = {}


def sorted_players():
	with open('soccer_players.csv', newline = '') as csvfile:
			rows_reader = csv.DictReader(csvfile, delimiter=',')
			rows = list(rows_reader)

			for row in rows:
				if row['Soccer Experience'] == 'YES':
					experienced_players.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))
				else:
					non_experienced_players.append(tuple([row['Name'], row['Soccer Experience'], row['Guardian Name(s)']]))

def teams_list(iter1, iter2):
	first = len(iter1)//3
	second = (2 * len(iter1))//3

	teams["Dragons"] = iter1[:first] + iter2[:first]
	teams["Sharks"] = iter1[first:second] + iter2[first:second]
	teams["Raptors"] = iter1[second:] + iter2[second:]
	return teams

def print_team(team):
	result = ''

	for player in team:
		result += 'Name: ' + player[0] + ' Soccer Experience: ' + player[1] + ' Guardians(s): ' + player[2] + '\n\n'
	return result

def write_file(team_name):
	with open('teams.txt', 'a') as file:
		file.write(f'\n\n\n\t\t\t\t\t\t\t {team_name} \n\n\n')
		file.write(print_team(teams.get(team_name)))

def letter():
	for name, team in teams.items():
		for player in team:
			with open('{}.txt'.format(player[0]), 'a') as file:
				file.write(f''' Dear {player[2]},\n
	{player[0]} has been selected to join the {name} Youth Soccer Team.
	First practice will be next Monday.
	Hope to see you all there!''')
				
				

if __name__ == '__main__':
	sorted_players() 
	teams_list(experienced_players, non_experienced_players)
	print_team(teams)
	write_file('Dragons')
	write_file('Sharks')
	write_file('Raptors')
	letter()