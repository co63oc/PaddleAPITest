export CUDA_VISIBLE_DEVICES=3
export FLAGS_use_system_allocator=1
export PYTHONPATH=/host_home/wanghuan29/Paddle/build/python
# sleep 3h
for i in {1..10000}; do python engine.py --api_config_file=test_pipline/gpu_bigtensor/gpu_bigtensor_accuracy/gpu_bigtensor_accuracy_errorconfig_4.txt --accuracy=True >> test_pipline/gpu_bigtensor/gpu_bigtensor_accuracy/gpu_bigtensor_accuracy_errorconfig_4.log 2>&1; done
