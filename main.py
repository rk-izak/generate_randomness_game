import random

data = []
binary = ('000', '001', '010', '011', '100', '101', '110', '111')
money = 1000
bet = 1


def analyse(sth):
    j = 0
    results = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    triads = ('000', '001', '010', '011', '100', '101', '110', '111')
    for value in triads:
        value_1 = value + '0'
        value_2 = value + '1'
        for i in range(0, len(sth) - 2):
            if "".join(sth[i: i + 4]) == value_1:
                results[j][0] += 1
            elif "".join(sth[i: i + 4]) == value_2:
                results[j][1] += 1
        j += 1
    return results


def predict(test, start, analysis):
    # test as a list of the form ['X', 'Y', 'Z', ...]
    # analysis is a list of the form [[a, b], [c, d], ...] where a/b/c/d are int
    # triads = ('000', '001', '010', '011', '100', '101', '110', '111')
    prediction = []
    prediction[0:3] = start
    for i in range(0, len(test) - 3):
        a = ''
        b = "".join(test[i: i + 3])
        if b == '000':
            if analysis[0][0] > analysis[0][1]:
                a = '0'
            elif analysis[0][0] < analysis[0][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])
        elif b == '001':
            if analysis[1][0] > analysis[1][1]:
                a = '0'
            elif analysis[1][0] < analysis[1][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])

        elif b == '010':
            if analysis[2][0] > analysis[2][1]:
                a = '0'
            elif analysis[2][0] < analysis[2][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])

        elif b == '011':
            if analysis[3][0] > analysis[3][1]:
                a = '0'
            elif analysis[3][0] < analysis[3][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])

        elif b == '100':
            if analysis[4][0] > analysis[4][1]:
                a = '0'
            elif analysis[4][0] < analysis[4][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])
        elif b == '101':
            if analysis[5][0] > analysis[5][1]:
                a = '0'
            elif analysis[5][0] < analysis[5][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])

        elif b == '110':
            if analysis[6][0] > analysis[6][1]:
                a = '0'
            elif analysis[6][0] < analysis[6][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])
        elif b == '111':
            if analysis[7][0] > analysis[7][1]:
                a = '0'
            elif analysis[7][0] < analysis[7][1]:
                a = '1'
            else:
                a = random.choice(['1', '0'])

        prediction.extend(a)

    counter = 0
    for j in range(3, len(test)):
        if test[j] == prediction[j]:
            counter += 1

    return prediction, counter


def find_first(initial):
    intensity = [0] * 8
    for i in range(0, len(initial)):
        b = "".join(initial[i: i + 3])
        if b == '000':
            intensity[0] += 1
        elif b == '001':
            intensity[1] += 1
        elif b == '010':
            intensity[2] += 1
        elif b == '011':
            intensity[3] += 1
        elif b == '100':
            intensity[4] += 1
        elif b == '101':
            intensity[5] += 1
        elif b == '110':
            intensity[6] += 1
        elif b == '111':
            intensity[7] += 1
    return intensity


print('Please give AI some data to learn...')
while True:
    print("The current data length is {}, {} symbols left".format(len(data), 100 - len(data)))
    print("Print a random string containing 0 or 1:\n")
    user = input()
    for char in list(user):
        if str(char) == '1' or str(char) == '0':
            data += str(char)
        else:
            break
    if len(data) >= 100:
        break

print('\nFinal data string:')
print("".join(data) + '\n')
initial_analyse = analyse(data)
print("""You have ${}. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn ${}. Print "enough" to leave the game. Let's go!""".format(money, bet))

triads_dict = {binary[j]: analyse(data)[j][0:2] for j in range(0, len(binary))}

first_three = find_first(data)
first_three = first_three.index(max(first_three))
first_three = list(binary[first_three])  # in the form of str ['X', 'Y', 'Z']

# first_three = list(random.choice(binary))
#  for j in range(0, len(binary)):
#  print('{}: {},{}'.format(binary[j], triads_dict[binary[j]][0], triads_dict[binary[j]][1]))

while True:
    print("\nPrint a random string containing 0 or 1:")
    user = input()
    if user == 'enough':
        break
    elif set(user) == {'1', '0'} or set(user) == {'1'} or set(user) == {'0'}:
        new_data = []

        for char in list(user):
            if str(char) == '1' or str(char) == '0':
                new_data += str(char)
            else:
                break
        guess, pred = predict(new_data, first_three, initial_analyse)
        money -= bet * pred
        money += bet * ((len(new_data) - 3) - pred)
        print("prediction:")
        print("".join(guess))
        print('\nComputer guessed right {} out of {} symbols ({} %)'
              .format(pred, len(new_data) - 3, round(pred * 100 / (len(new_data) - 3), 2)))
        print("Your balance is now ${}".format(money))
        new_analyse = analyse(new_data)

        for v in range(len(initial_analyse)):
            # iterate through columns
            for k in range(len(initial_analyse[0])):
                initial_analyse[v][k] += + new_analyse[v][k]
    else:
        pass

print("Game over!")
print(analyse(data))
