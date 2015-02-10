import random

class Pledge:
	name = ''
	listOfPrefs = {}

class Active:
	name = ''
	listOfPrefs = {}
	takingTwo = False

pledgeNames = ['Adya Jain','Aly Wayne','Amanda Brown','Amanda Marks','Amber Michaeli','Ashley Chiu','Casey Zheng','Devin Ryan','EB Byrn','Elizabeth Liechti','Emily Bluedorn','Emily Bross','Emily Garner','Emma Lapin','Erin Gaffaney','Grace Wang','Gwen Clark','Haley Botteron','Hannah Moran','Hannah Oden-Brunson','Hannah Sfreddo','Hayley Talkington','Hillie Sennot','Ivy Zhang','Jenny Lin','Joanna LeFebvre','Julia Osteen','Kate Alexander','Kate Hao','Kelly Andrulis','Kendall Carroll','Lauren Spungen','Lauren Strubbe','Leah Starbuck','Lian Giloth','Lulu Huang','Maddy Drolen','Maria Gilfoyle','MK Mollman','Natalie Golota','Natalie Howard','Nicole Wong','Nicole Zanolli','Noa Yadidi','Rachel Butler','Rae Hung','Samatha Greene','Sarah Jane','Savannah Rush','Shivangi Bhatia','Stacy Curnow','Stephanie Yandow','Sydney Shafer','Tess Gong']
activeNames = ['Alyssa Carruba','Cassie Wang','Vanessa Salazar','Rachel Eun','Charlotte Bourg','Daphne Deng','Ally Hartenstein','Alyse Gellis','Anna Boerwinkle','Anna Garbuzov','Anna Gautier','Ashley Ferguson','Ashley Profozich','Audrey Ball','Becca Bloom','Billie Mandelbaum','Bridget Ahad','Cami Koziatek','Charlotte Young','Cliodhna Dill','Dahlgren Baker','Elizabeth Sak','Ellie Johnson','Emma Fichtel','Erica Achepohl','Erica Sloan','Grace Portelance','Iman Abdikarim','Jamie Zack','Julia Marks','Lauren Berger','Lauren Kliska','Madeline McGraw','Madeline Pensiero','Mary-Brent Brown','Megan Nicklay','Rebecca Feltman-Frank','Saniya Suri','Shoshanah Shanes','Sophia Veksler','Stephanie Mertz','Taylor Maxwell','Zoe Fisch']
pledges = []
actives = []
activeScoreList = {}

for pledge in pledgeNames:
	newPledge = Pledge()
	newPledge.name = pledge

	tempActiveNames = activeNames[:]
	prefList = {}

	for i in range(10):
		rando = int(random.random()*(len(activeNames)-i))
		prefList[tempActiveNames[rando]] = i + 1
		tempActiveNames.pop(rando)
	
	newPledge.listOfPrefs = prefList
	pledges.append(newPledge)

for active in activeNames:
	newActive = Active()
	newActive.name = active

	tempPledgeNames = pledgeNames[:]
	prefList = {}

	for i in range(10):
		rando = int(random.random()*(len(pledgeNames)-i))
		prefList[tempPledgeNames[rando]] = i + 1
		tempPledgeNames.pop(rando)
	
	newActive.listOfPrefs = prefList
	actives.append(newActive)

for i in range(11):
	actives[i].takingTwo = True

for pledge in pledges:
	for active in actives:
		activeScoreList[pledge.name + '+' + active.name] = 0

for pledge in pledges:
	for active in actives:
		if active.name in pledge.listOfPrefs:
			activeScoreList[pledge.name + '+' + active.name] = pledge.listOfPrefs[active.name]
		if pledge.name in active.listOfPrefs:
			activeScoreList[pledge.name + '+' + active.name] = activeScoreList[pledge.name + '+' + active.name] + active.listOfPrefs[pledge.name]

sortedNameList = sorted(activeScoreList, key=activeScoreList.get)
sortedNameList.reverse()
singleCombos = []
twinningCombos = []

for active in actives:
	activeUsed = False
	pledgesToDelete = []
	for combo in sortedNameList:
		if active.name in combo:
			if active.takingTwo is True:
				twinningCombos.append(combo)
				active.takingTwo = False
				for pledge in pledges:
					if pledge.name in combo:
						pledgesToDelete.append(pledge.name)
			elif activeUsed is False:
				singleCombos.append(combo)
				activeUsed = True
				for pledge in pledges:
					if pledge.name in combo:
						pledgesToDelete.append(pledge.name)
	tempSortedNames = sortedNameList[:]
	for pledge in pledgesToDelete:
		for combo in tempSortedNames:
			if pledge in combo:
				sortedNameList.remove(combo)


finalCombos = []

for combo in singleCombos: finalCombos.append(combo)
for combo in twinningCombos: finalCombos.append(combo)
for combo in finalCombos: print combo, activeScoreList[combo]









