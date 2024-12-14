from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        """Abstract method that needs to be implemented by subclasses."""
        pass

class PushButton(Button):
    def click(self):
        print("PushButton clicked!")

# Create instances
push_button = PushButton()
# Call the click method
push_button.click()  # Output: PushButton clicked!MRO.PY
