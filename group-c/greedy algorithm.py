# Consider the scheduling problem. n tasks to be scheduled on single processor. Let t1, 
# ...,tn be durations required to execute on single processor is known. The tasks can be 
# executed in any order but one task at a time. Design a greedy algorithm for this problem 
# and find a schedule that minimizes the total time spent by all the tasks in the system. 
# (The time spent by one is the sum of the waiting time of task and the time spent on its 
# execution.)   

def greedy_schedule(tasks):
    # Sort tasks based on their durations in non-decreasing order
    sorted_tasks = sorted(tasks)

    # Initialize total time spent
    total_time = 0

    # Calculate total time spent by all tasks
    for i, task in enumerate(sorted_tasks):
        # Calculate waiting time (time spent on previous tasks)
        waiting_time = sum(sorted_tasks[:i])
        # Add waiting time and task duration to total time
        total_time += waiting_time + task

    return total_time

# Example usage:
tasks = [3, 1, 5, 2, 4]
min_total_time = greedy_schedule(tasks)
print("Minimum total time spent by all tasks:", min_total_time)

