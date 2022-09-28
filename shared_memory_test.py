##import shm_win_patch
from multiprocessing import shared_memory as sm

def get_shared_memory(i, size_bytes):
    print('getting shared memory: size=%0.2fGB, iteration=%03d'%(
        1e-9 * size_bytes, i))
    shm1 = sm.SharedMemory(create=True,  size=size_bytes) # get some
    shm2 = sm.SharedMemory(create=False, name=shm1.name)  # take a look
    shm1.unlink()
    shm1.close()
    shm2.unlink()
    shm2.close()
    return None

# TEST:
# -> increase iterations for more RAM (~60 for 16GB RAM, ~600 for 384GB RAM)
# -> normally the loop slows down as memory runs out...

for i in range(100):
    get_shared_memory(i, int(1e9)) # 1GB chunks

# ERROR:

##Traceback (most recent call last):
##  File "C:\Users\AMS\My Drive\AMS_temp\shared_memory_bug\shared_memory_test.py", line 25, in <module>
##    get_shared_memory(int(1e9))
##  File "C:\Users\AMS\My Drive\AMS_temp\shared_memory_bug\shared_memory_test.py", line 8, in get_shared_memory
##    shm1 = shared_memory.SharedMemory(create=True, size=size_bytes)
##  File "C:\Users\AMS\Python39\lib\multiprocessing\shared_memory.py", line 151, in __init__
##    self._mmap = mmap.mmap(-1, size, tagname=temp_name)
##OSError: [WinError 1455] The paging file is too small for this operation to complete

# SOLUTION:
# -> uncomment line 1 'import shm_win_patch' should fix the memory leak
