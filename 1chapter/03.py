mo = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

PI = []
count = 0

for i in mo:
    if i == " " or i == "," or i == ".":
        if count == 0:
            continue
        PI.append(count)
        count = 0
    else:
        count += 1

print(PI)