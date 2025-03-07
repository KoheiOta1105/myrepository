import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.makedirs('output', exist_ok=True)

timestep = 100
theta = np.linspace(-10, 10, timestep)  # -10から10の間のデータをtimestep分作成

x = np.cos(theta)
y = np.sin(theta*2)

data = np.stack([x, y], axis=1)

plt.plot(data[:, 0], data[:, 1])

plt.savefig('./output/eight.png')