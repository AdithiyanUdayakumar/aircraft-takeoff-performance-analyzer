def calculate_dynamic_pressure(air_density,velocity):
    q = 0.5 * air_density * velocity ** 2
    return q 

def calculate_lift(dynamic_pressure,air_density,lift_coefficient):
    lift = dynamic_pressure * air_density * lift_coefficient 
    return lift 

def calculate_drag(dynamic_pressure,wing_aera, drag_coefficient):
    drag = dynamic_pressure * wing_aera * drag_coefficient
    return drag 

def calculate_net_force(thrust,drag):
    net_force = thrust - drag 
    return net_force 

def calculate_acceleration(net_force,mass):
    acceleration = net_force / mass
    return acceleration