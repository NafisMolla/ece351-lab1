import random_generator
import event
import numpy as np
import matplotlib.pyplot as plt

class MM1:
    
    def __init__ (self,rho:int,average_len_bit:int,trans_rate:int,sim_time_multiplier:int):
        #rho = l()
        self.rho:int = rho
        #represents the average length of packets arrived per second
        self.lamda:int = rho*(trans_rate/average_len_bit)
        #represents the average length of bits
        self.average_len_bit:int = average_len_bit
        #represents the average  
        self.trans_rate:int = trans_rate
        #how long we want the sim to run for
        self.sim_time:int = 1000 * sim_time_multiplier
        #observer lamda value, we will call it lambda
        self.alpha:int = self.lamda * 5
        #this will hold arrival events 
        self.arrival_event_array = []
        #this will hold observer events
        self.observer_event_array = []
        #this will hold the departure arrival events
        self.departure_event_array = []
        #this is the array that will hold all the events
        self.events = []
        
        
        
        #these variables will be used for the observer
        self.idle = 0
        self.en = 0
        
    #generate arrivals will genearate all the arrival times and poplulate the arrival_even_array
    def generate_arrivals(self) -> None:
        #sim time
        time = 0
        
        while time <= self.sim_time:
            #keep a running count of the total time
            time += random_generator.generate(self.lamda)
            #make a new object that is of type 'ARRIVAL' with a packet length of 1/l
            curr = event.event('ARRIVAL', time,False,random_generator.generate(1/self.average_len_bit))
            #dding the current object we just created to our list of arrival objects
            self.arrival_event_array.append(curr)
            
    
    
    
    #generate observers will genearate 
    def generate_observers(self) -> None:
        #sim time
        time = 0
        
        while time <= self.sim_time:
            #keep a running count of the total time
            time += random_generator.generate(self.alpha)
            #make a new object that is of type 'ARRIVAL'
            curr = event.event('OBSERVER', time)
            #dding the current object we just created to our list of arrival objects
            self.observer_event_array.append(curr)
    
    
    
    #generate departures
    def generate_departures(self) -> None:
        time = 0
        #looping through all the
        for arrivals in self.arrival_event_array:
            
            #if the time of the current arrival we are going through is bigger than the current time we want to move the sim time up
            if arrivals.time > time:
                #moveing sim time up
                time = arrivals.time
                
            #calculate the departure time, currtime + servie time
            departure_time = time + (arrivals.packet_length / self.trans_rate)
            
            #make a new departure event with the new departure time
            self.departure_event_array.append(event.event('DEPARTURE',departure_time))
            
            #move the sim time up to the time where the packet departued
            time = departure_time
            
    #combine all the even arrays into one 
    def concat_events(self):
        self.events = self.arrival_event_array + self.departure_event_array + self.observer_event_array
    #observing events, and updating counters
    def observe_sim_events(self) -> None:
        #this is a sum of the number of packets we observe at each observation event
        '''
        so lets say during our 1st observation we see that theres 10 packets in the queue,
        next obs we see 20 in the queue, and last obs we see 30 packets in the queue
        
        so the average number of items that was in the queue was -> total_packets/observers
        
        '''
        total_packets = 0
        na=0
        nd=0
        no=0
        local_idle = 0
        print(len(self.events))
        for e in self.events:
            if e.event_type == 'ARRIVAL':
                na +=1
            
            elif e.event_type == 'OBSERVER':
                no+=1
                number_of_packets = na - nd
                #empty buffer
                if number_of_packets == 0:
                    local_idle +=1
                    
                total_packets += number_of_packets
            
            else:
                if e.event_type == 'DEPARTURE':
                    nd += 1
                

        #populate the en variables 
        self.en = total_packets / no
        self.idle = local_idle/no
        
    
    #sort array
    def sort_events(self) -> None:
        #sorting by the time attribute
        self.events.sort(key=lambda event: event.time)
    
    #function to run the sim
    def run_sim(self) -> None:
        #generate all the events
        self.generate_arrivals()
        self.generate_observers()
        self.generate_departures()
        
        #add all the arrays together
        self.concat_events()
    
        #sort array so we proccess in a timely manner
        self.sort_events()
        
        #run the sim
        self.observe_sim_events()
        
        
    

if __name__ == '__main__':
   print("this works gang")
