from random import randint
lmartinez = {"name": "Lionel Martinez", "shot": 8}
mcastillo = {'name': "Martin Castillo", 'saves': 7}
ejuarez = {'name': 'Emilio Juarez', 'shot': 8}
mhernandez = {'name': 'Miguel Hernandez', 'saves': 5}
jdelgado = {"name": "Josue Delgado", "shot": 5}
dnogorov = {'name': "Dmitri Nogorov", 'saves': 3}
mhinajosa = {'name': 'Mateo Hinajosa', 'shot': 6}
gkingston = {'name': 'George Kingston', 'saves': 4}
malmonte = {"name": "Marcos Almonte", "shot": 2}
psanchez = {'name': "Pancho Sanchez", 'saves': 2}
clopes = {'name': 'Cristian Lopes', 'shot': 3}
drodriguez = {'name': 'Davien Rodriguez', 'saves': 1}

aragonita = {'goalie': mcastillo, 'striker': lmartinez, 'name': 'CA Aragonita'}
leon = {'goalie': mhernandez, 'striker': ejuarez, 'name': 'CFR Leon'}
vayereicas = {'goalie': dnogorov, 'striker': jdelgado, 'name': 'CF Vayereicas'}
bahia = {'goalie': gkingston, 'striker': mhinajosa, 'name': 'Bahia CF'}
iglesias = {'goalie': psanchez, 'striker': malmonte, 'name': 'Iglesias FC'}
lagoricas = {'goalie': drodriguez, 'striker': clopes, 'name': 'AF Lagoricas'}

def shot(player, goalie):
	if player['shot'] > randint(0,10):
		if goalie['saves'] > randint(0,10):
			return "GOOOL!"
		else:
			return 'Parada!'
	else:
		return "Fuera."

def game(team1, team2):
	score1 = 0
	score2 = 0
	for x in range(0,5):
		if shot(team1['striker'], team2['goalie']) == 'GOOOL!':
			score1 += 1
	for x in range(0,5):
		if shot(team2['striker'], team1['goalie']) == 'GOOOL!':
			score2 += 1
	return "%s %d - %d %s" % (team1['name'], score1, score2, team2['name'])
	
	

	
print game(aragonita, iglesias)
print game(leon, bahia)
print game(vayereicas, lagoricas)


#------------------------------------------------------------

def shot(player, goalie):
	if player['shot'] > randint(0,10):
		if goalie['saves'] > randint(0,10):
			return 'g'
		else:
			return 'p'
	else:
		return 'f'
		



		