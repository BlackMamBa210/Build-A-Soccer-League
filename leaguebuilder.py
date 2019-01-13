#import csv file
#read from csv file
import csv

#create empty lists to sort players
experienced_players = []
non_experienced_players = []

#create a function to read from file
def sorted_players():
	with open('soccer_players.csv', newline = '') as csvfile:
			rows_reader = csv.DictReader(csvfile, delimiter=',')
			rows = list(rows_reader)

	for row in rows:
		if row['Soccer Experience'] == 'YES':
			experienced_players.append([row['Name'], row['Soccer Experience']])
		else:
			non_experienced_players.append([row['Name'], row['Soccer Experience']])
	print(experienced_players)
	print(non_experienced_players)

with open('teams.txt', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'soccer_experience', 'team']
    team_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    team_writer.writeheader() #create a dict and pack it with the teams first name, last name, experience and teams
    team_writer.writerow({
    })

if __name__ == '__main__':
	sorted_players() #then I need to print out the teams and write them to the teams.txt file
