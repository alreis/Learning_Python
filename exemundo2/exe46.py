import emoji
import time

for c in range(10, 0, -1):
    print('\r{}'.format(c))
    time.sleep(1)

print(emoji.emojize(':fireworks:'*20))

import time, sys, emoji

for i in range(10, 0, -1):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print(emoji.emojize('\r:fireworks:'*20))