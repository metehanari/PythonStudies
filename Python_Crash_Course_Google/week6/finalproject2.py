def get_event_date(event): # this function is used to sort the events by date
    return event.date 

def current_users(events): # this function is used to get the current users
    events.sort(key=get_event_date) # sort the events by date
    machines = {} # create an empty dictionary
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set() # create a set for each machine
        if event.type == "login":
            machines[event.machine].add(event.user) # add the user to the machine
        elif event.type == "logout":
            machines[event.machine].remove(event.user) # remove the user from the machine  
    return machines                         

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users) # join all the users in the set
            print("{}: {}".format(machine, user_list)) # print the machine and the users