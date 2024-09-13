def mars_mission(distance, speed, fuel, crew_ready):
    global time
    #Anything tabde in under def is one function, everything within is only accesible inside that function. 
    #global makes time accessible inside and outside the function. 
    time = distance / speed
    # time = distance / speed
    if speed < 20000:
      print("Warning: Speed is too slow for a timely arrival!")
    elif speed > 500000:
      print("Speed is too fast, may overshoot mars")
    else: 
      print("Speed is optimal for mars mission")

    if fuel < 100:
      print("Warning: Fuel level low, please refuel")
    else: 
      print("Fuel level is optimal")
    if distance < 140:
      print("Warning: Distance is too short, may not be headed to Mars. ")
    elif distance == 140: 
      print("Mission selected")
    else: 
      print("Distance is incorrect for Mars arrival. ")
  
    if crew_ready == True:
      print("Crew is ready for launch")
    else:
      print("Crew is not ready for launch")

    # return time

mars_mission(140, 51000, 141, True)

print("Estimated time travel to mars is:", time, "hours")
