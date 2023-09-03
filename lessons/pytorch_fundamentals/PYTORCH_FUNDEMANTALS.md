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
MATRIX = torch.tensor([7,8],[9,10])
print(MATRIX) # tensor([[7,8],[9,10]])
print(MATRIX) # 2
print(MATRIX[0]) # tensor([7,8])
print(MATRIX[1]) # tensor([9,10])
print(MATRIX.shape) # torch.Size([2,2])

# Tensor
TENSOR = torch.tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(TENSOR) # tensor([[[1,2,3],[3,6,9],[2,4,5]]])
print(TENSOR.ndim) # 3
print(TENSOR.shape) # torch.Size([1,3,3])
print(TENSOR[0]) # tensor([[1,2,3],[3,6,9],[2,4,5]])

```

#### Random Tensors
Random tensors are important because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those random numbers 
to better represent the data.<br>
Start with random numbers -> look at data -> update random numbers -> look at data -> update random numbers<br>
Torch random tensors - [https://pytorch.org/docs/stable/generated/torch.rand.html](https://pytorch.org/docs/stable/generated/torch.rand.html)
```python
import torch

# Create a random tensor of size (3,4)
random_tensor = torch.rand(3,4)
print(random_tensor)

# Create a random tensor with similar shape to an image tensor
random_image_size_tensor = torch.rand(size=(224, 224, 3)) # height, width, colour channels (R, G, B)
print(random_image_size_tensor.shape)
print(random_image_size_tensor.ndim)

# Create a tensor of all zeros
zeros = torch.zeros(size=(3,4))
print(zeros)

# Create a tensor of all ones
ones = torch.ones(size=(3,4))
print(ones)

```