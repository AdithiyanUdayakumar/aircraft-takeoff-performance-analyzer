def validate_positive( value,name):
    if value<=0:
        raise ValueError(name + "Must be greater than zero.")
    return True 