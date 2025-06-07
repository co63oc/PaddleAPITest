rm -vf ./tester/api_config/test_log/checkpoint.txt

echo $1
echo "accuracy"
python engine.py --accuracy=True --api_config_file=tester/api_config/big_and_0size/api_config_0sizetensor_accuracy.txt --filter "$1"
echo "paddleonly"
# python engine.py --accuracy=True --api_config_file=tester/api_config/big_and_0size/api_config_0sizetensor_paddleonly.txt --filter "$1"
python engine.py --paddle_only=True --api_config_file=tester/api_config/big_and_0size/api_config_0sizetensor_paddleonly.txt --filter "$1"

# python engine.py --paddle_only=True --api_config_file=report/0size_tensor_gpu/20250319/accuracy/coredump_error/error_config.txt --filter "$1"