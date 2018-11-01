import re
mo = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

PI = []

mo2 = re.split('[,. ]', mo)

for i in mo2:
    if len(i) == 0:
        continue
    PI.append(len(i))

print(PI)