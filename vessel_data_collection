import krpc, time

END_TIME = 300

link = krpc.connect(name="ProjectKSP")


vessel = link.space_center.active_vessel
vessel.control.activate_next_stage()

with open("file1.txt", "w") as file:
    t = 0
    while t < END_TIME:
        if t == 30:
            vessel.control.gear = False
        mass = vessel.mass
        file.write(str(mass) + '\n')
        t += 1
        time.sleep(1)
