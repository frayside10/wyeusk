def gc():
    current, nxt = 0, 1

    while True:
        yield current
        current, nxt = nxt, current + nxt


for v in gc():
    print(v)
    if v > 100:
        break
