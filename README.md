# shm_win_patch
Fix a memory leak in SharedMemory on Windows:
- https://stackoverflow.com/questions/65968882/unlink-does-not-work-in-pythons-shared-memory-on-windows
- https://github.com/python/cpython/pull/20684
- https://bugs.python.org/issue40882
- https://github.com/python/cpython/issues/85059

## Note:
May have to update 'shm_win_patch.py' peroidically to keep up with the 'shared_memory.py' repository:
- https://github.com/python/cpython/blob/main/Lib/multiprocessing/shared_memory.py

At some point the real fix should filter through and be updated to 'shared_memory.py' at which point this patch will no longer be needed...

## Acknowledgments:
Thanks to https://github.com/nhthayer for throwing this together
