def get_calibration_value(word):
    for sign in word:
        if sign.isdigit():
            begin_digit = sign

    for sign in reversed(word):
        if sign.isdigit():
            end_digit = sign
    begin = int(begin_digit)
    end = int(end_digit)
    return end * 10 + begin


with open('input', 'r') as plik:
    wyrazy = plik.read().splitlines()

wyniki = [get_calibration_value(x) for x in wyrazy]

print(sum(wyniki))
