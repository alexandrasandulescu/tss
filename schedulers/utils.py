class RunTask:
    """
    @param pairs : (node, job)
    """
    def __init__(self, taskid):
        self.taskid = taskid
        self.added = False
        self.pairs = []

    def set_added(self, added):
        self.added = added

    def add_pair(self, index, node, task):
        self.pairs[index] = (node, task)

class SchedulePair:

    def __init(self, task, node):
        self.task = task
        self.node = node
        self.start = 0

    def update(self):
        if self.node.finish > self.start:
            self.start = self.node.finish
            return True
        return False
