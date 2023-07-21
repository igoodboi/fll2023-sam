from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Initialize a motor on port A.
lmotor = Motor(Port.A)
rmotor = Motor(Port.B)

# Make the motor run clockwise at 500 degrees per second.
lmotor.run(500)
rmotor.run(500)

# Wait for three seconds.
wait(3000)

# Make the motor run counterclockwise at 500 degrees per second.
lmotor.run(-500)
rmotor.run(-500)

# Wait for three seconds.
wait(3000)
print('doyee')
