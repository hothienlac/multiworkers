from threading import Thread
import queue



class Worker(Thread):

    def __init__(self, tasks_queue):
        super().__init__()
        self.tasks_queue = tasks_queue
    

    def run(self):
        while True:
            try:
                task = self.tasks_queue.get(timeout=3)
            except queue.Empty:
                return
            
            task.run()


