# rm -vf ./tester/api_config/test_log/checkpoint.txt

echo $1
# echo "accuracy"
# python engine.py --accuracy=True --api_config_file=tester/api_config/big_and_0size/api_config_0sizetensor_accuracy.txt --filter "$1"
# echo "paddleonly"
# python engine.py --paddle_only=True --api_config_file=tester/api_config/big_and_0size/api_config_0sizetensor_paddleonly.txt --filter "$1"

echo "accuracy"
python engine.py --accuracy=True --api_config_file=report/0size_tensor_gpu/error_config.txt --filter "masked_select("
python engine.py --accuracy=True --api_config_file=report/0size_tensor_gpu/error_config_paddleonly.txt --filter "paddle.polar("

# config_file=tester/api_config/7_0_size/0_size_tensor_1_8_1.txt
# echo "accuracy"
# python engine.py --accuracy=True --api_config_file=$config_file --filter "$1"
# echo "paddleonly"
# python engine.py --paddle_only=True --api_config_file=$config_file --filter "$1"
