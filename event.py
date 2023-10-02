class event:
    
    '''
    The event type class is used to represent an event of type arrival, observer or departure
    event_type ->  arrival, observer or departure
    time -> 
    '''
    # Constructor (initialize instance variables)
    def __init__(self, event_type: str, time: int, was_dropped: bool = False,packet_len: int =None):
        self.event_type = event_type
        self.time = time
        self.dropped = was_dropped  # only relevant for arrival events
        self.packet_length = packet_len # only relevant for arrival events



if __name__ == '__main__':
    x = event("arrival",20)
    print(x.time)