export CUDA_VISIBLE_DEVICES=3
export FLAGS_use_system_allocator=1
for i in {1..10000}; do python engine.py --api_config_file=tester/api_config/api_config_merged_13.txt --paddle_only=True >> test_pipline/paddle_only/paddleonly_13.log 2>&1; done