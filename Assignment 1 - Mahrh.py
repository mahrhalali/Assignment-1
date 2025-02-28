from datetime import datetime, timedelta

class DeliveryOrder:
    """Class to manage delivery order details, items, and computation of costs."""
    def __init__(self, order_number, recipient_info, weight, dimensions, delivery_method="Courier"):
        self.order_number = order_number
        self.recipient_info = recipient_info
        self.items = []
        self.weight = weight
        self.dimensions = dimensions
        self.delivery_method = delivery_method

    def add_item(self, item):
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.get_total_price() for item in self.items)

    def calculate_taxes_and_fees(self):
        return round(self.calculate_subtotal() * 0.05, 2)

    def calculate_total(self):
        return round(self.calculate_subtotal() + self.calculate_taxes_and_fees(), 2)

class Item:
    """Class to represent an individual item in a delivery order."""
    def __init__(self, item_code, description, quantity, unit_price):
        self.item_code = item_code
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_price(self):
        return round(self.quantity * self.unit_price, 2)

class DeliveryNote:
    """Class to generate a delivery note for an order."""
    def __init__(self, note_id, order_details):
        self.note_id = note_id
        self.order_details = order_details
        self.delivery_date = datetime.now().strftime("%B %d, %Y")

    def generate_note(self):
        print("Delivery Note")
        print("Thank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.")
        print("\nRecipient Details:")
        print("Name:", self.order_details.recipient_info['name'])
        print("Contact:", self.order_details.recipient_info['contact'])
        print("Delivery Address:", self.order_details.recipient_info['address'])
        print("\nDelivery Information:")
        print("Order Number:", self.order_details.order_number)
        print("Reference Number:", self.note_id)
        print("Delivery Date:", self.delivery_date)
        print("Delivery Method:", self.order_details.delivery_method)
        print("Package Dimensions:", self.order_details.dimensions)
        print("Total Weight:", f"{self.order_details.weight} kg")
        print("\nSummary of Items Delivered:")
        for item in self.order_details.items:
            print(f"{item.item_code:<10} {item.description:<20} {item.quantity:<10} {item.unit_price:<15.2f} {item.get_total_price():<15.2f}")
        print("\nSubtotal: AED", self.order_details.calculate_subtotal())
        print("Taxes and Fees: AED", self.order_details.calculate_taxes_and_fees())
        print("Total Charges: AED", self.order_details.calculate_total())

class DeliveryStatus:
    """Class to track and update the status and location of a delivery order."""
    def __init__(self, order_number, current_status="Order Placed", current_location="Warehouse"):
        self.order_number = order_number
        self.current_status = current_status
        self.current_location = current_location

    def update_status(self, new_status):
        self.current_status = new_status
        print(f"Status updated to {new_status}")

    def update_location(self, new_location):
        self.current_location = new_location
        print(f"Location updated to {new_location}")

    def estimate_delivery_time(self):
        # Example implementation, actual logic may vary
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

status = DeliveryStatus(order.order_number)
status.update_status("In Transit")
status.update_location("Local Distribution Center")
print("Estimated Delivery Time:", status.estimate_delivery_time().strftime("%B %d, %Y"))
