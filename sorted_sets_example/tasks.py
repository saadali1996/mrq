import time

from mrq.task import Task


class SortedTask(Task):
    def run(self, params):
        print('Sorted Set Payload {0}'.format(params))
        time.sleep(1)
        return


class SetTask(Task):
    def run(self, params):
        print('Set Payload {0}'.format(params))
        time.sleep(1)
        return


class RawTask(Task):
    def run(self, params):
        print('Raw Payload {0}'.format(params))
        time.sleep(1)
        return
