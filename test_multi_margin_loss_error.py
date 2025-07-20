import paddle

# paddle.nn.functional.multi_margin_loss(Tensor([5, 0],"float64"), Tensor([5],"int64"), p=1, margin=1.0, weight=None, reduction="mean", name=None, )

input = paddle.zeros([5, 0], dtype='float64')
label = paddle.ones([5], dtype="int64")
result = paddle.nn.functional.multi_margin_loss(input, label, p=1, margin=1.0, weight=None, reduction="mean")
print(result)
