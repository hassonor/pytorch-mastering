### Introduction To Tensors
____
#### Creating tensors
See the Link: [https://pytorch.org/docs/stable/tensors.html](https://pytorch.org/docs/stable/tensors.html) <br>
```python
import torch

# Scalar
scalar = torch.tensor(7)
print(scalar) # tensor(7)
print(scalar.ndim) #  0

# Get tensor back as Python int
scalar.item() #  7

# Vector
vector = torch.tensor([7,7])
print(vector) #  tensor([7,7])
print(vector.ndim) #  1
print(vector.shape) # torch.Size([2]) 

# Matrix
matrix = torch.tensor([7,8],[9,10])
print(matrix) # tensor([[7,8],[9,10]])
print(matrix) # 2
print(matrix[0]) # tensor([7,8])
print(matrix[1]) # tensor([9,10])
print(matrix.shape) # torch.Size([2,2])

# Tensor
tensor = torch.tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(tensor) # tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(tensor.ndim) # 3
print(tensor.shape) # torch.Size([1,3,3])
print(tensor[0]) # tensor([[1,2,3],[3,6,9],[2,4,5]])
```
