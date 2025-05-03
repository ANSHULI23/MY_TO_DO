import csv
#Function to display all tasks from the CSV file
def display_tasks():
        with open('tasks.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"ID: {row[0]}, Title: {row[1]}, Description: {row[2]}, Status: {row[3]}")

# Function to add a new task to the CSV file
def add_task(title, description):
    with open('tasks.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        task_id = sum(1 for row in open('tasks.csv'))  # Get new task id
        writer.writerow([task_id, title, description, 'pending'])
    print("Task added successfully!")

# Function to mark a task as completed
def mark_completed(task_id):
    rows = []
    with open('tasks.csv', mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    for row in rows:
        if row[0] == str(task_id):
            row[3] = 'completed'
    
    with open('tasks.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f"Task {task_id} marked as completed!")

# Main function to interact with the user
def main():
    while True:
        print("\nTo-Do List App")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
        elif choice == '4':
            print("Exiting app.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()