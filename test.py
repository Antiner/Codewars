side = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}


def direction(facing, turn):
    return [k for k, v in side.items() if v == ((side.get(facing) + turn) % 360)][0]
