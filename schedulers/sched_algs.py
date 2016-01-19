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
#def hleft

# Modified Critical Path
#def mcp
