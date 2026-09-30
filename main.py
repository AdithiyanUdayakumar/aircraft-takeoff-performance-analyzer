from input_handler import get_aircraft_data , get_environment_data
from calculations import(
    calculate_dynamic_pressure,
    calculate_lift ,
    calculate_drag,
    calculate_net_force,
    calculate_acceleration

)

from takeoff_analysis import calculate_takeoff_distance
from runway_analysis import analyze_runway
from report import display_report


def main():

    print("=" * 50)
    print("       AIRCRAFT TAKEOFF PERFORMANCE")
    print("                 ANALYZER")
    print("=" * 50)

    print("\nEnter Aircraft information")
    print("-"*50)
    (
        mass,
        thrust,
        wing_area,
        lift_coefficient,
        drag_coefficient,
        takeoff_speed
    ) = get_aircraft_data()

    print("\nEnter Environment and Runway Information")
    print("-" * 50)

    (
        air_density,
        wind_speed,
        runway_length,
        runway_slope
    ) = get_environment_data()

    # Aerodynamic calculations
    dynamic_pressure = calculate_dynamic_pressure(
        air_density,
        takeoff_speed
    )

    lift = calculate_lift(
        dynamic_pressure,
        wing_area,
        lift_coefficient
    )

    drag = calculate_drag(
        dynamic_pressure,
        wing_area,
        drag_coefficient
    )

    # Takeoff calculations
    net_force = calculate_net_force(
        thrust,
        drag
    )

    acceleration = calculate_acceleration(
        net_force,
        mass
    )
    if acceleration<0:
        print("error:acceleration can't be negative")
        exit()

    required_runway = calculate_takeoff_distance(
        takeoff_speed,
        acceleration
    )

    # Runway analysis
    safety_margin, assessment = analyze_runway(
        runway_length,
        required_runway
    )

    # Display final report
    display_report(
        mass,
        thrust,
        takeoff_speed,
        dynamic_pressure,
        lift,
        drag,
        acceleration,
        required_runway,
        runway_length,
        safety_margin,
        assessment
    )


if __name__ == "__main__":
    main()