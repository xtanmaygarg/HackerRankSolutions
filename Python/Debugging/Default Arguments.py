# Debug Code Only Available.
# Replace It With Code in Your Window

def print_from_stream(n, stream=EvenStream()):
    if not stream.current & 1:
        stream.current = 0
    for _ in range(n):
        print(stream.get_next())

