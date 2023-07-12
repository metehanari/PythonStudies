# we will create a sport competition schedule 
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']

for home in teams:
    for away in teams:
        if home != away: #for same team matching error
            print(home + " vs " + away)
        