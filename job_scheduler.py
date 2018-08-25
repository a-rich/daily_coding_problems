from __future__ import print_function
import time

def schedule(f_map, n):
    time.sleep(n/1000.)
    return f_map['function'](*f_map['args'])

if __name__ == '__main__':
    n = 2000
    f_map = {
            'function': lambda x,y: x + y,
            'args': [7,3]
            }

    start = time.time()
    result = schedule(f_map, n)
    print('Computed {} after approximately {} milliseconds.'.format(result,
        (time.time() - start) * 1000))
