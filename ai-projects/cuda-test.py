import torch

# Create a tensor on GPU
x = torch.tensor([1.0, 2.0, 3.0]).cuda()
print(x)
print(x.device)