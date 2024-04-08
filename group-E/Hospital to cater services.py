# Consider a scenario for Hospital to cater services to different kinds of patients as Serious 
# (top priority), b) non-serious (medium priority), c) General Checkup (Least priority). 
# Implement the priority queue to cater services to the patients. 

class Hospital:
    def __init__(self):
        self.priority_queue = {
            'serious': [],
            'non_serious': [],
            'general_checkup': []
        }

    def enqueue(self, patient, priority):
        if priority not in self.priority_queue:
            print("Invalid priority level.")
            return
        self.priority_queue[priority].append(patient)

    def dequeue(self):
        for priority in ['serious', 'non_serious', 'general_checkup']:
            if self.priority_queue[priority]:
                return self.priority_queue[priority].pop(0)
        print("Queue is empty.")

    def display_queue(self):
        for priority, patients in self.priority_queue.items():
            print(f"{priority.capitalize()} patients:")
            for patient in patients:
                print(patient)
            print()

# Example usage:
hospital = Hospital()

hospital.enqueue("Patient 1", 'serious')
hospital.enqueue("Patient 2", 'non_serious')
hospital.enqueue("Patient 3", 'serious')
hospital.enqueue("Patient 4", 'general_checkup')

hospital.display_queue()

print("Processing patients...")
print("Next patient:", hospital.dequeue())
print("Next patient:", hospital.dequeue())
print("Next patient:", hospital.dequeue())
print("Next patient:", hospital.dequeue())  # Attempting to dequeue from an empty queue
