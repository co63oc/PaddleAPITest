set -x
echo $1

mkdir -p tmp/config

name=`basename $0`
op_name=`echo $1 | tr -d "("`
config_file=`pwd`/tmp/config/${name}_${op_name}.txt
. ./3_config.sh
cat $config_file1 $config_file2 | grep "$1" | sort | uniq > $config_file

python engine.py --accuracy=True --test_cpu=True --api_config_file=$config_file --filter "$1"
