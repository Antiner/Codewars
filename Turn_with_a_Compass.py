"""You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW)
and a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise,
and negative means counter-clockwise.

Return the direction you will face after the turn.

Examples
"S",  180  -->  "N"
"SE", -45  -->  "E"
"W",  495  -->  "NE" """

side = {"N": 0, "NE": 45, "E": 90, "SE": 135, "S": 180, "SW": 225, "W": 270, "NW": 315}


def direction(facing, turn):
    return [k for k, v in side.items() if v == ((side.get(facing) + turn) % 360)][0]


# Best practice

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


def direction_1(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]


# Clever

com = {"N": 360,
       "NE": 45,
       "E": 90,
       "SE": 135,
       "S": 180,
       "SW": 225,
       "W": 270,
       "NW": 315,
       "NN": 0}


def direction_2(facing, turn):
    if facing == "N":
        x = 360
        if 0 <= turn <= 360:
            x = turn
        elif 360 < turn <= 720:
            y = turn - 360
            x = y
        elif 720 < turn <= 1080:
            y = turn - 720
            x = y
        elif -360 <= turn < 0:
            x = 360 + turn
        elif -720 <= turn < -360:
            x = 720 + turn
        elif -1080 <= turn < -720:
            x = 1080 + turn
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "NE":
        x = 45
        if 0 <= turn <= 360:
            if turn > 315:
                x = (turn + 45) - 360
            elif turn <= 315:
                x = turn + 45
        elif 360 < turn <= 720:
            if turn > 675:
                y = turn - 360
                x = (45 + y) - 360
            elif turn <= 675:
                y = turn - 360
                x = 45 + y
        elif 720 < turn <= 1080:
            if turn > 1035:
                y = turn - 720
                x = (45 + y) - 360
            elif turn <= 1035:
                y = turn - 720
                x = 45 + y
        elif -360 <= turn < 0:
            if turn >= -45:
                x = 45 + turn
            elif turn < -45:
                y = 45 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -405:
                y = 45 + turn
                x = y + 360
            elif turn < -405:
                y = 45 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -765:
                y = 45 + turn
                x = y + 720
            elif turn < -765:
                y = 45 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "E":
        x = 90
        if 0 <= turn <= 360:
            if turn > 270:
                x = (turn + 90) - 360
            elif turn <= 270:
                x = turn + 90
        elif 360 < turn <= 720:
            if turn > 630:
                y = turn - 360
                x = (90 + y) - 360
            elif turn <= 630:
                y = turn - 360
                x = 90 + y
        elif 720 < turn <= 1080:
            if turn > 990:
                y = turn - 720
                x = (90 + y) - 360
            elif turn <= 990:
                y = turn - 720
                x = 90 + y
        elif -360 <= turn < 0:
            if turn >= -90:
                x = 90 + turn
            elif turn < -90:
                y = 90 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -450:
                y = 90 + turn
                x = y + 360
            elif turn < -450:
                y = 90 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -810:
                y = 90 + turn
                x = y + 720
            elif turn < -810:
                y = 90 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "SE":
        x = 135
        if 0 <= turn <= 360:
            if turn > 225:
                x = (turn + 135) - 360
            elif turn <= 225:
                x = turn + 135
        elif 360 < turn <= 720:
            if turn > 585:
                y = turn - 360
                x = (135 + y) - 360
            elif turn <= 585:
                y = turn - 360
                x = 135 + y
        elif 720 < turn <= 1080:
            if turn > 945:
                y = turn - 720
                x = (135 + y) - 360
            elif turn <= 945:
                y = turn - 720
                x = 135 + y
        elif -360 <= turn < 0:
            if turn >= -135:
                x = 135 + turn
            elif turn < -135:
                y = 135 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -495:
                y = 135 + turn
                x = y + 360
            elif turn < -495:
                y = 135 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -855:
                y = 135 + turn
                x = y + 720
            elif turn < -855:
                y = 135 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "S":
        x = 180
        if 0 <= turn <= 360:
            if turn > 180:
                x = (turn + 180) - 360
            elif turn <= 180:
                x = turn + 180
        elif 360 < turn <= 720:
            if turn > 540:
                y = turn - 360
                x = (180 + y) - 360
            elif turn <= 540:
                y = turn - 360
                x = 180 + y
        elif 720 < turn <= 1080:
            if turn > 900:
                y = turn - 720
                x = (180 + y) - 360
            elif turn <= 900:
                y = turn - 720
                x = 180 + y
        elif -360 <= turn < 0:
            if turn >= -180:
                x = 180 + turn
            elif turn < -180:
                y = 180 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -540:
                y = 180 + turn
                x = y + 360
            elif turn < -540:
                y = 180 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -900:
                y = 180 + turn
                x = y + 720
            elif turn < -900:
                y = 180 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "SW":
        x = 225
        if 0 <= turn <= 360:
            if turn > 135:
                x = (turn + 225) - 360
            elif turn <= 135:
                x = turn + 225
        elif 360 < turn <= 720:
            if turn > 495:
                y = turn - 360
                x = (225 + y) - 360
            elif turn <= 495:
                y = turn - 360
                x = 225 + y
        elif 720 < turn <= 1080:
            if turn > 855:
                y = turn - 720
                x = (225 + y) - 360
            elif turn <= 855:
                y = turn - 720
                x = 225 + y
        elif -360 <= turn < 0:
            if turn >= -225:
                x = 225 + turn
            elif turn < -225:
                y = 225 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -585:
                y = 225 + turn
                x = y + 360
            elif turn < -585:
                y = 225 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -945:
                y = 225 + turn
                x = y + 720
            elif turn < -945:
                y = 225 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "W":
        x = 270
        if 0 <= turn <= 360:
            if turn > 90:
                x = (turn + 270) - 360
            elif turn <= 90:
                x = turn + 270
        elif 360 < turn <= 720:
            if turn > 450:
                y = turn - 360
                x = (270 + y) - 360
            elif turn <= 450:
                y = turn - 360
                x = 270 + y
        elif 720 < turn <= 1080:
            if turn > 810:
                y = turn - 720
                x = (270 + y) - 360
            elif turn <= 810:
                y = turn - 720
                x = 270 + y
        elif -360 <= turn < 0:
            if turn >= -270:
                x = 270 + turn
            elif turn < -270:
                y = 270 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -630:
                y = 270 + turn
                x = y + 360
            elif turn < -630:
                y = 270 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -990:
                y = 270 + turn
                x = y + 720
            elif turn < -990:
                y = 270 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    elif facing == "NW":
        x = 315
        if 0 <= turn <= 360:
            if turn > 45:
                x = (turn + 315) - 360
            elif turn <= 45:
                x = turn + 315
        elif 360 < turn <= 720:
            if turn > 405:
                y = turn - 360
                x = (315 + y) - 360
            elif turn <= 405:
                y = turn - 360
                x = 315 + y
        elif 720 < turn <= 1080:
            if turn > 765:
                y = turn - 720
                x = (315 + y) - 360
            elif turn <= 765:
                y = turn - 720
                x = 315 + y
        elif -360 <= turn < 0:
            if turn >= -315:
                x = 315 + turn
            elif turn < -315:
                y = 315 + turn
                x = 360 + y
        elif -720 <= turn < -360:
            if turn >= -675:
                y = 315 + turn
                x = y + 360
            elif turn < -675:
                y = 315 + turn
                x = (y + 360) + 360
        elif -1080 <= turn < -720:
            if turn >= -1035:
                y = 315 + turn
                x = y + 720
            elif turn < -1035:
                y = 315 + turn
                x = (y + 720) + 360
        for key, value in com.items():
            if value == x:
                if value == 0:
                    return "N"
                return key
    return x
