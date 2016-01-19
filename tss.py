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
        self.dag = DAG()
        self.ready = PriorityQueue()
        self.running = {}

    def add_task(self, task):
        self.dag.insert(task)

    def benchmarking(self):
        print("[*] Running Earliest Time First algorithm with " + str(self.cores) + " cores")
        etf(self.dag)


def main():
    print("[*] Task scheduler simulator started ...")
    print("[*] Configuring the environment ...")
    parser = Parser()
    # skip first 2 lines
    sys.stdin.readline()
    sys.stdin.readline()
    parser.parse()
    scheduler = Scheduler(4)
    scheduler.benchmarking()

if __name__ == "__main__":
    main()
