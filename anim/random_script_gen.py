import random
d = {'box':5, 'sphere':3, 'torus':4, 'rotate': 'xyz', 'move': 2}
constants = ['shiny_purple', 'shiny_teal', 'dull_yellow']

f = raw_input("how many randoms: ")
times = int(f)
out = "constants shiny_purple 0.3 0.2 0.8 0.3 0 0 0.3 0.2 0.8\nconstants shiny_teal 0.3 0.0 0.0 0.3 0.2 0.8 0.3 0.2 0.8\nconstants dull_yellow 0.3 0.8 0.2 0.3 0.8 0.2 0 0 0\n"
keys = list(d.keys())
keys.append('sphere')
while times:
    r = random.choice(keys)
    out += r + " "
    if r in 'box sphere torus pyramid':
        out += random.choice(constants) + " "
    if d[r] == 'xyz':
        out += random.choice(["x","y","z"]) + " " + str(random.randrange(0, 360)) + "\n"
    else:
        v = d[r]
        ran = 500
        if d[r] == 'move':
            ran = 100
        while v:
            out += str(random.randrange(0, ran)) + " "
            v -= 1

        if d[r] != 'move':
            out += str(random.randrange(0, 100)) + "\n"


    times -= 1

out += "display\nsave randy.png"
f = open("script_rand.mdl", "w")
f.write(out)
f.close()
print("done")
