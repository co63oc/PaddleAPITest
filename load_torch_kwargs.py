
import pickle
import numpy as np

def open_f(f):
    a = pickle.load(open(f, 'rb'))
    return a

api_name = "conv2d"
framework = "paddle"

if framework == "paddle":
    import paddle
if framework == "torch":
    import torch
ret = open_f(f"tmp/data/{api_name}_{framework}_kwargs.pkl")

if isinstance(ret, dict):
    for k, v in ret.items():
        if isinstance(v, np.ndarray):
            v = paddle.to_tensor(v)
        ret[k] = v
    kwargs = ret

ret = open_f(f"tmp/data/{api_name}_{framework}_args.pkl")
if isinstance(ret, list):
    for i, v in enumerate(ret):
        if isinstance(v, np.ndarray):
            v = paddle.to_tensor(v)
            ret[i] = v
    args = ret

# print(locals())
# ret = open_f("tmp/code/_paddle_args.pkl")
# print(paddle.to_tensor(ret[0]))
# ret = open_f("tmp/code/_paddle_kwargs.pkl")
