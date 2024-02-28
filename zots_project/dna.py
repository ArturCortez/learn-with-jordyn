"""
The DNA will create the inputs for the template render on the Zot.
List of inputs to change with each State:
1. A different external file template.
2. Different Title
3. a different list to be looped thru

"""

import abc


class Dna:
    """
    This is the Context class, the class that encapsulates the concrete classes and the abstract classes.
    """
    _state = None

    def __init__(self, state: "State") -> None:
        """
        This initializer works by immediately calling the transition_to method, adding the state to any Dna object.
        :param state: A state object is necessary in order to initialize this object
        """
        print("Initializing DNA ")
        self._zot = None
        self._template_name = ""
        self._menu_list = []
        self._filename = ""
        self.transition_to(state)

    @property
    def zot(self) -> "Zot":
        return self._zot

    @zot.setter
    def zot(self, zot: "Zot") -> None:
        self._zot = zot

    @property
    def template_name(self) -> str:
        """
        The template name property, we used the decorator property to create a getter and setter-like way.
        """
        return self._template_name

    @template_name.setter
    def template_name(self, name: str):
        """Sets the template name after validating it is a string."""
        if not isinstance(name, str):
            raise TypeError("Template name must be of type string")
        self._template_name = name

    @property
    def main_name(self) -> str:
        return self._main_name

    @main_name.setter
    def main_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("main_name must be a string")
        self._main_name = value

    @property
    def menu_list(self) -> list:
        return self._menu_list

    @menu_list.setter
    def menu_list(self, value: list):
        if not isinstance(value, list):
            raise ValueError("menu_list must be a list")
        self._menu_list = value

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, value: str):
        if not isinstance(value, str):
            raise ValueError("filename must be a string")
        self._filename = value

    def transition_to(self, state: "State") -> None:
        """
        Applies a State to the Dna
        :param state: The State abstract object to be implemented
        """
        self._state = state
        print(f"DNA: Transition to {type(state).__name__}")
        self._state.dna = self
        self._state.actions()

    def change_state_next_phase(self) -> None:
        if self._state:
            self._state.change_next_phase()
            return
        print("No state set to be changed")

    def request1(self) -> None:
        """
        Changes the phase of the state via DNA.
        """
        self.change_state_next_phase()


class State(abc.ABC):
    """
    This is the abstract class the will provide the blueprint for each State.
    """

    def __init__(self) -> None:
        self._dna = None

    @abc.abstractmethod
    def actions(self) -> None:
        """
        This abstract method must be implemented on every state.
        """
        pass

    @property
    def dna(self) -> Dna:
        return self._dna

    @dna.setter
    def dna(self, dna: Dna) -> None:
        self._dna = dna

    def change_next_phase(self) -> None:
        """
        This abstract method must be implemented on every state. It changes the state to a next state provided by the
        concrete class below. The order is arbitrary.
        """
        pass


class Home(State):
    def __init__(self) -> None:
        super().__init__()

    def actions(self) -> None:
        self.dna.template_name = "Home"
        self.dna.menu_list = ["Products", "Price", "Press", "Contact Us"]
        self.dna.filename = "index.html"
        print(f"adding state {self.dna.template_name}")

    def change_phase_products(self) -> None:
        self.dna.transition_to(Products())

    def change_phase_price(self) -> None:
        self.dna.transition_to(Price())

    def change_phase_press(self) -> None:
        self.dna.transition_to(Press())

    def change_phase_contact_us(self) -> None:
        self.dna.transition_to(ContactUs())

    def change_next_phase(self) -> None:
        self._dna.transition_to(Products())


class Products(State):
    def __init__(self) -> None:
        super().__init__()

    def actions(self) -> None:
        self.dna.template_name = "Products"
        self.dna.menu_list = ["Software as a Service", "Software as a Software", "Software as Code", "Code as Code",
                              "Bits as Bits"]
        self.dna.filename = "products.html"
        print(f"adding state {self.dna.template_name}")

    def change_phase_home(self) -> None:
        self.dna.transition_to(Home())

    def change_phase_price(self) -> None:
        self.dna.transition_to(Price())

    def change_phase_press(self) -> None:
        self.dna.transition_to(Press())

    def change_phase_contact_us(self) -> None:
        self.dna.transition_to(ContactUs())

    def change_next_phase(self) -> None:
        self.dna.transition_to(Price())


class Price(State):
    def __init__(self) -> None:
        super().__init__()

    def actions(self) -> None:
        self.dna.template_name = "Price"
        self.dna.menu_list = ["$100/month", "$200/month", "1000/year"]
        self.dna.filename = "Price.html"
        print(f"adding state {self.dna.template_name}")

    def change_phase_products(self) -> None:
        self.dna.transition_to(Products())

    def change_phase_price(self) -> None:
        self.dna.transition_to(Home())

    def change_phase_press(self) -> None:
        self.dna.transition_to(Press())

    def change_phase_contact_us(self) -> None:
        self.dna.transition_to(ContactUs())

    def change_next_phase(self) -> None:
        self.dna.transition_to(Press())


class Press(State):
    def __init__(self) -> None:
        super().__init__()

    def actions(self) -> None:
        self.dna.template_name = "Press"
        self.dna.menu_list = ["Newspaper", "Magazines", "TV Shows", "Social Media"]
        self.dna.filename = "press.html"
        print(f"adding state {self.dna.template_name}")

    def change_phase_products(self) -> None:
        self.dna.transition_to(Products())

    def change_phase_price(self) -> None:
        self.dna.transition_to(Price())

    def change_phase_press(self) -> None:
        self.dna.transition_to(Home())

    def change_phase_contact_us(self) -> None:
        self.dna.transition_to(ContactUs())

    def change_next_phase(self) -> None:
        self.dna.transition_to(ContactUs())


class ContactUs(State):
    def __init__(self) -> None:
        super().__init__()

    def actions(self) -> None:
        self.dna.template_name = "Contact us"
        self.dna.menu_list = ["Phone", "Postal Code", "Email", "SMS", "Direct Message"]
        self.dna.filename = "contact_us.html"
        print(f"adding state {self.dna.template_name}")

    def change_phase_products(self) -> None:
        self.dna.transition_to(Products())

    def change_phase_price(self) -> None:
        self.dna.transition_to(Price())

    def change_phase_press(self) -> None:
        self.dna.transition_to(Press())

    def change_phase_contact_us(self) -> None:
        self.dna.transition_to(Home())

    def change_next_phase(self) -> None:
        self.dna.transition_to(Home())


if __name__ == "__main__":
    dna1 = Dna(Home())
    dna1._state.actions()
    dna1.request1()
