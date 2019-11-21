import matplotlib.pyplot as plt

def plot_salt_concentration_over_time(in_speed=6, salt_concentration_in=0.1,\
                        out_speed=6, total_water=1000, total_salt=0, t_end=1000, line_color="-r"):
    # Initialize results array
    times = [0]
    values = [0]

    # Initialize time variable
    t = 0

    while t < t_end:
        # Flow in
        total_water += in_speed
        total_salt += salt_concentration_in * in_speed
        salt_concentration = total_salt / total_water

        # Flow out
        total_water -= out_speed
        total_salt -= salt_concentration * out_speed
        salt_concentration = total_salt / total_water

        # Set new time
        t += 1

        # Add values to results
        times.append(t)
        values.append(salt_concentration)

    # Create the plot
    plt.plot(times, values, line_color, label=f"Out Speed: {out_speed}")

plot_salt_concentration_over_time()
plot_salt_concentration_over_time(out_speed=5, line_color="-y")
plt.legend()
plt.show()
