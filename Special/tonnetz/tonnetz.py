
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
    if chord[INDEX_KEYNOTE] > chord[INDEX_KEYNOTE+1]:
        chord[INDEX_KEYNOTE+1] += 12
        chord[INDEX_KEYNOTE+2] += 12
    elif chord[INDEX_KEYNOTE+1] > chord[INDEX_KEYNOTE+2]:
        chord[INDEX_KEYNOTE+2] += 12

def __reset_chord_value(chord):
    # __change_to_real_value의 반대
    for idx in range(0, len(chord)):
        chord[idx] = chord[idx] % 12

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
        """5음을 2반음 올린 다음 5음을 맨 앞으로 이동해서 으뜸으로 설정
            [0, 4, 7] -> [0, 4, 9] -> [9, 0, 4]
        """
        chord[INDEX_KEYNOTE+2] += 2
        tmp_note = chord[INDEX_KEYNOTE+2]
        del chord[INDEX_KEYNOTE+2]
        chord.insert(INDEX_KEYNOTE, tmp_note)
        __reset_chord_value(chord)

        return True

    elif chord_type == IS_MINOR:
        """
            으뜸음을 2반음 내린 다음 으뜸음을 5음 위치로 이동시켜서 3음을 으뜸으로 설정
            [0, 3, 7] -> [10, 3, 7] -> [3, 7, 10]
        """
        chord[INDEX_KEYNOTE] -= 2
        tmp_note = chord[INDEX_KEYNOTE]
        del chord[INDEX_KEYNOTE]
        chord.append(tmp_note)
        __reset_chord_value(chord)

        return True
    else:
        return False

def leading_tone(chord):

    __change_to_real_value(chord)
    chord_type = __check_major_or_minor(chord)

    if chord_type == IS_MAJOR:
        """
            으뜸음을 1반음 내린 다음, 3음을 으뜸음으로 설정
            [0, 4, 7] -> [11, 4, 7] -> [4, 7, 11]
        """
        chord[INDEX_KEYNOTE] -= 1
        tmp_note = chord[INDEX_KEYNOTE]
        del chord[INDEX_KEYNOTE]
        chord.append(tmp_note)
        __reset_chord_value(chord)

        return True
    
    elif chord_type == IS_MINOR:
        """
            5음을 1반음 올린 다음 5음을 으뜸음으로 설정
            [0, 3, 7] -> [0, 3, 8] -> [8, 0, 3]
        """
        chord[INDEX_KEYNOTE+2] += 1
        tmp_note = chord[INDEX_KEYNOTE+2]
        del chord[INDEX_KEYNOTE+2]
        chord.insert(INDEX_KEYNOTE, tmp_note)
        __reset_chord_value(chord)

        return True
    else:
        return False


""" MUSIC FUNCTION """

if __name__ == "__main__":

    # Parrel
    major_chord_list = [generate_chord("major", idx) for idx in range(0, 12)]
    minor_chord_list = [generate_chord("minor", idx) for idx in range(0, 12)]

    print("PARREL - MAJOR")
    print("================================")
    for chord in major_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        parrel(chord)
        print(f"{before} ==> {chord}")

    print("")
    print("PARREL - MINOR")
    print("================================")
    for chord in minor_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        parrel(chord)
        print(f"{before} ==> {chord}")



    # Relative    
    major_chord_list = [generate_chord("major", idx) for idx in range(0, 12)]
    minor_chord_list = [generate_chord("minor", idx) for idx in range(0, 12)]

    print("")
    print("RELATIVE - MAJOR")
    print("================================")
    for chord in major_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        relative(chord)
        print(f"{before} ==> {chord}")

        
    print("")
    print("RELATIVE - MINOR")
    print("================================")
    for chord in minor_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        relative(chord)
        print(f"{before} ==> {chord}")
        


    # Leading Tone
    major_chord_list = [generate_chord("major", idx) for idx in range(0, 12)]
    minor_chord_list = [generate_chord("minor", idx) for idx in range(0, 12)]

    print("")
    print("LEADING TONE - MAJOR")
    print("================================")
    for chord in major_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        leading_tone(chord)
        print(f"{before} ==> {chord}")
        
    print("")
    print("LEADING TONE - MINOR")
    print("================================")
    for chord in minor_chord_list:
        before = [chord[idx] for idx in range(0, len(chord))]
        leading_tone(chord)
        print(f"{before} ==> {chord}")
