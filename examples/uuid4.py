from cuuid import UUID, randstr_16, uuid4

if __name__ == "__main__":
    # Example 1: Create a UUID from a string
    uuid_str = "12345678-1234-5678-1234-567812345678"
    u1 = UUID(uuid_str)
    print("UUID from string:", u1)
    print("  hex:", u1.hex)
    print("  int:", u1.int)
    print("  bytes:", u1.bytes)

    # Example 2: Generate a random UUID (version 4)
    u2 = uuid4()
    print("\nRandom UUID4:", u2)
    print("  version:", u2.version)
    print("  hex:", u2.hex)
    print("  bytes:", u2.bytes)

    # Example 3: Generate 16 random bytes (can be used as a UUID)
    random_bytes = randstr_16()
    print("\nRandom 16 bytes:", random_bytes)
    u3 = UUID(random_bytes)
    print("UUID from random bytes:", u3)
