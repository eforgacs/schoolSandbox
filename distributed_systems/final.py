def read():
    if not (concurrent with another write) and not (concurrent with failed operation):
        return last value written
    else:
        return last / concurrent value

def write():
    2 message round trips, for read and read/repair
