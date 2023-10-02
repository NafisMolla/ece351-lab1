import statistics
import random_generator
import MM1
import numpy as np
import matplotlib.pyplot as plt

def q1():
    print("this is q1")
    #testing to see if this shit works
    nums = []
    for i in range(1000):
        nums.append(random_generator.generate(75))
        
    mean = statistics.mean(nums)
    variance = statistics.variance(nums)
    print("The exponential random variable mean is: ",mean)
    print("The exponential random variable variance is: ", variance)
    
def q3():
    rho = [0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95]
    avg_packet_data = []
    avg_idle_data = []
    
    average_len_bits = 2000
    transmission_rate = 1000000
    sim_multi = 1
    #we need the sim with all the different rho values
    for r in rho:
        print("current rho is: ---> ", r)
        #creating obj for the mm1
        sim_obj = MM1.MM1(r,average_len_bits,transmission_rate,sim_multi)
        #run the sim
        sim_obj.run_sim()
        #E[N] value
        print("this is the E[N] Value: -> ",sim_obj.en)
        avg_packet_data.append(sim_obj.en)
        #idle value 
        print("this is the idle Value: -> ",sim_obj.idle)
        avg_idle_data.append(sim_obj.idle)
        
    print(avg_packet_data)
    print(avg_idle_data)
    
    # To generate random data for plotting
    axisX = rho
    axisY = avg_packet_data
    # To create the line graph from above data
    plt.plot(axisX, axisY)
    # Adding title and labels for the graph
    plt.title('Line Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    # to show the final graph
    plt.show()
        
        
        
    

def main():
    # q1()
    q3()
    
    
if __name__ == '__main__':
   main()