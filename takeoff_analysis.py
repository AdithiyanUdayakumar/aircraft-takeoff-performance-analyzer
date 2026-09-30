def calculate_takeoff_distance(velocity,acceleration):
    if acceleration <=0:
        raise ValueError("Acceleration must be greater than zero.")
    distance = (velocity ** 2) / (2 * acceleration)
    return distance 