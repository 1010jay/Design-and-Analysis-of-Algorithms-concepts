# Greedy Algorithm for Job Scheduling

def schedule_jobs_min_completion_time(job_times):
   
    # Sort jobs by processing time (ascending order)
    sorted_jobs = sorted(job_times)
    
    # Calculate total completion time
    total_completion_time = 0
    current_time = 0
    job_schedule = []
    
    for job in sorted_jobs:
        current_time += job  # Completion time for the current job
        total_completion_time += current_time  # Accumulate total completion time
        job_schedule.append(job)  # Add to schedule
    
    return total_completion_time, job_schedule


# Example: Job processing times
job_times = [3, 2, 8, 6, 4]

total_time, schedule = schedule_jobs_min_completion_time(job_times)

print("Total Completion Time:", total_time)
print("Job Schedule:", schedule)
