from queue import PriorityQueue
from parser import Parser
from utils import DAG
from schedulers.sched_algs import etf
import sys

class Scheduler:
    """
    @brief : running is a dict that holds the assignment of tasks to cores
    """
    def __init__(self, cores):
        self.cores = cores
        self.ready = PriorityQueue()
        self.running = {}
        self.parser = Parser()

    def compute_makespan(scheduling):
        # TODO compute with finish time
        makespan = -1
        for node in scheduling:
            tasks = scheduling[node]
            time = sum([task.time for task in tasks])
            makespan = max(makespan, time)
        return makespan

    def compute_flowtime(scheduling):
        # TODO compute with finish time
        flowtime = 0
        for node in scheduling:
            tasks = scheduling[node]
            finish = 0
            for task in tasks:
                finish += task.time
                flowtime += finish

        return flowtime

    def benchmarking(self):
        print("[*] Running Earliest Time First algorithm with " + str(self.cores) + " cores")
        etf(self.parser.dag, self.parser.no_nodes)
        scheduling = etf(self.dag)
        makespan = compute_makespan(scheduling)


def main():
    print("[*] Task scheduler simulator started ...")
    print("[*] Configuring the environment ...")
    parser = Parser()
    # skip first 2 lines
    sys.stdin.readline()
    sys.stdin.readline()
    scheduler = Scheduler(4)
    scheduler.parser.parse()
    scheduler.benchmarking()

if __name__ == "__main__":
    main()
