#pragma once

#include <stdint.h>

#define UUID_SIZE 16

// Function to generate a random UUID (version 4)
void c_uuid4(uint8_t uuid[UUID_SIZE]);
