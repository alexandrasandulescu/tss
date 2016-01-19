from schedulers.utils import RunTask, compute_static_level
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
def hleft(dag, no_nodes):
    scheduling = {}
    # initialize empty task list for each processor
    for node in range(0, no_nodes):
        scheduling[node] = []

    L = dag.listify()
    L.sort(key=lambda task: task.static_level)

    while len(L) > 0:
        task = L.pop()
        min_node = 0
        for node in scheduling:
            processor_finish(scheduling[node])

    return scheduling

def processor_finish(tasks):
    if tasks:
        return tasks[-1].finish()

    return 0

# Modified Critical Path
#def mcp
