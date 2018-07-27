import json;
import requests

#Place API Key here!! You can get one for free at https://developer.riotgames.com
api_key = 'RGAPI-8935f6b9-7eff-4c32-9bef-2611a50b8680'

#Returns JSON object that contains information on the specified 'summoner'.
def getSummonerByName(summonerName):
	print("Running Service: getSummonerByName...")
	url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s' % (summonerName, api_key)
	response = requests.get(url)
	return response.json()

#Returns JSON object that contains information on the specified 'matchList'
def getMatchListByAccountId(accountId):
	print("Running Service: getMatchListByAccountId...")
	url = 'https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/%s?api_key=%s' % (accountId, api_key)
	response = requests.get(url)
	return response.json()


#Returns JSON object that contains information on the specified 'gameId'
def getMatchByGameId(gameId):
	print("Running Service: getMatchByGameId...")
	url = 'https://na1.api.riotgames.com/lol/match/v3/matches/%s?api_key=%s' % (gameId, api_key)
	response = requests.get(url)
	return response.json()

#Returns participantId of specified 'summonerObj' within specified 'game'
#Returns -1 if summoner could not be found in game
def getParticipantId(summonerObj, game):
	#Compares the accountId field to that of each player in the game until a match is found. Then returns participantId of the matching player.
	print("AccountId to Match: ", summonerObj['accountId'])
	#Iterator set to 0 and will loop through at max 10 times. There are only 10 players per match
	i = 0
	for player in game['participantIdentities']:
		if(summonerObj['accountId'] == player['player']['accountId']):
			return i
		i = i + 1

#Returns JSON object that contains per game statistical information for the specified 'participant' in the specified 'game'
def getParticipantStats(participantId, game):
	print("Getting Participant Stats...")
	return game['participants'][participantId]

def sortStats(participantStats):
	try:
		stats = {'championId':participantStats['championId'],'participantId':participantStats['participantId'],'win':participantStats['stats']['win'],'item0':participantStats['stats']['item0'],'item1':participantStats['stats']['item1'],'item2':participantStats['stats']['item2'],'item3':participantStats['stats']['item3'],
			 'item4':participantStats['stats']['item4'],'item5':participantStats['stats']['item5'],'item6':participantStats['stats']['item6'],'kills':participantStats['stats']['kills'], 'deaths':participantStats['stats']['deaths'],
			 'assists':participantStats['stats']['assists'],'longestTimeSpentLiving':participantStats['stats']['longestTimeSpentLiving'],'totalDamageDealt':participantStats['stats']['longestTimeSpentLiving'],
			 'magicDamageDealt':participantStats['stats']['magicDamageDealt'],'physicalDamageDealt':participantStats['stats']['physicalDamageDealt'],'trueDamageDealt':participantStats['stats']['trueDamageDealt'],
			 'totalDamageDealtToChampions':participantStats['stats']['totalDamageDealtToChampions'],'magicDamageDealtToChampions':participantStats['stats']['magicDamageDealtToChampions'],'physicalDamageDealtToChampions':participantStats['stats']['physicalDamageDealtToChampions'],
			 'trueDamageDealtToChampions':participantStats['stats']['trueDamageDealtToChampions'],'totalHeal':participantStats['stats']['totalHeal'],'damageSelfMitigated':participantStats['stats']['damageSelfMitigated'],
			 'damageDealtToObjectives':participantStats['stats']['damageDealtToObjectives'],'damageDealtToTurrets':participantStats['stats']['damageDealtToTurrets'],'visionScore':participantStats['stats']['visionScore'],
			 'timeCCingOthers':participantStats['stats']['timeCCingOthers'],'totalDamageTaken':participantStats['stats']['totalDamageTaken'],'magicalDamageTaken':participantStats['stats']['magicalDamageTaken'],
			 'physicalDamageTaken':participantStats['stats']['physicalDamageTaken'],'goldEarned':participantStats['stats']['goldEarned'],'goldSpent':participantStats['stats']['goldSpent'],'totalMinionsKilled':participantStats['stats']['totalMinionsKilled'],
			 'neutralMinionsKilled':participantStats['stats']['neutralMinionsKilled'],'visionWardsBoughtInGame':participantStats['stats']['visionWardsBoughtInGame'],'wardsPlaced':participantStats['stats']['wardsPlaced'],'wardsKilled':participantStats['stats']['wardsKilled']}
	
		return stats;


	#Error handling for assumed non-summoner's rift game mode
	except KeyError as error:
		print('KeyError has occured because - ', str(error), ' was not found in the JSON to be sorted.')
		print('Trying new parse for assumed non-summoner\'s rift game mode')
		stats = {'championId':participantStats['championId'],'participantId':participantStats['participantId'],'win':participantStats['stats']['win'],'item0':participantStats['stats']['item0'],'item1':participantStats['stats']['item1'],'item2':participantStats['stats']['item2'],'item3':participantStats['stats']['item3'],
			 'item4':participantStats['stats']['item4'],'item5':participantStats['stats']['item5'],'item6':participantStats['stats']['item6'],'kills':participantStats['stats']['kills'], 'deaths':participantStats['stats']['deaths'],
			 'assists':participantStats['stats']['assists'],'longestTimeSpentLiving':participantStats['stats']['longestTimeSpentLiving'],'totalDamageDealt':participantStats['stats']['longestTimeSpentLiving'],
			 'magicDamageDealt':participantStats['stats']['magicDamageDealt'],'physicalDamageDealt':participantStats['stats']['physicalDamageDealt'],'trueDamageDealt':participantStats['stats']['trueDamageDealt'],
			 'totalDamageDealtToChampions':participantStats['stats']['totalDamageDealtToChampions'],'magicDamageDealtToChampions':participantStats['stats']['magicDamageDealtToChampions'],'physicalDamageDealtToChampions':participantStats['stats']['physicalDamageDealtToChampions'],
			 'trueDamageDealtToChampions':participantStats['stats']['trueDamageDealtToChampions'],'totalHeal':participantStats['stats']['totalHeal'],'damageSelfMitigated':participantStats['stats']['damageSelfMitigated'],
			 'damageDealtToObjectives':participantStats['stats']['damageDealtToObjectives'],'damageDealtToTurrets':participantStats['stats']['damageDealtToTurrets'],'visionScore':participantStats['stats']['visionScore'],
			 'timeCCingOthers':participantStats['stats']['timeCCingOthers'],'totalDamageTaken':participantStats['stats']['totalDamageTaken'],'magicalDamageTaken':participantStats['stats']['magicalDamageTaken'],
			 'physicalDamageTaken':participantStats['stats']['physicalDamageTaken'],'goldEarned':participantStats['stats']['goldEarned'],'goldSpent':participantStats['stats']['goldSpent'],'totalMinionsKilled':participantStats['stats']['totalMinionsKilled'],
			 'neutralMinionsKilled':participantStats['stats']['neutralMinionsKilled'],'visionWardsBoughtInGame':participantStats['stats']['visionWardsBoughtInGame']}

		return stats
	
#SummonerName: Name of summoner
#gameNumber: The number of your most recent game (0 for most recent, 1 for second most recent, and so on)
def getStatsFromGame(summonerName,gameNumber):
	summoner = getSummonerByName(summonerName)
	matchList = getMatchListByAccountId(summoner['accountId'])
	game = getMatchByGameId(matchList['matches'][gameNumber]['gameId'])
	participantId = getParticipantId(summoner,game)
	participantStats = getParticipantStats(participantId, game)
	return sortStats(participantStats)

#Returns list of all participant stats in game.
def getGameStats(game):
	
	participantIdentities = game['participantIdentities']
	participantStatList = []

	#Hidden function used to match data blocks with the correct summoner. Appends 'summonerName' key/value to each stat dict.
	def getSummonerNameForStats(stats, iterator):
		if(stats['participantId'] == participantIdentities[iterator]['participantId']):
			stats['summonerName'] = participantIdentities[iterator]['player']['summonerName']

	i = 0
	while(i < 10):
		stats = sortStats(getParticipantStats(i,game))
		getSummonerNameForStats(stats,i)
		participantStatList.append(stats)
		i = i + 1

	print('Participants have been added')
	return participantStatList

