
# FORMAT OF CHORD (3 ONLY)
FORMAT_MAJOR =  [0, 4, 7]
FORMAT_MINOR =  [0, 3, 7]

# index of keynote
INDEX_KEYNOTE = 0

# RESULT VALUE IN CHECKING MAJOR, MINOR
IS_MAJOR =      1
IS_MINOR =      0
IS_ERROR =      -1

# NOTE LIST
NOTE_A =        0

NOTE_A_SHARP =  1
NOTE_B_FLAT =   1

NOTE_B =        2
NOTE_C_FLAT =   2

NOTE_B_SHARP =  3
NOTE_C =        3

NOTE_C_SHARP =  4
NOTE_D_FLAT =   4

NOTE_D =        5

NOTE_D_SHARP =  6
NOTE_E_FLAT =   6

NOTE_E =        7

NOTE_E_SHARP =  8
NOTE_F =        8

NOTE_F_SHARP =  9
NOTE_G_FLAT =   9

NOTE_G =        10

NOTE_G_SHARP =  11
NOTE_A_FLAT =   11


def generate_chord(type, chord):
    if type == "major":
        new_format = [(note+chord)%12 for note in FORMAT_MAJOR]
        return new_format
    elif type == "minor":
        new_format = [(note+chord)%12 for note in FORMAT_MINOR]
        return new_format

def __change_to_real_value(chord):
    # 정확한 으뜸음 계산을 위해 값 조정
    if chord[INDEX_KEYNOTE] > chord[INDEX_KEYNOTE+1]:
        chord[INDEX_KEYNOTE+1] += 12
        chord[INDEX_KEYNOTE+2] += 12
    elif chord[INDEX_KEYNOTE+1] > chord[INDEX_KEYNOTE+2]:
        chord[INDEX_KEYNOTE+2] += 12

def __reset_chord_value(chord):
    # __change_to_real_value의 반대
    for idx in range(0, len(chord)):
        chord[idx] %= 12

def __check_major_or_minor(chord):

    # Must Setting to real value (use change_to_real_value before using this)
    interval_of_chord = [
        (chord[INDEX_KEYNOTE+1] - chord[INDEX_KEYNOTE]),
        (chord[INDEX_KEYNOTE+2] - chord[INDEX_KEYNOTE+1])
    ]
    interval_of_major = [
        (FORMAT_MAJOR[INDEX_KEYNOTE+1] - FORMAT_MAJOR[INDEX_KEYNOTE]),
        (FORMAT_MAJOR[INDEX_KEYNOTE+2] - FORMAT_MAJOR[INDEX_KEYNOTE+1])
    ]
    interval_of_minor = [
        (FORMAT_MINOR[INDEX_KEYNOTE+1] - FORMAT_MINOR[INDEX_KEYNOTE]),
        (FORMAT_MINOR[INDEX_KEYNOTE+2] - FORMAT_MINOR[INDEX_KEYNOTE+1])
    ]
    
    if interval_of_chord == interval_of_major:
        return IS_MAJOR
    elif interval_of_chord == interval_of_minor:
        return IS_MINOR
    else:
        return IS_ERROR


""" BASIC FUNCTIONS """
def parrel(chord):

    __change_to_real_value(chord)
    
    chord_type = __check_major_or_minor(chord)
    if chord_type == IS_MAJOR:
        # 3음을 1반음 내려서 Minor로 만든다
        chord[INDEX_KEYNOTE+1] -= 1
        __reset_chord_value(chord)
        return True

    elif chord_type == IS_MINOR:
        # 3음을 1반음 올려서 Major로 만든다
        chord[INDEX_KEYNOTE+1] += 1
        __reset_chord_value(chord)
        return True

    else:
        return False

def relative(chord):
    __change_to_real_value(chord)
    chord_type = __check_major_or_minor(chord)

    if chord_type == IS_MAJOR:
        pass

def leading_tone(chord):
    pass


""" MUSIC FUNCTION """

if __name__ == "__main__":
    major_chord_list = [generate_chord("major", idx) for idx in range(0, 12)]
    for chord in major_chord_list:
        parrel(chord)
        print(chord)

