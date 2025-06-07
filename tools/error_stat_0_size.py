# test_log 一键整理小工具（engineV2有序版）：log_digester_lite + get_api_set + get_api_config_set
# @author: cangtianhuang
# 整理效果：pass + error + invalid

from pathlib import Path
import re

TEST_LOG_PATH = Path("tester/api_config/est_log_0_size")
OUTPUT_PATH = TEST_LOG_PATH
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# get all test blocks
logs = []
in_test_block = False
current_content = []

LOG_PATH = TEST_LOG_PATH / "log_inorder.log"
try:
    with LOG_PATH.open("r") as f:
        input_text = f.read()
except Exception as err:
    print(f"Error reading {LOG_PATH}: {err}", flush=True)
    exit(1)

for line in input_text.split("\n"):
    if "gpu_resources.cc" in line or "Waiting for available memory" in line:
        continue

    if "test begin" in line:
        if in_test_block and current_content:
            logs.append("\n".join(current_content))
        in_test_block = True
        current_content = [line]
        continue

    if "Worker PID" in line:
        if in_test_block and current_content:
            logs.append("\n".join(current_content))
        in_test_block = False
        current_content = []
        continue

    if in_test_block:
        current_content.append(line)

if current_content:
    logs.append("\n".join(current_content))


def get_sort_key(content):
    lines = content.split("\n")
    match = re.search(r"test begin: (.*)$", lines[0])
    if match:
        return match.group(1).strip()
    return ""


# get all pass api and config
pass_file = TEST_LOG_PATH / "api_config_pass.txt"
pass_names = set()
pass_configs = set()
if pass_file.exists():
    try:
        with open(pass_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    pass_name = line.split("(", 1)[0]
                    pass_names.add(pass_name)
                    pass_configs.add(line)
    except Exception as err:
        print(f"Error reading {pass_file}: {err}", flush=True)
        exit(0)
print(f"Read {len(pass_names)} pass api(s)", flush=True)
print(f"Read {len(pass_configs)} pass api config(s)", flush=True)

# classify logs
invalid_logs = {}
pass_logs = {}
error_logs = {}
torch_error_logs = {}
for content in logs:
    key = get_sort_key(content)
    if not key:
        continue
    if (
        "CUDA out of memory" in content
        or "Out of memory error" in content
        or "[torch error]" in content
        or "(NotFound)" in content
    ):
        invalid_logs[key] = content
    elif key in pass_configs:
        pass_logs[key] = content
    else:
        error_logs[key] = content

# write pass_log.log
pass_log = OUTPUT_PATH / "pass_log.log"
try:
    with open(pass_log, "w") as f:
        for key in sorted(pass_logs.keys()):
            content = pass_logs[key]
            f.write(content + "\n\n")
except Exception as err:
    print(f"Error writing {pass_log}: {err}", flush=True)
    exit(0)
print(f"Read and write {len(pass_logs)} pass log(s)", flush=True)

# write pass_api.txt
API_OUTPUT_PATH = OUTPUT_PATH / "pass_api.txt"
try:
    with open(API_OUTPUT_PATH, "w") as f:
        f.writelines(f"{line}\n" for line in sorted(pass_names))
except Exception as err:
    print(f"Error writing {API_OUTPUT_PATH}: {err}", flush=True)
    exit(0)
print(f"Write {len(pass_names)} pass api(s)", flush=True)

# write pass_config.txt
CONFIG_OUTPUT_PATH = OUTPUT_PATH / "pass_config.txt"
try:
    with open(CONFIG_OUTPUT_PATH, "w") as f:
        f.writelines(f"{line}\n" for line in sorted(pass_configs))
except Exception as err:
    print(f"Error writing {CONFIG_OUTPUT_PATH}: {err}", flush=True)
    exit(0)
print(f"Write {len(pass_configs)} pass api config(s)", flush=True)

# error logs
ERROR_FILES = [
    "api_config_accuracy_error.txt",
    "api_config_crash.txt",
    "api_config_paddle_error.txt",
    "api_config_torch_error.txt",
    "api_config_paddle_to_torch_failed.txt",
    "api_config_timeout.txt",
    "api_config_skip.txt",
]

# get all error api and config
error_names = set()
error_configs = set()
for file_name in ERROR_FILES:
    FILE_PATH = TEST_LOG_PATH / file_name
    if not FILE_PATH.exists():
        continue
    try:
        with open(FILE_PATH, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    if line not in error_logs:
                        if line not in invalid_logs:
                            invalid_logs[line] = ""
                        continue
                    error_name = line.split("(", 1)[0]
                    error_names.add(error_name)
                    error_configs.add(line)
    except Exception as err:
        print(f"Error reading {file_name}: {err}", flush=True)
        exit(0)
print(f"Read {len(error_names)} error api(s)", flush=True)
print(f"Read {len(error_configs)} error api config(s)", flush=True)

# write error_api.txt
API_OUTPUT_PATH = OUTPUT_PATH / "error_api.txt"
try:
    with open(API_OUTPUT_PATH, "w") as f:
        f.writelines(f"{line}\n" for line in sorted(error_names))
except Exception as err:
    print(f"Error writing {API_OUTPUT_PATH}: {err}", flush=True)
    exit(0)
print(f"Write {len(error_names)} error api(s)", flush=True)

# write error_config.txt
CONFIG_OUTPUT_PATH = OUTPUT_PATH / "error_config.txt"
try:
    with open(CONFIG_OUTPUT_PATH, "w") as f:
        f.writelines(f"{line}\n" for line in sorted(error_configs))
except Exception as err:
    print(f"Error writing {CONFIG_OUTPUT_PATH}: {err}", flush=True)
    exit(0)
print(f"Write {len(error_configs)} error api config(s)", flush=True)

# write error_log.log
error_log = OUTPUT_PATH / "error_log.log"
count = 0
try:
    with open(error_log, "w") as f:
        for key in sorted(error_logs.keys()):
            if key not in error_configs:
                continue
            content = error_logs[key]
            f.write(content + "\n\n")
            count += 1
except Exception as err:
    print(f"Error writing {error_log}: {err}", flush=True)
    exit(0)
print(f"Read and write {count} error log(s)", flush=True)

# write invalid_config.txt
CONFIG_OUTPUT_PATH = OUTPUT_PATH / "invalid_config.txt"
try:
    with open(CONFIG_OUTPUT_PATH, "w") as f:
        f.writelines(f"{line}\n" for line in sorted(invalid_logs.keys()))
except Exception as err:
    print(f"Error writing {CONFIG_OUTPUT_PATH}: {err}", flush=True)
    exit(0)
print(f"Write {len(invalid_logs)} invalid api config(s)", flush=True)
