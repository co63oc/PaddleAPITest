export CUDA_VISIBLE_DEVICES=0
export FLAGS_use_system_allocator=1
for i in {1..10000}; do python engine.py --api_config_file=tester/api_config/api_config_merged_1.txt --accuracy=True >> test_pipline/cpu_accuracy/cpu_accuracy_1.log 2>&1; done