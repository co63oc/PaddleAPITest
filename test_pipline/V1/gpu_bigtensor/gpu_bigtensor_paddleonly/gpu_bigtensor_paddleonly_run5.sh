export CUDA_VISIBLE_DEVICES=4
export FLAGS_use_system_allocator=1
export PYTHONPATH=/host_home/wanghuan29/Paddle/build/python
# sleep 3h
for i in {1..10000}; do python engine.py --api_config_file=test_pipline/gpu_bigtensor/gpu_bigtensor_paddleonly/gpu_bigtensor_paddleonly_errorconfig_5.txt --paddle_only=True >> test_pipline/gpu_bigtensor/gpu_bigtensor_paddleonly/gpu_bigtensor_paddleonly_errorconfig_5.log 2>&1; done
