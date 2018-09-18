time = int(input("Time Spent on Road: "))
acceleration = int(input("Acceleration: "))
distance = int(input("Distance: "))
duration = 0

speed = acceleration * time

while  duration <= time:
    print("duration",duration,"distance: ","*" * int(acceleration * duration * duration * 0.5* 0.1))
    duration = duration + 1

actualdistance = acceleration * time * time * 0.5

if speed > 60:
    print("The​ ​person​ ​went​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was",speed, "m/s)")

if speed < 60:
    print("The​ ​person​ ​went​ ​over​ ​the​ ​speed​ ​limit.​ ​(Max​ ​speed​ ​was", speed, "m/s)")

if actualdistance >= distance:
    print("The​ ​person​ ​reached​ ​the​ ​destination.​ ​(Reached",actualdistance, "m)")

if actualdistance < distance:
    print("The​ ​person​ did not​ reach​ ​the​ ​destination.​ ​(Reached",actualdistance, "m)")