import paddle
import numpy as np
paddle.device.set_device('cpu')
x = paddle.to_tensor([1,2], dtype='float32')
x.stop_gradient = False
y = paddle.to_tensor([False,False], dtype='bool')
z = x.masked_select(y)
print(z) #shape=[0]
z.sum().backward()
print(x.grad)

import torch
import numpy as np
# paddle.device.set_device('cpu')
x = torch.tensor([1,2], dtype=torch.float32)
x.requires_grad = True
y = torch.tensor([False,False], dtype=torch.bool)
z = x.masked_select(y)
print(z) #shape=[0]
z.sum().backward()
print(x.grad)
