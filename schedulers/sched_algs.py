from queue import PriorityQueue
from schedulers.utils import RunTask, compute_static_level

def add_schedule_pairs(task, nodes, pq):
    taskset[task.taskid] = task
    task.set_added(True)

    for i in range(0, len(nodes)):
        pq.push((nodes[i], task))
        entry.add_pair(i, nodes[i], task)

#def update_start(node, task, )



# Early time first algorithm
def etf(dag, no_nodes):
    pq = PriorityQueue()
    taskset = []
    visited = no_nodes * [False]
    compute_static_level(dag, visited)

    #pq.push(dag)

    #while not pq.empty():
    #    (node, task) = pq.pop()
    #    taskset[task.taskid] = None


# Highest Level First with Estimated Time
#def hleft

# Modified Critical Path
#def mcp
