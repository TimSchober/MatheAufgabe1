# Time Taken: About 25 Minutes -> 10 Minutes for Beatification -> About 15 Minutes to get the Solution.


# a -> b
def if_then(a, b):
    if a == 1 and b == 0:
        return 0
    else:
        return 1

# a v b
def or_bin(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1

# a xor b
def xor_bin(a, b):
    if a == b:
        return 0
    else:
        return 1

# a <==> b
def equivalent(a, b):
    if a == b:
        return 1
    else:
        return 0

# c -> a and b
def if_then_and(a, b, c):
    if a == 1 and b == 1:
        return if_then(c, 1)
    else:
        return if_then(c, 0)

def execute():
    # enable showing of complete table
    show_all = False
    print('MRDupont', ' | ', 'MSDupont', ' | ', 'Emma', ' | ', 'Georg', ' | ', 'Ivana', ' ||| ',
          # If Mr. Dupont comes, then his wife will come, too.
          'MD -> MSD',
          ' | ',
          # At least one of the two children Ivana and Georg will come.
          'I v G',
          ' | ',
          # Either Mrs. Dupont or Emma will come.
          'MSD xor E',
          ' | ',
          # Either Emma and Georg come both, or they both don't come.
          'E <==> G',
          ' | ',
          # If Ivana comes, then also Georg and Mr. Dupont will come.
          'I -> G and MD')
    for i in range(32):
        binary = '{0:05b}'.format(i)
        MRDupont = int(binary[0])
        MSDupont = int(binary[1])
        Emma = int(binary[2])
        Georg = int(binary[3])
        Ivana = int(binary[4])

        # If Mr. Dupont comes, then his wife will come, too.
        ifThen = if_then(MRDupont, MSDupont)
        # At least one of the two children Ivana and Georg will come.
        orBin = or_bin(Ivana, Georg)
        # Either Mrs. Dupont or Emma will come.
        xorBin = xor_bin(MSDupont, Emma)
        # Either Emma and Georg come both, or they both don't come.
        aq = equivalent(Emma, Georg)
        # If Ivana comes, then also Georg and Mr. Dupont will come.
        ifThenAnd = if_then_and(Georg, MRDupont, Ivana)

        if show_all or (ifThen == 1 and orBin == 1 and xorBin == 1 and aq == 1 and ifThenAnd == 1):
            print(MRDupont, '        | ', MSDupont, '        | ', Emma, '    | ', Georg, '     | ', Ivana, '     ||| ',
                  ifThen, '         | ', orBin, '     | ', xorBin, '         | ', aq, '        | ', ifThenAnd)


if __name__ == '__main__':
    execute()

