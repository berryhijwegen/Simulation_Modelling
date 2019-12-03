
import matplotlib.pyplot as plt
import numpy as np

def total_harvest():
    maximum_growth_rate = 0.5 # 1 / year
    carrying_capacity = 2e6 # tons
    MSY = 0.8
    maximum_harvest_rate = MSY * 2.5e5 # tons / year

    end_time = 10. # years
    h = 0.1 # years
    num_steps = int(end_time / h)
    fish = [2e5]

    results = []

    for ramp_start in np.arange(2., 10.01, 0.5): # 10.01 to prevent issues with roundoff errors
        for ramp_end in np.arange(ramp_start, 10.01, 0.5):
            is_extinct = False
            total_harvest = 0.
            for step in range(num_steps):
                time = h * step # years
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)
                harvest_rate = harvest_factor * maximum_harvest_rate

                if is_extinct:
                    fish_next_step = 0.
                    current_harvest = 0.
                else:
                    fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
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
    plt.show()

plot_me()