import torch
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd

smoothing = 10 #Number of trials for each matrix dimension

def compare_computation(max_dimension, smoothing):
    dimensions = np.arange(1, max_dimension+1, 1)
    cpu_times = []
    gpu_times = []

    for dim in dimensions:
        cpu_t = torch.ones(dim, dim, device='cpu')
        gpu_t = torch.ones(dim, dim, device='mps')
        cpu_for_this_dim = []
        gpu_for_this_dim = []

        for _ in range (smoothing):
            ti = time.time()
            cpu_t*cpu_t
            tf = time.time()
            cpu_for_this_dim.append(tf-ti)

            torch.mps.synchronize()
            ti = time.time()
            gpu_t*gpu_t
            torch.mps.synchronize()
            tf = time.time()
            gpu_for_this_dim.append(tf-ti)

        cpu_times.append(np.mean(cpu_for_this_dim))
        gpu_times.append(np.mean(gpu_for_this_dim))

    data = {'dimensions': dimensions, 'cpu times': cpu_times, 'gpu times': gpu_times}
    df = pd.DataFrame(data)
    df.to_csv(f'GPU vs CPU Computation/Multiplication_to_{max_dimension}_dim.csv', index=False)
    
compare_computation(10000, smoothing)


