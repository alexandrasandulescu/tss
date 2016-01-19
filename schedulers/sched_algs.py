from queue import PriorityQueue
from schedulers.utils import RunTask

def add_schedule_pairs(task, nodes, pq):
    taskset[task.taskid] = task
    task.set_added(True)

    for i in range(0, len(nodes)):
        pq.push((nodes[i], task))
        entry.add_pair(i, nodes[i], task)

#def update_start(node, task, )



# Early time first algorithm
def etf(dag):
    #TODO compute static level
    pq = PriorityQueue()
    taskset = []

    #add_schedule_pairs(entry, nodes, pq)

    while not pq.empty():
        (node, task) = pq.pop()
        taskset[task.taskid] = None




# Highest Level First with Estimated Time
#def hleft

# Modified Critical Path
#def mcp
