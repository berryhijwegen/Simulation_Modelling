
import matplotlib.pyplot as plt
import numpy as np



# Check optimal situation 
# 
# 
def total_harvest():
    maximum_growth_rate = 0.5                       # 1 / year
    carrying_capacity = 2e6                         # tons
    start_fish = 2e5
    MSY = 0.7
    maximum_harvest_rate = MSY * carrying_capacity  # tons / year

    end_time = 10.                                  # end time in years
    h = 0.1                                         # stepsize in years
    num_steps = int(end_time / h)                   # set number of steps
    fish = [start_fish]                             # Initialize total of fish over time with start_fish as t = 0

    results = []

    start_year = 2.

    # Check all combinations of start and end years between the given years
    for ramp_start in np.arange(start_year, end_time + 0.01, 0.5): # +0.01 to prevent issues with roundoff errors
        for ramp_end in np.arange(ramp_start, end_time + 0.01, 0.5):
            is_extinct = False
            total_harvest = 0.
            
            # Calculate harvest factor, which is linear to the current time, then correct harvest_factor based on MSY (harvest_rate)
            for step in range(num_steps):
                time = h * step 
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)
                harvest_rate = harvest_factor * maximum_harvest_rate

                # if a species is extinct it's totals will be constant (0). 
                if is_extinct:
                    fish_next_step = 0.
                    current_harvest = 0.

                # if a species is not extinct, calculate the number of fishes for the next step. This is calculated b
                # + check if species extinct after next calculation.
                else:
                   
                    fish_next_step = fish[step] + change
                    current_harvest = h * harvest_rate
                    if fish_next_step <= 0.:
                        is_extinct = True
                        fish_next_step = 0.
                        current_harvest = fish[step]
                total_harvest += current_harvest
                fish.append(fish_next_step)
            results.append([ramp_start, ramp_end, total_harvest])

    return results

results = total_harvest()

def plot_me():
    plt.scatter([r[0] for r in results], [r[1] for r in results], [5e-11 * r[2]**2. for r in results])
    axes = plt.gca()
    axes.set_xlabel('Start in jaren')
    axes.set_ylabel('Einde in jaren')
    plt.savefig('plots/fish.png')
    plt.show()

plot_me()