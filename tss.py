from queue import PriorityQueue
from parser import Parser
from utils import DAG, listify
from schedulers.sched_algs import etf, hlfet
from schedulers.utils import compute_static_level, compute_est
import sys
import copy

class Scheduler:
    """
    @brief : running is a dict that holds the assignment of tasks to cores
    """
    def __init__(self, cores):
        self.cores = cores
        self.ready = PriorityQueue()
        self.running = {}
        self.parser = Parser()

    def compute_makespan(self, scheduling):
        # TODO compute with finish time
        makespan = -1
        for node in scheduling:
            tasks = scheduling[node]
            time = max([task.finish() for task in tasks])
            makespan = max(makespan, time)
        return makespan

    def compute_flowtime(self, scheduling):
        # TODO compute with finish time
        flowtime = 0
        for node in scheduling:
            tasks = scheduling[node]
            for task in tasks:
                flowtime += task.finish()

        return flowtime

    def benchmarking(self):
        print("[*] Running Earliest Time First algorithm with " + str(self.cores) + " cores")
        print("[HLFET]")
        scheduling = hlfet(self.parser.dag, self.cores)
        print(scheduling)
        makespan = self.compute_makespan(scheduling)
        flowtime = self.compute_flowtime(scheduling)
        print(makespan, flowtime)


        self.parser.dag.clear_time()
        scheduling = etf(self.parser.dag, self.cores)
        print(scheduling)
        makespan = self.compute_makespan(scheduling)
        flowtime = self.compute_flowtime(scheduling)
        print(makespan, flowtime)


def main():
    print("[*] Task scheduler simulator started ...")
    print("[*] Configuring the environment ...")
    parser = Parser()
    # skip first 2 lines
    sys.stdin.readline()
    sys.stdin.readline()

    scheduler = Scheduler(4)
    scheduler.parser.parse()

    visited = scheduler.parser.no_nodes * [False]
    compute_static_level(scheduler.parser.dag, visited)
    visited = scheduler.parser.no_nodes * [False]
    compute_est(scheduler.parser.dag, visited)

    scheduler.benchmarking()

if __name__ == "__main__":
    main()
