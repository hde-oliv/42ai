from datetime import date, datetime
from sys import stdout
from time import sleep


def ft_progress(a_range: range):
    total = len(a_range)
    step = total / 20
    start_time = datetime.now()
    second_delta = datetime.now() - start_time
    
    for i in a_range:
        delta = datetime.now() - start_time
        bar = "".join(["#"] * (int(i / step) % 20))

        stdout.write("\r")
        stdout.write("ETA: {0:.1f} secs ".format(second_delta.seconds * (total - i) / 10**7))
        stdout.write("[{0:>3.0f}%]".format(i * 100 / total))
        stdout.write("[{0:<19}] ".format(bar))
        stdout.write(f"{i + 1}/{total} | elapsed time {delta.seconds} secs")
        yield i
        second_delta = second_delta - delta
    

def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

if __name__ == '__main__':
    main()
