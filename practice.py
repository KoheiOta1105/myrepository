import numpy as np
import torch


ndarray = np.array([[1,2,3],
                    [4,5,6]])
print('\n', ndarray)
print('\n', type(ndarray))

tensor = torch.from_numpy(ndarray)  # np.ndarray -> torch.tensor
print('\n\n', tensor)
print('\n', type(tensor))

ndarray = tensor.detach().clone().numpy()  # torch.tensor -> np.ndarray
print('\n\n', ndarray)
print('\n', type(ndarray))
