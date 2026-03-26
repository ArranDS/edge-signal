import random

DURATION = 60
EVENTRATE = 5
MAXBAND = 100

class Event:
    def __init__(self):
        self.confidence = random.random()
        self.size = random.randint(5, 20)
        self.type = random.choice(["A", "B", "C"])

    def score(self):
        score = self.confidence
        if self.type == "A":
            score += 0.3
        return score

def simulate():
    queue = []
    sent = 0
    dropped = 0

    for _ in range(DURATION):
        events = [Event() for _ in range(EVENTRATE)]

        for e in events:
            s = e.score()
            if s > 0.8:
                queue.insert(0, e)
            elif s > 0.5:
                queue.append(e)
            else:
                dropped += 1

        bandwidth = random.randint(40, MAXBAND)

        used = 0
        new_queue = []

        for e in queue:
            if used + e.size <= bandwidth:
                used += e.size
                sent += 1
            else:
                new_queue.append(e)

        queue = new_queue

    print("Sent:", sent)
    print("Dropped:", dropped)
    print("Remaining in queue:", len(queue))

if __name__ == "__main__":
    simulate()
