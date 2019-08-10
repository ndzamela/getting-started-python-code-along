# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data =yaml.load(f)
#data

# Find data type of the file
print(type(data))

# In which city, and at which venue the match was played and where was it played ?
city = data['info']['city']
print("City where the match was played " + city)
#print("type of city varable: " + str(type(city)))
venue = data['info']['venue']
print("Venue where the match was played: " + venue)

# Which are all the teams that played in the tournament ? How many teams participated in total?
teams = data['info']['teams']
#print(type(teams))
#print(teams[0])
#print(teams([1])
print("Teams participated are: " + teams[0] + " and " + teams [1])
 
print("There are a total of: " + str(len(teams)) + " teams ")
# Which team won the toss and what was the decision of toss winner ?
toss_winner = data['info']['toss']['winner']
toss_decision = data['info']['toss']['decision']
print("Team that won toss: " + toss_winner + " by " + toss_decision)

# Find the first bowler and first batsman who played the first ball of the first inning
first_bowler = data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler']
first_batsman = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']

print("First bowler who delivered the first ball of the first inning: " + first_bowler)
print("First batsman who faced the first ball of the first inning: " + first_batsman)

# How many deliveries were delivered in second inning ?
deliveries = len(data['innings'][0]['1st innings']['deliveries'])

print("First inning was consisting of " + str(deliveries) + " deliveries delivered")

deliveries_2 = len(data['innings'][1]['2nd innings']['deliveries'])

print("Second inning was consisting of " + str(deliveries_2) + " deliveries delivered")

# Which team won and how ?
runs = data['info']['outcome']['by']['runs']
winner = data['info']['outcome']['winner']

print("The team that won the tournament is: " + winner + " by: " + str(runs) + " runs")
print( "winner: ", runs)

print(data['info'][list(data['info'].keys())[-1]])
print(data['info']['venue'])




