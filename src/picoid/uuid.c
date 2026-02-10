#include <stdint.h>
#include <string.h>
#include <stdatomic.h>
#include <stdlib.h>

#ifdef _WIN32
    #include <windows.h>
    #include <wincrypt.h>
    static HCRYPTPROV hProvider = 0;
#else
    #include <fcntl.h>
    #include <unistd.h>
    #include <errno.h>
    static int urandom_fd = -1;
#endif

#define UUID_SIZE 16
#define BUFFER_SIZE 8192  // 8KB buffer (512 UUIDs)
static unsigned char random_buffer[BUFFER_SIZE];
static _Atomic size_t buffer_pos = BUFFER_SIZE;  // Start empty to force initial fill

static void fill_buffer(void) {
    #ifdef _WIN32
        CryptGenRandom(hProvider, BUFFER_SIZE, random_buffer);
    #else
        if (urandom_fd != -1) {
            ssize_t bytes_read = read(urandom_fd, random_buffer, BUFFER_SIZE);
            if (bytes_read != BUFFER_SIZE) {
                // Handle error - could not read enough random bytes
                exit(1);
            }
        }
    #endif
    buffer_pos = 0;
}

static void __attribute__((constructor)) init_rng(void) {
    #ifdef _WIN32
        CryptAcquireContext(&hProvider, NULL, NULL, PROV_RSA_FULL, CRYPT_VERIFYCONTEXT);
    #else
        urandom_fd = open("/dev/urandom", O_RDONLY);
    #endif
    fill_buffer();  // Initial fill
}

static void __attribute__((destructor)) cleanup_rng(void) {
    #ifdef _WIN32
        if (hProvider) CryptReleaseContext(hProvider, 0);
    #else
        if (urandom_fd != -1) close(urandom_fd);
    #endif
}

void c_uuid4(uint8_t uuid[UUID_SIZE]) {
    size_t current_pos = atomic_fetch_add(&buffer_pos, UUID_SIZE);
    
    // Check if we need to refill
    if (current_pos + UUID_SIZE > BUFFER_SIZE) {
        fill_buffer();
        current_pos = atomic_fetch_add(&buffer_pos, UUID_SIZE);
    }
    
    // Copy bytes from buffer
    memcpy(uuid, random_buffer + current_pos, UUID_SIZE);

    // Set version and variant
    uuid[6] = (uuid[6] & 0x0F) | 0x40;
    uuid[8] = (uuid[8] & 0x3F) | 0x80;
}
