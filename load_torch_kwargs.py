
import pickle
import numpy as np

def open_f(f):
    a = pickle.load(open(f, 'rb'))
    return a

import os
current_file = os.path.basename(__file__)
name_without_extension = current_file[:-3]
parts = name_without_extension.split("_")
framework = parts[-1]
api_name = "_".join(parts[:-1])

# api_name = "conv2d"
# framework = "paddle"

if framework == "paddle":
    import paddle
if framework == "torch":
    import torch
ret = open_f(f"tmp/data/{api_name}_{framework}_kwargs.pkl")

if isinstance(ret, dict):
    for k, v in ret.items():
        if isinstance(v, np.ndarray):
            if framework == "paddle":
                v = paddle.to_tensor(v)
            if framework == "torch":
                v = torch.from_numpy(v)
        ret[k] = v
    kwargs = ret

ret = open_f(f"tmp/data/{api_name}_{framework}_args.pkl")
if isinstance(ret, list):
    for i, v in enumerate(ret):
        if isinstance(v, np.ndarray):
            if framework == "paddle":
                v = paddle.to_tensor(v)
            if framework == "torch":
                v = torch.from_numpy(v)
            ret[i] = v
    args = ret


