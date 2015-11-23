import itertools
import pandas as pd

def getDistance(hall,team):
	distances=pd.read_csv('data/distances.csv')
	return  distances[(distances.team==team)][hall]

def permutations(iterable, r=None):
	result=[]
	pool = tuple(iterable)
	n = len(pool)
	r = n if r is None else r
	for indices in itertools.product(range(n), repeat=r):
		if len(set(indices)) == r:
			result.append(  tuple(pool[i] for i in indices))
	return result

teams=pd.read_csv('data/teams.csv')
dfHalls=pd.read_csv('data/halls.csv')
divisions= pd.unique(teams.division.ravel())
halls=dfHalls.hall.tolist()

# For each division create a dictionary, to sum distances of all teams for each hall
# So for div1 sum of distance is 10, for div2 sum of distance is 15
# distanceDics=[{x:10}{x:15}]
distanceDics = [dict() for x in range(len(divisions))]

i=0
for div in divisions:
	for hall in halls:	
		for index, row in teams.iterrows():
			if row.division==div:
				teamname=row.teamname
				if hall in distanceDics[i]:
					distanceDics[i][hall]+=int(getDistance(hall,teamname))
				else:
					distanceDics[i][hall]=int(getDistance(hall,teamname))	
	i+=1

# each permutation has a hall assigned to each division
# (x,y,x) means div1=x, div2=y, etc.
perms=permutations(halls, len(divisions))

endResult=[]

for p in perms:
	i=0
	distance=0
	for div in p:
		distance+=distanceDics[i][div]
		i+=1
	endResult.append(distance)

minimum=min(endResult)
maximum=max(endResult)
i=0
count=1
for item in endResult:
	if item==minimum:
		finalResult=perms[i]
		j=0
		print "Result: "+str(count)
		for div in finalResult:
			print "Division: "+str(j)+" plays in hall: "+div
			j+=1
		count+=1
	i+=1
print "Minimum distance is: "+str(minimum)
print "Max distance is: "+str(maximum)