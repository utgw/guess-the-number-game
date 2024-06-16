import sys
import random

sys.stdout.buffer.write(b'Please enter the minimum value\n')
sys.stdout.flush()
min_value = int(sys.stdin.buffer.readline().strip())

sys.stdout.buffer.write(b'Please enter the maximum value\n')
sys.stdout.flush()
max_value = int(sys.stdin.buffer.readline().strip())

while min_value >= max_value:
    sys.stdout.buffer.write(b'Please ensure the minimum value is less than the maximum value\n')
    sys.stdout.flush()
    
    sys.stdout.buffer.write(b'Please enter the minimum value\n')
    sys.stdout.flush()
    min_value = int(sys.stdin.buffer.readline().strip())

    sys.stdout.buffer.write(b'Please enter the maximum value\n')
    sys.stdout.flush()
    max_value = int(sys.stdin.buffer.readline().strip())

answer = random.randint(min_value, max_value)

while True:
    sys.stdout.buffer.write(b'Please enter the number you think is correct\n')
    sys.stdout.flush()
    user_input = int(sys.stdin.buffer.readline().strip())
    
    if user_input == answer:
        sys.stdout.buffer.write(b"That's correct!\n")
        sys.stdout.flush()
        break
    else:
        sys.stdout.buffer.write(b"That's incorrect, please try again\n")
        sys.stdout.flush()
