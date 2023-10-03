import heapq
import argparse
class event:
    
    '''
    The event type class is used to represent an event of type arrival, observer or departure
    event_type ->  arrival, observer or departure
    time -> 
    '''
    # Constructor (initialize instance variables)
    def __init__(self, event_type: str, time: int, packet_len: int =None):
        self.event_type = event_type
        self.time = time
        self.packet_length = packet_len # only relevant for arrival events
    
    #this is a function that lets python compare 2 objects of type event
    def __lt__(self, other):
        return self.time < other.time



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Parses .')

    parser.add_argument('question', type=str, help='The name to greet')

    args = parser.parse_args()

    q = args.question
    
    print(q)
    




