import paddle
a = paddle.full([0, 2], 2)
a.stop_gradient = False
b = paddle.ones([1, 2])
b.stop_gradient = False
z = a+b
paddle.autograd.backward([z])
print(a.grad)
