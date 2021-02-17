import matplotlib.pyplot as plt

circle2 = plt.Circle((0, 0), 10, color='blue')

fig, ax = plt.subplots()
ax.autoscale(enable=True)

ax.add_patch(circle2)

plt.show()