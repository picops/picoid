cdef extern from "uuid.h":
    cdef void c_uuid4(unsigned char* uuid)

################################################################################
# Copyright (C) 2016-present the asyncpg authors and contributors
# <see AUTHORS file>
#
# This module is part of asyncpg and is released under
# the Apache 2.0 License: http://www.apache.org/licenses/LICENSE-2.0

cdef extern from "hex.h":
    cdef void uuid_to_str(const char *source, char *dest)
    cdef void uuid_to_hex(const char *source, char *dest)
    # cdef void uuid_to_int(const char *source, unsigned long long *dest)

################################################################################