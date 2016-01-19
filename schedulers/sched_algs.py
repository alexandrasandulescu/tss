from utils import listify
import sys

def add_schedule_pairs(task, nodes, pq):
    taskset[task.taskid] = task
    task.set_added(True)

    for i in range(0, len(nodes)):
        pq.push((nodes[i], task))
        entry.add_pair(i, nodes[i], task)

#def update_start(node, task, )

def compare_dags(node):
    return node.task.est

# Early time first algorithm
def etf(dag, no_nodes):
    pq = [dag]
    scheduling = {}
    for i in range(0, no_nodes):
        scheduling[i] = []

    while pq:
        pq.sort(key=compare_dags)
        node = None
        # If ties, compare static level
        if len(pq) > 1 and (pq[0].task.est == pq[1].task.est):
            if pq[0].task.static_level > pq[1].task.static_level:
                node = pq.pop(0)
            else:
                node = pq.pop(1)
        if node == None:
            node = pq.pop(0)
        # Select processor

        min_core = -1
        min_est = sys.maxsize
        for i in range(0, no_nodes):
            est = sum([d.task.time for d in scheduling[i]])
            if est + node.task.est < min_est:
                min_est = est + node.task.est
                min_core = i
        scheduling[min_core] += [node.task]

        #find the processor
    return scheduling


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
