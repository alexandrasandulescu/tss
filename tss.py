from enum import Enum
from Queue import PriorityQueue

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


class Scheduler:
    """
    @brief : running is a dict that holds the assignment of tasks to cores
    """
    def __init__(self, cores):
        self.cores = cores
        self.dag = DAG()
        self.ready = PriorityQueue()
        self.running = {}

    def add_task(self, task):
        self.dag.insert(task)


def main():
    print("[*] Task scheduler simulator started ...")
    print("[*] Configuring the environment ...")
    scheduler = Scheduler(4)

if __name__ == "__main__":
    main()
