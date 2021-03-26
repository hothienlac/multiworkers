from .task                      import Task
from .worker_result_receiver    import WorkerResultReceiver



class TasksManager:

    def __init__(self, function, arguments_list, callback):
        self.function           = function
        self.arguments_list     = arguments_list
        self.callback           = callback


    def callback_not_in_order_tasks_list(self):
        for argument in self.arguments_list:
            yield Task(self.function, argument, self.callback)


    def callback_in_order_tasks_list(self):
        worker_result_receiver = WorkerResultReceiver(self.callback)

        # Feed tasks with sequential id, so handler can handle result in order
        count = 0
        for argument in self.arguments_list:
            yield Task(
                lambda argument_with_count: (argument_with_count[0], self.function(argument_with_count[1])),
                (count, argument),
                lambda result_with_count: worker_result_receiver.receive(result_with_count),
            )
            count += 1
