import torch
import pandas as pd
import numpy as np

################################################################
# Simple attempt to use autograd to produce linear fit between #
# data in an unknown unit system and data in celsius           #
################################################################

#Load data from CSV
df = pd.read_csv('autograd/temp_data.csv')
t_c = torch.tensor(df['Celsius Temp'])
t_u = torch.tensor(df['Unknown Temp'])

def model(x:torch.tensor, w:torch.tensor, b:torch.tensor):
    """Model for linear fit."""
    return x*w + b

def loss(t_p, t_c):
    """Calculates squared loss function"""
    sqr_diff = (t_p - t_c) ** 2
    return sqr_diff.mean()


w = torch.ones(()) #Weight
b = torch.ones(()) #Bias

t_p = model(t_u, w, b) #Model predicton
L = loss(t_p, t_c) #Loss function
print(t_p, L)

# grad = np.sqrt(L) * 
# alpha =
