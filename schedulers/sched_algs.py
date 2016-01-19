from schedulers.utils import RunTask, compute_static_level
from utils import listify
import heapq

def add_schedule_pairs(task, nodes, pq):
    taskset[task.taskid] = task
    task.set_added(True)

    for i in range(0, len(nodes)):
        pq.push((nodes[i], task))
        entry.add_pair(i, nodes[i], task)

#def update_start(node, task, )



# Early time first algorithm
def etf(dag, no_nodes):
    hq = []
    heapq.heappush(hq, (0, dag))

    #while not pq.empty():
    #    (node, task) = pq.pop()
    #    taskset[task.taskid] = None
    return {}


# Highest Level First with Estimated Time
def hlfet(dag, no_nodes):
    scheduling = {}
    # initialize empty task list for each processor
    for node in range(0, no_nodes):
        scheduling[node] = []

    L = listify(dag)
    L.sort(key=lambda task: task.static_level)

    while len(L) > 0:
        task = L.pop()
        min_node = 0
        min_val = processor_finish(scheduling[0])
        for node in scheduling:
            t = processor_finish(scheduling[node])
            m = max(t, task.est)
            if m < min_val:
                min_val = m
                min_node = node
        scheduling[min_node].append(task)
        task.start = min_val

    return scheduling

def processor_finish(tasks):
    if len(tasks) > 0:
        return (tasks[-1]).finish()

    return 0

# Modified Critical Path
#def mcp
