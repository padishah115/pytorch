import matplotlib.pyplot as plt
import torch
import numpy as np

torch.manual_seed(123)

T = np.arange(1, 5, 1)

a = torch.rand(5)

for t in T:
    prob= torch.exp(a/t) / torch.exp(a/t).sum()
    plt.scatter(a, prob.numpy(), label = f'T={t:.2f}')

plt.title('Effect of Temperature, T, on Softmax distribution')
plt.ylabel('Probability P(x)')
plt.xlabel('x')
plt.legend()
plt.show()