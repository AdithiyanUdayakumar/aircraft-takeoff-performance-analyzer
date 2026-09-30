def display_report(
    mass,
    thrust,
    takeoff_speed,
    dynamic_pressure,
    lift,
    drag,
    acceleration,
    required_runway,
    available_runway,
    safety_margin,
    assessment

):
    print("\n")
    print("="*50)
    print("      AIRCRAFT TAKEOFF PERFORMANCE")
    print("               ANALYZER")
    print("="*50)      


    print("\nAIRCRAFT DATA")
    print("-" * 50)
    print(f"Aircraft mass       : {mass : } kg")
    print(f"Engine thrust       : {thrust : } N ")
    print(f"Takeoff speed       : {takeoff_speed : } m/s")

    print("\nAERODYNAMIC RESULTS")
    print("="*50)
    print(f"Dynamic pressure    : {dynamic_pressure : } pa")
    print(f"lift                : {lift : } N")
    print(f"drag                : {drag : } N")

    print("\nTAKEOFF PERFFORMANCE")
    print("-"*50)
    print(f"Accelerstion        : {acceleration : } m/s^2")
    print(f"Rquired runway      : {required_runway :} m ")

    print("\nRUNWAY ANALYSIS")
    print("-"*50)
    print(f"Available Runway    : {available_runway : } m")
    print(f"Safety Margin       : {safety_margin :} m")
    print(f"Assessment          : {assessment}")

    print("=" * 50)