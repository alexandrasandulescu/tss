from enum import Enum

class TaskState(Enum):
    running = 1
    ready = 2
    terminated = 3

class Task:
    """
    @brief : non-preemptable task
    @param task_id : unique task id
    @param quantums : the number of quantums the task needs to run
    """
    def __init__(self, task_id, parent, quantums):
        self.task_id = task_id
        self.parent = parent
        self.quantums = quantums
        self.state = TaskState.ready

class DAG:
    """
    @brief : graph 
    """
    def __init__(self):
        self.parent = None
        self.task = None
        self.kids = []

    def insert(self, task):
        return True
