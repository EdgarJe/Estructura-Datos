class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qtty())
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data  # The object stored in the node
        self.next = None  # Reference to the next node in the list


# Queue class implementing QueueInterface
class Queue:
    def __init__(self):
        self.front = None  # Reference to the front of the queue
        self.rear = None  # Reference to the rear of the queue
        self.size = 0     # Number of elements in the queue

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.front.data

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        self.size -= 1
        if self.is_empty():
            self.rear = None  # If the queue becomes empty, reset the rear reference
        return removed_data

    # Method to print the queue
    def print_queue(self):
        current = self.front
        while current is not None:
            current.data.print()  # Call the print method of the Order object
            current = current.next

    # Method to get an item at a specific position without removing it
    def get_item_at_position(self, position):
        if position < 0 or position >= self.size:
            return None  # Invalid position
        current = self.front
        for _ in range(position):
            current = current.next
        return current.data


# Main function to demonstrate the functionality
def main():
    # Create a queue
    queue = Queue()

    # Add 5 Order objects to the queue
    queue.enqueue(Order(10, "Alice"))
    queue.enqueue(Order(20, "Bob"))
    queue.enqueue(Order(30, "Charlie"))
    queue.enqueue(Order(40, "David"))
    queue.enqueue(Order(50, "Eve"))

    # Print the queue
    print("Queue contents:")
    queue.print_queue()

    # Demonstrate get_item_at_position
    print("\nSearching for items at specific positions:")
    print("Item at position 0:")
    item = queue.get_item_at_position(0)
    if item is not None:
        item.print()
    else:
        print("Invalid position")

    print("\nItem at position 2:")
    item = queue.get_item_at_position(2)
    if item is not None:
        item.print()
    else:
        print("Invalid position")

    print("\nItem at position 4:")
    item = queue.get_item_at_position(4)
    if item is not None:
        item.print()
    else:
        print("Invalid position")

    print("\nItem at position 5 (invalid):")
    item = queue.get_item_at_position(5)
    if item is not None:
        item.print()
    else:
        print("Invalid position")


# Run the main function
if __name__ == "__main__":
    main()