from stream import Stream
from tank import Tank
from system import System

for steps in [10, 50,100, 200, 500]:
    tank_system = System()

    tank1 = Tank('Tank A')
    tank2 = Tank('Tank B', start_salt=20, line_color="-b")

    streams1_in = [Stream(6, 0.2), Stream(1, tank2)]
    streams1_out = [Stream(3, tank1), Stream(4, tank1)]

    for stream in streams1_in:
        tank1.add_stream_in(stream)

    for stream in streams1_out:
        tank1.add_stream_out(stream)

    streams2_in = [Stream(3, tank1)]
    streams2_out = [Stream(1, tank2), Stream(2, tank2)]

    for stream in streams2_in:
        tank2.add_stream_in(stream)

    for stream in streams2_out:
        tank2.add_stream_out(stream)

    tank_system.add_tank(tank1)
    tank_system.add_tank(tank2)

    tank_system.run(steps=steps)