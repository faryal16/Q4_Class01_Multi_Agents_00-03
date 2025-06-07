import threading
import time

print("\n\t\t>>> STEP: Starting Swarm of Agents using threading")

def agent_task(name, delay):
    print(f"\n[{name}] Starting task...")
    time.sleep(delay)
    print(f"\n[{name}] Finished task after {delay} seconds.")

agents = [
    threading.Thread(target=agent_task, args=(f"Agent-{i}", i))
    for i in range(1, 4)
]

print("\n\t\t>>> STEP: Launching agent threads")
for agent in agents:
    agent.start()

print("\n\t\t>>> STEP: Waiting for all agent threads to finish")
for agent in agents:
    agent.join()

print("\n\t\t>>> DONE: All agents have completed their tasks.")
