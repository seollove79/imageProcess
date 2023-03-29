import tensorflow as tf
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
# 출력 화면에 GPU가 있다면 성공! CPU만 있으면 실패... :(
# memory_limit: GPU 메모리 사양