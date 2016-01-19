def compute_static_level(dag, visited):

    if visited[dag.task.task_id]:
        return
    if len(dag.kids) == 0:
        return

    for kid in dag.kids:
        compute_static_level(kid, visited)

    dag.task.static_level = dag.task.time + \
            max([dag_kid.task.static_level for dag_kid in dag.kids])
    visited[dag.task.task_id] = True

def compute_est(dag, visited):
    queue = [dag]
    while queue:
        node = queue.pop(0)
        if  not visited[node.task.task_id]:
            if len(node.parent) == 0:
                node.task.est = 0
            else:
                node.task.est = max(p.task.est + p.task.time \
                        for p in node.parent)
            visited[node.task.task_id] = True
            queue += [k for k in node.kids if not visited[k.task.task_id]]
