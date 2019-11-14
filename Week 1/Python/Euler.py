import numpy
import matplotlib.pyplot

def forward_euler():
    h=0.01
    g=9.81
    friction = 0.1
    stretch = 8

    num_steps = 100
    t = numpy.zeros(num_steps+1)
    x = numpy.zeros(num_steps+1)
    v = numpy.zeros(num_steps+1)

    x[0] = 5
    for step in range(num_steps):
        t[step+1] = t[step] + h
        x[step+1] = x[step] + v[step]*h
        v[step+1] = v[step] - friction * v[step] - stretch * x[step]
    return t,x,v

t,x,v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()

plot_me()