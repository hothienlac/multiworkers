


# Class is to feed workers' results to handler in order
class WorkerResultReceiver:

    def __init__(self, handler):
        self.handler = handler
        self.queue = []
        self.waiting_index = 0


    def receive(self, result):
        # Insert result to right position (keep id ascending)
        # position is the current position of new added result
        position = len(self.queue)
        self.queue.append(result)
        while (position > 0) and (self.queue[position][0] < self.queue[position - 1][0]):
            temp = self.queue[position]
            self.queue[position] = self.queue[position - 1]
            self.queue[position - 1] = temp

            position -= 1
        
        # Feed result to handler if in right order
        while self.queue:
            # If waiting result is not received yet, then break
            if self.waiting_index != self.queue[0][0]:
                break

            self.handler(self.queue.pop(0)[1])
            self.waiting_index += 1
