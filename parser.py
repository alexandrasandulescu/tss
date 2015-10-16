import sys
from utils import DAG

class Parser:
    """
    @brief : parses input task graph with the following stucture
    NODE <index> <children list> <node type> <node cost> <parallelization overhead>
    <node type> : ROOT, COMPUTATION, TRANSFER, END

    @return : DAG
    """

    def __init__(self):
        self.dag = DAG()

    def parse(self):
        for line in sys.stdin:
            pass

