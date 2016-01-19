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
    @param memory, flops : the cost of the node depending on its type
    """
    def __init__(self, task_id, task_type, memory=0, flops=0):
        self.task_id = task_id
        self.task_type = task_type
        self.time = self.get_time(task_type, memory, flops)
        #print(str(self.time)+ TaskType.get_string(self.task_type))
        self.state = TaskState.ready
        self.finish = 0
        self.static_level = 0
        if self.task_type == TaskType.END:
            self.static_level = self.time

    def get_time(self, task_type, memory, flops):
        if task_type == TaskType.COMPUTATION:
            return flops / (10000 * 1024 * 1024)

        if task_type == TaskType.TRANSFER:
            return memory / (3200 * 1024 * 1024);

        return 0;

    def print(self):
        print(TaskType.get_string(self.task_type) + " id " + str(self.task_id))

    def set_finish(self, finish):
        self.finish = finish

class DAG:
    """
    @brief : graph
    @param kids : dag kids
    @param kids_indices :  unique ids of kids
    """
    def __init__(self):
        self.parent = []
        self.task = None
        self.kids = []
        self.kids_indices = []
        self.inserted_indices = []
        self.static_level = 0

    def insert(self, task, kids_indices, child):
        # who is the parent of this task
        if not (task.task_id in self.kids_indices):
            for kid in self.kids:
                child = kid.insert(task, kids_indices, child)
            return child

        if child == None:
            child = DAG()
            child.task = task
            child.kids = []
            child.kids_indices = kids_indices

        #verify if child is already here
        if task.task_id in self.inserted_indices:
            return child
        #print("parent " + str(self.task.task_id) + " added child " + str(task.task_id))

        child.parent += [self]
        self.kids += [child]
        self.inserted_indices += [child.task.task_id]
        return child

    def print(self):
        for kid in self.kids:
            if kid.task:
                kid.task.print()
            kid.print()
        print(len(self.kids))
