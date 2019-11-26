import matplotlib.pyplot as plt


h = 0.5 # days
contacts_per_day = 86 # people
infection_probability = 0.02 # per contact
latency_time = 2. # days
infectious_time = 5. # days
end_time = 60.0 # days

total_population = 96e6 # people
vaccinated_population = 1e6 # people
exposed_population = 1e5 # people

transmission_coeff = infection_probability * (1/total_population) * contacts_per_day # 1 / day person

num_steps = int(end_time / h) # days
times = [h * num for num in range(num_steps + 1)] # days

def sier_model():
    s = [total_population - vaccinated_population - exposed_population]
    i = [0]
    e = [exposed_population]
    r = [vaccinated_population]


    for step in range(num_steps):
        s2e = h * transmission_coeff * i[step] * s[step]
        e2i = h / latency_time * e[step]
        i2r = h / infectious_time * i[step]

        s.append(s[step] - s2e)
        e.append(e[step] + s2e - e2i)
        i.append(i[step] + e2i - i2r)
        r.append(r[step] + i2r)
        
    return s, i, e, r

s, i, e, r = sier_model()

data = {
    'S' : s,
    'I' : i,
    'E' : e,
    'R' : r
}

for key in data:
    plt.plot(times, data[key], label=key)

plt.legend()
plt.savefig('plot.png')
plt.show()

## Calculate amount of needed vaccines
vaccines_needed = total_population - int((1 / infectious_time) / transmission_coeff)
print(f"vaccines needed = {vaccines_needed:.0f}")
print(f"That's {(vaccines_needed / total_population) * 100:.2f}% of total population.")