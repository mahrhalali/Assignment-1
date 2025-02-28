from datetime import datetime, timedelta

class DeliveryOrder:
    """Class to manage delivery order details, items, and computation of costs."""
    def __init__(self, order_number, recipient_info, weight, dimensions, delivery_method="Courier"):
        self._order_number = order_number
        self._recipient_info = recipient_info
        self._items = []
        self._weight = weight
        self._dimensions = dimensions
        self._delivery_method = delivery_method

    def add_item(self, item):
        """Adds an item to the order."""
        self._items.append(item)

    # Getters
    def get_order_number(self):
        return self._order_number

    def get_recipient_info(self):
        return self._recipient_info

    def get_items(self):
        return self._items

    def get_weight(self):
        return self._weight

    def get_dimensions(self):
        return self._dimensions

    def get_delivery_method(self):
        return self._delivery_method

    # Setters
    def set_delivery_method(self, new_method):
        self._delivery_method = new_method

    def calculate_subtotal(self):
        return sum(item.get_total_price() for item in self._items)

    def calculate_taxes_and_fees(self):
        return round(self.calculate_subtotal() * 0.05, 2)

    def calculate_total(self):
        return round(self.calculate_subtotal() + self.calculate_taxes_and_fees(), 2)

class Item:
    """Class to represent an individual item in a delivery order."""
    def __init__(self, item_code, description, quantity, unit_price):
        self._item_code = item_code
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price

    # Getters
    def get_item_code(self):
        return self._item_code

    def get_description(self):
        return self._description

    def get_quantity(self):
        return self._quantity

    def get_unit_price(self):
        return self._unit_price

    # Setters
    def set_quantity(self, new_quantity):
        self._quantity = new_quantity

    def set_unit_price(self, new_price):
        self._unit_price = new_price

    def get_total_price(self):
        return round(self._quantity * self._unit_price, 2)

class DeliveryNote:
    """Class to generate a delivery note for an order."""
    def __init__(self, note_id, order_details):
        self._note_id = note_id
        self._order_details = order_details
        self._delivery_date = datetime.now().strftime("%B %d, %Y")

    # Getters
    def get_note_id(self):
        return self._note_id

    def get_delivery_date(self):
        return self._delivery_date

    def generate_note(self):
        """Prints the delivery note in a formatted structure."""
        print("Delivery Note")
        print("Thank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.")
        print("\nRecipient Details:")
        print("Name:", self._order_details.get_recipient_info()['name'])
        print("Contact:", self._order_details.get_recipient_info()['contact'])
        print("Delivery Address:", self._order_details.get_recipient_info()['address'])
        print("\nDelivery Information:")
        print("Order Number:", self._order_details.get_order_number())
        print("Reference Number:", self.get_note_id())
        print("Delivery Date:", self.get_delivery_date())
        print("Delivery Method:", self._order_details.get_delivery_method())
        print("Package Dimensions:", self._order_details.get_dimensions())
        print("Total Weight:", f"{self._order_details.get_weight()} kg")
        print("\nSummary of Items Delivered:")
        print(f"{'Item Code':<10} {'Description':<20} {'Quantity':<10} {'Unit Price':<15} {'Total Price':<15}")
        for item in self._order_details.get_items():
            print(f"{item.get_item_code():<10} {item.get_description():<20} {item.get_quantity():<10} {item.get_unit_price():<15.2f} {item.get_total_price():<15.2f}")
        print("\nSubtotal: AED", self._order_details.calculate_subtotal())
        print("Taxes and Fees: AED", self._order_details.calculate_taxes_and_fees())
        print("Total Charges: AED", self._order_details.calculate_total())

class DeliveryStatus:
    """Class to track and update the status and location of a delivery order."""
    def __init__(self, order_number, current_status="Order Placed", current_location="Warehouse"):
        self._order_number = order_number
        self._current_status = current_status
        self._current_location = current_location

    # Getters
    def get_order_number(self):
        return self._order_number

    def get_current_status(self):
        return self._current_status

    def get_current_location(self):
        return self._current_location

    # Setters
    def set_current_status(self, new_status):
        self._current_status = new_status

    def set_current_location(self, new_location):
        self._current_location = new_location

    def update_status(self, new_status):
        """Updates the order status and prints the update."""
        self.set_current_status(new_status)
        print(f"Status updated to {new_status}")

    def update_location(self, new_location):
        """Updates the order location and prints the update."""
        self.set_current_location(new_location)
        print(f"Location updated to {new_location}")

    def estimate_delivery_time(self):
        """Returns the estimated delivery time."""
        return datetime.now() + timedelta(days=2)


# Example usage
recipient_info = {
    'name': "Sarah Johnson",
    'contact': "sarah.johnson@example.com",
    'address': "45 Knowledge Avenue, Dubai, UAE"
}

order = DeliveryOrder("DEL123456789", recipient_info, 7, "Not specified")
order.add_item(Item("ITM001", "Wireless Keyboard", 1, 100.00))
order.add_item(Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00))
order.add_item(Item("ITM003", "Laptop Cooling Pad", 1, 120.00))
order.add_item(Item("ITM004", "Camera Lock", 3, 15.00))

note = DeliveryNote("DN-2025-001", order)
note.generate_note()

status = DeliveryStatus(order.get_order_number())
status.update_status("In Transit")
status.update_location("Local Distribution Center")
print("Estimated Delivery Time:", status.estimate_delivery_time().strftime("%B %d, %Y"))
