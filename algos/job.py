def find_min_completion_time(jobs):
    n = len(jobs)
    completion_times = [0] * n
    start_times = [0] * n

    jobs.sort(key=lambda x: x[1])  # Sort jobs by their deadlines

    for job in jobs:
        deadline = job[1]
        duration = job[0]

        # Find the latest available time slot before the deadline
        for i in range(min(n, deadline) - 1, -1, -1):
            if start_times[i] == 0:
                start_times[i] = 1
                completion_times[i] = i + duration
                break

    return max(completion_times)

# Example usage
jobs = [(3, 6), (2, 8), (5, 4), (6, 7)]
min_completion_time = find_min_completion_time(jobs)
print("Minimum completion time:", min_completion_time)

