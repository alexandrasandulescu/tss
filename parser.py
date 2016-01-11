import sys
from utils import DAG, Task, TaskType


class Parser:
    """
    @brief : parses input task graph with the following stucture
    NODE <index> <children list> <node type> <node cost> <parallelization overhead>
    <node type> : ROOT, COMPUTATION, TRANSFER, END

    @return : DAG
    """

    def __init__(self):
        self.no_nodes = 0
        self.dag = DAG()

    def parse(self):
        for line in sys.stdin:
            task_info = line.split()
            if task_info[0] == "NODE_COUNT":
                self.no_nodes = int(task_info[1])
                continue

            if task_info[0] != "NODE":
                continue
            task_type = TaskType.parse_type(task_info[3])
            memory = flops = 0
            if task_type == TaskType.COMPUTATION:
                flops=int(task_info[4])
            elif task_type == TaskType.TRANSFER:
                memory=int(task_info[4])

            t = Task(task_id=int(task_info[1]),
                    task_type=task_type,
                    memory=memory, flops=flops)
            children = task_info[2].split(',')
            self.dag.insert(t, children)
        self.dag.print()

