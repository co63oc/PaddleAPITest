# rm -vf ./tester/api_config/test_log/checkpoint.txt
set -x
echo $1

mkdir -p tmp/config

name=`basename $0`
op_name=`echo $1 | tr -d "("`
config_file=`pwd`/tmp/config/${name}_${op_name}.txt
. ./2_config.sh
cat $config_file1 $config_file2 | grep "$1" | sort | uniq | grep -v "\"float16\"" > $config_file

# python engineV2.py --accuracy=True --num_gpus=1 --num_workers_per_gpu=1 --required_memory=1 --api_config_file=$config_file --filter "$1"
python engine.py --accuracy=True --test_cpu=True --api_config_file=$config_file --filter "$1"
