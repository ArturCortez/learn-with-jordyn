import jinja2
from dna import Dna, Home, Products, Price, Press, ContactUs
import random


class Zot:
    """
    This is a Class that contains the DNA. The DNA and the State are implemented via transition_to method, which takes
    the Concrete Class name as argument.
    """

    def __init__(self, state: "State") -> None:
        """
        The state is between parameters because otherwise it gives an error.
        :param state: The state to be implemented on the Dna.
        """
        print("Creating zot")
        self._dna = Dna(state)

    def transition_to(self, state: "State") -> None:
        """
        This is method calls the transition of state to the DNA class
        :param state:
        :return:
        """

        self._dna.transition_to(state)

    def next_dna_phase(self) -> None:
        """
        This method changes the phase of the DNA in an arbitrary manner, like this:
        Home -> Products -> Price -> Press -> Contact Us -> Home
        :return:
        """
        if self._dna:
            self._dna.change_state_next_phase()
            return
        print("No DNA set")
        return

    def write_template(self, rendered_template: str, filename: str) -> None:
        """
        This method writes a html template to a file using 'with open'
        :param rendered_template: the template to be rendered
        :param filename: the filename
        """
        with open(filename, 'w') as file:
            file.write(rendered_template)

    def render_template(self) -> None:
        """
        This method renders the template. It is the main functionality of a Zot.
        :return:
        """
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
        template = environment.get_template("ecommerce_main.html")
        filename = self._dna.filename
        menu_list = self._dna.menu_list
        main_name = self._dna.template_name
        template_name = self._dna.template_name
        input_dict = {'main_name': main_name, 'menu_list': menu_list, 'template_name': template_name}
        html_content = template.render(input_dict)

        self.write_template(html_content, filename)

    def set_random_state(self) -> None:
        """
        This method provides a random state to a zot.
        :return:
        """
        state_list = [Home(), Products(), Price(), Press(), ContactUs()]
        random_state = random.choice(state_list)
        self.transition_to(random_state)


if __name__ == "__main__":

    while True:
        phase_dict = {"home": Home(), "products": Products(), "price": Price(), "press": Press(),
                      "contact us": ContactUs()}
        phase = input("What is the DNA template: Home, Products, Price, Press, Contact Us? ")

        if phase.lower() in phase_dict.keys():
            break

    state = phase_dict.get(phase.lower())

    zot1 = Zot(state)

    zot1.render_template()
