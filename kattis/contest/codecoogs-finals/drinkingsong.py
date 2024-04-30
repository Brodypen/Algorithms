def singSong(times, drink):
    if times == 2:
        st = str(times) + " bottles of " + drink + " on the wall, " + str(times) + " bottles of " + drink + ".\nTake one down, pass it around, " + str(times-1) + " bottle of " + drink + " on the wall."
        st += "\n\n"
        return st + singSong(times-1, drink)
    if times == 1:
        st = "1 bottle of " + drink + " on the wall, 1 bottle of " + drink + ".\nTake it down, pass it around, no more bottles of " + drink + "."
        return st
    st = ""
    # st = "1bottles" + times +  " bottle of " + drink + " on the wall, 1 bottle of " + drink + ".\nTake one down, pass it around," + (times-1) + " bottles of " + drink + " on the wall."
    # st += times + "bottles of" + drink + "on the wall," + times + "bottles of" + drink + ".Take one down, pass it around," + times-1 + "bottles of" + drink + "on the wall."
    st = str(times) + " bottles of " + drink + " on the wall, " + str(times) + " bottles of " + drink + ".\nTake one down, pass it around, " + str(times-1) + " bottles of " + drink + " on the wall."
    st += "\n\n"
    return st + singSong(times-1, drink)


t = int(input())
d = input()
print(singSong(t,d))
