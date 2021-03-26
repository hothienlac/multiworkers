import queue

from .worker import Worker



class ParallelRunner:

    def __init__(self, number_of_worker, queue_size):
        self.queue      = queue.Queue(queue_size)
        self.workers    = [Worker(self.queue) for _ in range(number_of_worker)]


    def run(self, tasks):
        # Init all worker
        for worker in self.workers:
            worker.start()
        
        # Add tasks to queue
        for task in tasks:
            self.queue.put(task, block=True, timeout=3)

        # Wait for all worker done their tasks
        for worker in self.workers:
            worker.join()


