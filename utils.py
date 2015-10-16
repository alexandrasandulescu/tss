from enum import Enum

class TaskState(Enum):
    running = 1
    ready = 2
    terminated = 3

class TaskType(Enum):
    ROOT = 1
    COMPUTATION = 2
    TRANSFER = 3
    END = 4

    def parse_type(string_t):
        if string_t == "ROOT":
            return ROOT
        if string_t == "COMPUTATION":
            return COMPUTATION
        if string_t == "TRANSFER":
            return TRANSFER
        if string_t == "END":
            return "END"
        return -1

class Task:
    """
    @brief : non-preemptable task
    @param task_id : unique task id
    @param quantums : the number of quantums the task needs to run
    """
    def __init__(self, task_id, task_type, memory=0, flops=0):
        self.task_id = task_id
        self.task_type = task_type
        self.memory = memory
        self.flops = flops
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
