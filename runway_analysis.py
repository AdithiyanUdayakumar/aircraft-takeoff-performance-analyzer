def calculate_safety_margin(available_runway,required_runway):
    safety_margin = available_runway - required_runway
    return safety_margin

def analyze_runway(available_runway,required_runway):
    safety_margin = calculate_safety_margin(available_runway,required_runway)

    if safety_margin >= 0:
        assessment = "SUFFICIENT RUNWAY"
    else:
        assessment = "INSUFFICIENT RUNWAY"
    return safety_margin,assessment

    