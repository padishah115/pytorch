import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/Users/hayden/Documents/pytorch/GPU vs CPU Computation/Multiplication_to_400_dim.csv')

plt.plot(df['dimensions'], df['cpu times'], label='cpu', color='r')
plt.plot(df['dimensions'], df['gpu times'], label='gpu', color='g')
plt.ylabel('Time / s')
plt.xlabel('Square Matrix Dimension Number')
plt.title('Matrix Multiplication Computation Time\n As Function of Device')
plt.legend()
plt.show()
