#Dictionary
# hlo={
#     'A':'Clean',
#     'B':'Dirty'
# }
# hlo['A']

# vacuum clean
import numpy as np 

rooms=np.array(['A','B'])
states=np.array(['clean','dirty'])

def choose_room():
    return np.random.choice(rooms)

print(choose_room())

def choose_state():
    return np.random.choice(states)

print(choose_state())

def clean_room():
    room_states={} #Dictionary 
    # for i in range (for loop in python)
    for room in rooms:
        room_states[room]=choose_state()
    print(room_states)


    vacuum_pos=choose_room()
    print('Vaccum Position:',vacuum_pos)
    cost=0
    for i in range(len(rooms)):
    
        if room_states[vacuum_pos]=='dirty':
         print(vacuum_pos,'is dirty')
         print(f'Cleaning {vacuum_pos}.')
         print('================================================')
         room_states[vacuum_pos]='Clean'
         print(f'{vacuum_pos} is cleaned.')
         print('================================================')
         cost+=1
        else: 
         print(f'{vacuum_pos} is cleaned.')
         print('No operation')

        other_rooms= list(set(rooms)-set(vacuum_pos))
        #print (other_rooms)
        vacuum_pos=other_rooms[0]
        if i==0:
           cost+=1
    print(f'final room state{room_states}')
    print('Both rooms cleanes, stop')
    print('cost',cost)   

clean_room()


