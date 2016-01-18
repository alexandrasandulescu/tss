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
            return TaskType.ROOT
        if string_t == "COMPUTATION":
            return TaskType.COMPUTATION
        if string_t == "TRANSFER":
            return TaskType.TRANSFER
        if string_t == "END":
            return TaskType.END
        return -1

    def get_string(index):
        if index == TaskType.ROOT:
            return "ROOT"
        if index == TaskType.COMPUTATION:
            return "COMPUTATION"
        if index == TaskType.TRANSFER:
            return "TRANSFER"
        if index == TaskType.END:
            return "END"
        return ""



class Task:
    """
    @brief : non-preemptable task
    @param task_id : unique task id
    @param quantums : the number of quantums the task needs to run
    """
    def __init__(self, task_id, task_type, cost=0, memory=0, flops=0):
        self.task_id = task_id
        self.task_type = task_type
        self.memory = memory
        self.flops = flops
        self.state = TaskState.ready
        self.cost = cost
        self.finish = 0

    def print(self):
        print(TaskType.get_string(self.task_type) + " id " + str(self.task_id))

    def set_finish(self, finish):
        self.finish = finish

class DAG:
    """
    @brief : graph
    """
    def __init__(self):
        self.parent = None
        self.task = None
        self.kids = []
        self.children_indices = []

    def insert(self, task, children_indices):
        # who is the parent of this task
        child = DAG()
        child.parent = self
        child.task = task
        child.kids = []
        child.children_indices = children_indices
        self.kids += [child]
        for kid in self.kids:
            inserted = kid.insert_rec(child)
            if inserted:
                return True
        # if no place found, insert it in the root
        self.kids += [child]
        self.children_indices += [task.task_id]

    def insert_rec(self, child_dag):
        if not len(self.children_indices):
            return False
        if child_dag.task.task_id in self.children_indices:
            self.kids += [child_dag]
            return True
        for kid in self.kids:
            inserted = kid.insert_rec(child_dag)
            if inserted:
                return True
        return False

    def print(self):
        for kid in self.kids:
            if kid.task:
                kid.task.print()
            kid.print()
        print(len(self.kids))
