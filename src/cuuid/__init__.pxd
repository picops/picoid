# Cython-only: for other .pyx/.pxd to cimport cuuid
from .cuuid cimport UUID, randstr_16, uuid4
