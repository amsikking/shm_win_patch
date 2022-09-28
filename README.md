# shm_win_patch
Fix a memory leak in SharedMemory on **Windows**, i.e. the main Class from Pythons 'multiprocessing.shared_memory' module:
- https://docs.python.org/3/library/multiprocessing.shared_memory.html

## Bug details and status:
- https://stackoverflow.com/questions/65968882/unlink-does-not-work-in-pythons-shared-memory-on-windows
- https://github.com/python/cpython/pull/20684
- https://bugs.python.org/issue40882
- https://github.com/python/cpython/issues/85059

## Test:
- Download and run 'shared_memory_test.py'.
- If the test is failed then uncomment 'import shm_win-patch' on line 1 and re-run.
- This should fix the memory leak.

## Note:
This is a potentially fragile solution and we may need to update 'shm_win_patch.py' peroidically to keep up with the 'shared_memory.py' repository:
- https://github.com/python/cpython/blob/main/Lib/multiprocessing/shared_memory.py

At some point the real fix should be updated in 'shared_memory.py' at which point this patch will no longer be needed...

## Acknowledgments:
Thanks to https://github.com/nhthayer for throwing this together
