with open('input.txt') as rf:
    for line in rf:
        if '=' in line:
            break
        with open('output.txt', 'a') as af:
            af.write(line)
