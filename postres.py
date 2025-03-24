class Node:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_dessert(self, name, ingredients):
        """Add a new dessert with its list of ingredients."""
        new_node = Node(name, ingredients)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Dessert '{name}' added with ingredients: {', '.join(ingredients)}")

    def delete_dessert(self, name):
        """Delete a dessert and its ingredients."""
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                print(f"Dessert '{name}' deleted.")
                return
            previous = current
            current = current.next
        print(f"Dessert '{name}' not found.")

    def print_ingredients(self, name):
        """Print all ingredients of a given dessert."""
        current = self.head
        while current:
            if current.name == name:
                print(f"Ingredients for '{name}': {', '.join(current.ingredients)}")
                return
            current = current.next
        print(f"Dessert '{name}' not found.")

    def add_ingredients(self, name, new_ingredients):
        """Add more ingredients to a dessert."""
        current = self.head
        while current:
            if current.name == name:
                current.ingredients.extend(new_ingredients)
                print(f"Ingredients added to '{name}': {', '.join(new_ingredients)}")
                return
            current = current.next
        print(f"Dessert '{name}' not found.")

    def delete_ingredients(self, name, ingredients_to_delete):
        """Delete certain ingredients from a dessert."""
        current = self.head
        while current:
            if current.name == name:
                current.ingredients = [ing for ing in current.ingredients if ing not in ingredients_to_delete]
                print(f"Ingredients deleted from '{name}': {', '.join(ingredients_to_delete)}")
                return
            current = current.next
        print(f"Dessert '{name}' not found.")

    def remove_duplicates(self):
        """Remove all duplicate desserts based on the dessert name."""
        current = self.head
        previous = None
        seen_names = set()

        while current:
            if current.name in seen_names:
                # Remove the duplicate node
                previous.next = current.next
                print(f"Removed duplicate dessert: '{current.name}'")
            else:
                seen_names.add(current.name)
                previous = current
            current = current.next

desserts = LinkedList()
desserts.add_dessert("Cheesecake", ["cream cheese", "sugar", "eggs", "graham crackers"])
desserts.add_dessert("Brownie", ["chocolate", "flour", "sugar", "butter", "eggs"])
desserts.add_dessert("Cheesecake", ["cream cheese", "sugar", "eggs", "graham crackers"])

desserts.add_ingredients("Brownie", ["chocolate chips"])

print("\nBefore removing duplicates:")
desserts.print_ingredients("Cheesecake")
desserts.print_ingredients("Brownie")

desserts.remove_duplicates()

print("\nAfter removing duplicates:")
desserts.print_ingredients("Cheesecake")
desserts.print_ingredients("Brownie")