import threading
import time
from concurrent.futures import ThreadPoolExecutor


class resource_A:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self, name):
        print("The Resource - A is being aquired by {}".format(name))
        self.acquire()
        print("The Resource - A is aquired by {}".format(name))

    def release(self, name):
        print("The Resource - A is being releaseed by {}".format(name))
        self.lock.release()
        print("The Resource - A has been releaseed by {}".format(name))


class resource_B:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self, name):
        print("The Resource - B is being acquired by {}".format(name))
        self.acquire()
        print("The Resource - B is acquired by {}".format(name))

    def release(self, name):
        print("The Resource - B is being released by {}".format(name))
        self.release()
        print("The Resource - B has been released by {}".format(name))


def generic_task(name, resource_A, resource_B):

    resource_A.acquire(name)
    time.sleep(2)
    resource_B.acquire(name)
    time.sleep(2)

    print("Completed Using the Resources")
    resource_A.release(name)
    resource_B.release(name)


# Instantiating resources
if __name__ == "__main__":
    res_A = resource_A()
    res_B = resource_B()

    transactions = [["tasker-1", "tasker-2"], [res_A, res_B], [res_B, res_A]]

    with ThreadPoolExecutor(max_workers=2) as executer:
        executer.map(generic_task, *transactions)
