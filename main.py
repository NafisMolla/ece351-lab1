import statistics
import random_generator
import MM1
import numpy as np
import matplotlib.pyplot as plt
import MM1K
import argparse


def q1():
    print("---------------------------------------------")
    
    print("Running Q1")
    #testing to see if this shit works
    nums = []
    for i in range(1000):
        nums.append(random_generator.generate(75))
        
    mean = statistics.mean(nums)
    variance = statistics.variance(nums)
    print("The exponential random variable mean is: ",mean)
    print("The exponential random variable variance is: ", variance)
    print("Q1 Done")
    
def q3():
    print("---------------------------------------------")
    print("Running Q3")
    
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
    plt.title('rho vs E[N] (3.1)')
    plt.xlabel('rho')
    plt.ylabel('E[N]')
    # to show the final graph
    plt.savefig('images/Question3-1', bbox_inches='tight')
    plt.close()
    
    axisX = rho
    axisY = avg_idle_data
    # To create the line graph from above data
    plt.plot(axisX, axisY)
    # Adding title and labels for the graph
    plt.title('Rho vs P-Idle (3.2)')
    plt.xlabel('rho')
    plt.ylabel('P-idle')
    # to show the final graph
    plt.savefig('images/Question3-2', bbox_inches='tight')
    plt.close()
    
    print("---------------------------------------------")
    
    
    
def q4():
    print("---------------------------------------------")
    print("running Q4")
    
    rho = [1.2]
    packet_data = []
    idle_data = []
    
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
        packet_data.append(sim_obj.en)
        #idle value 
        idle_data.append(sim_obj.idle)
        
    print(packet_data)
    print(idle_data)
    
    # To generate random data for plotting
    axisX = rho
    axisY = packet_data
    # To create the line graph from above data
    plt.plot(axisX, axisY)
    # Adding title and labels for the graph
    plt.title('Rho vs E[N] (4)')
    plt.xlabel('rho')
    plt.ylabel('E[N]')
    # to show the final graph
    plt.savefig('images/Question4', bbox_inches='tight')
    
    print("---------------------------------------------")
    
    
def q6():
    print("---------------------------------------------")
    print("running Q6")
    rho_values = [0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]
    p_loss_data = []
    avg_packets_data = []
    k_vals = [5, 10, 40]
    
    L = 2000
    C = 1000000

    for k in k_vals:
        e_n_at_k = []
        loss_at_k = []
        for rho in rho_values:
            print("current rho is: ---> ", rho)
            sim_obj = MM1K.MM1K(rho, L,C,1,k)
            sim_obj.run_sim()
            e_n_at_k.append(sim_obj.en)
            loss_at_k.append(sim_obj.missed)
        
        p_loss_data.append(e_n_at_k)
        avg_packets_data.append(loss_at_k)
        
    
    
    # Graph 6.1
    plt.title("E[N] vs Rho")
    plt.xlabel('Rho Values')
    plt.ylabel('E[N]')
    for i in avg_packets_data:
        plt.plot(rho_values, i)
    plt.legend(['k = 5', 'k = 10', 'k = 40'], loc = 'upper left')
    # plt.show()
    plt.savefig('images/Question6-1.png', bbox_inches='tight')
    plt.close()
    
    # Graph 6.2
    plt.title("PLoss vs Rho Vals")
    plt.xlabel('Rho Value')
    plt.ylabel('Proportional Loss')
    for i in p_loss_data:
        plt.plot(rho_values, i)
    plt.legend(['k = 5', 'k = 10', 'k = 40'], loc = 'upper left')
    # plt.show()
    plt.savefig('images/Question6-2.png', bbox_inches='tight')
    plt.close()
    
    
    print("---------------------------------------------")

    

def main():
    #parsing arguments
    parser = argparse.ArgumentParser(description='enter which question you would like to simmulate.')
    parser.add_argument('question', type=str, help='The name to greet')
    args = parser.parse_args()
    q = args.question
    
    if q == "q1":
        q1()
        print("done running Sim!!!")
    if q == "q3":
        q3()
        print("done running Sim!!!")
    if q == "q4":
        q4()
        print("done running Sim!!!")
    if q == "q6":
        q6()
        print("done running Sim!!!")
    if q == "":
        print("running all of the Questions")
        q1()
        q3()
        q4()
        q6()
        print("done running Sim!!!")
    
    
    
if __name__ == '__main__':
   main()