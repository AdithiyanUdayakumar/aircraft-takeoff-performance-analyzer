def get_aircraft_data():
    mass = float(input("Enter the mass of the aircraft (kg) : "))
    thrust = float(input("Enter the thrust produced by the engine (N) : "))
    wing_area = float(input("Enter wing aera (m^2) : "))
    lift_coefficient = float(input("Enter lift coefficient (CL) : "))
    drag_coefficient = float(input("Enter drag coefficient (DL) : "))
    takeoff_speed = float(input("Enter flight take off speed (m/s) : "))
    if mass <=0:
       print("error: mass should be a positive value")
       exit()
    return mass,thrust,wing_area ,lift_coefficient,drag_coefficient,takeoff_speed

def get_environment_data():
    air_density = float(input("Enter air density  (kg/m^3) : "))
    wind_speed = float(input("Enter wind speed (m/s) : "))
    runway_length = float(input("Enter runway length (m) : "))
    runway_slope = float(input("Enter runway slope (%) : "))
    return air_density,wind_speed,runway_length,runway_slope
