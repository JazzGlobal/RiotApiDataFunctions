import services
import xlwt
from time import sleep

class PlayerStats:

	#Constructor for PlayerStats. Looks up summoner and contains 'matchList'.
	def __init__(self, summonerName):
		self.summonerName = summonerName
		self.summoner = services.getSummonerByName(self.summonerName)
		self.matchList = services.getMatchListByAccountId(self.summoner['accountId'])
	
	#Returns 'matchList'
	def getMatchList(self):
		return self.matchList

	#Returns sorted player stats from specified game
	def getGameFromMatchList(self,gameNumber):
		stats = services.getStatsFromGame(self.summonerName,gameNumber)
		return stats
	#Returns sorted player stats from the last x amount of games.
	#Most useful function. Running this will yield a list of player stats.
	def getGames(self, numberOfGames):
		statList = []
		i = 0
		j = 0

		if(numberOfGames >= 100):
			print('Could not return games because number entered is over 100. Getting last 10 games...')
			return 

		while(i < numberOfGames):
			if(j > 15):
				print('Request Overload. Sleep for 5 seconds...')
				sleep(5)
				j = 0

			print('GETTING GAME',i) 
			game = services.getMatchByGameId(self.matchList['matches'][i]['gameId'])
			participantId = services.getParticipantId(self.summoner,game)
			stats = services.sortStats(services.getParticipantStats(participantId,game))
			statList.append(stats)
			i = i + 1
			j = j + 1

		return statList

def ExportGames(statListObj):
	labels = ['championId', 'participantId', 'win', 'item0', 'item1', 
	'item2', 'item3', 'item4', 'item5', 'item6', 'kills', 'deaths', 
	'assists', 'longestTimeSpentLiving', 'totalDamageDealt', 'magicDamageDealt', 'physicalDamageDealt', 'trueDamageDealt', 
	'totalDamageDealtToChampions', 'magicDamageDealtToChampions', 'physicalDamageDealtToChampions', 'trueDamageDealtToChampions', 'totalHeal', 'damageSelfMitigated', 
	'damageDealtToObjectives', 'damageDealtToTurrets', 'visionScore', 'timeCCingOthers', 'totalDamageTaken', 'magicalDamageTaken', 'physicalDamageTaken', 'goldEarned', 
	'goldSpent', 'totalMinionsKilled', 'neutralMinionsKilled', 'visionWardsBoughtInGame', 'wardsPlaced', 'wardsKilled']

	i = 0
	book = xlwt.Workbook()
	try:
		for games in statListObj:
			name = 'Game %s' % (i + 1)
			print(name)
			ws = book.add_sheet(name)
			j = 0

			for text in labels:
				try:
					ws.write(j,0,labels[j])
					ws.write(j,1,statListObj[i][labels[j]])
					j = j + 1

				except:
					print('Skipping Warding Labels')

			i = i + 1
		book.save('last' + str(i) + 'games.xlsx')

	except TypeError as error:
		print('Could not export games because \' statListObj \' was invalid.')



