from MM1 import MM1
import heapq
import event

#inheriting from the unbuffered class
class MM1K(MM1):
    def __init__(self, rho, average_len_bit, trans_rate, sim_time_multiplier, buffer_size):
        # Call the constructor of the parent class (MM1)
        super().__init__(rho, average_len_bit, trans_rate, sim_time_multiplier)
        
        # Add any additional attributes specific to MyNewClass
        self.buffer_size = buffer_size
        #even heap for simmulation
        self.event_heap = []
        heapq.heapify(self.event_heap)
        
        self.missed = 0
        
            
    #combine all the even arrays into one 
    def add_items_to_heap(self,arr):
        #adding all the event objects from the arr to the heap
        for i in arr:
            heapq.heappush(self.event_heap,i)
            
    #observing events, and updating counters
    def dynamic_departure_gen(self) -> None:
        #this is a sum of the number of packets we observe at each observation event
        total_packets = 0
        #counter to keep track of arrivals
        na=0
        #counter to keep track of departures
        nd=0
        #counter to keep track of observers
        no=0
        local_idle = 0
        local_missed = 0
        buff_size = 0
        time = 0
        #looping through all the itesm
        while self.event_heap:
            #grab the top event from the heap
            e = heapq.heappop(self.event_heap)
            
            if e.event_type == 'ARRIVAL':
                
                #if there is no space in the buffer
                if buff_size >= self.buffer_size:
                    local_missed +=1
                    
                #there is space in the buffer
                else:
                    #update the counters
                    na +=1
                    buff_size +=1
                    #if the current packet is arriving at time past the current time 
                    if e.time > time:
                        #moveing sim time up so we can serve the packet right awawy
                        time = e.time
                        
                    #calculate the departure time, currtime + servie time
                    departure_time = time + (e.packet_length / self.trans_rate)
                    
                    #make a new departure event with the new departure time
                    heapq.heappush(self.event_heap,(event.event('DEPARTURE',departure_time)))
                    #move the sim time up to the time where the packet departued
                    time = departure_time
            #observer event
            elif e.event_type == 'OBSERVER':
                no+=1
                number_of_packets = na - nd
                #empty buffer we are idle
                if number_of_packets == 0:
                    local_idle +=1
                    
                total_packets += number_of_packets
            #if the event is a departure
            else:
                if e.event_type == 'DEPARTURE':
                    nd += 1
                    buff_size -=1
                

        #populate the en variables 
        self.en = total_packets / no
        self.idle = local_idle/no
        self.missed = local_missed/len(self.arrival_event_array)
        
    
    
    #function to run the sim
    def run_sim(self) -> None:
        #generate all the events
        self.generate_arrivals()
        self.generate_observers()
        
        #add arrivals to heap
        self.add_items_to_heap(self.arrival_event_array)
        
        #add all observers to heap
        self.add_items_to_heap(self.observer_event_array)
        
        
        #run the sim to dynaically generate the times for the
        self.dynamic_departure_gen()
    
#to test functions
if __name__ == '__main__':
   print("this works gang")
   
   tester = MM1K(1,1,1,1,1)
   
   tester.test()
