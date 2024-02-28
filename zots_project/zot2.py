import zot
import dna
import os


class ZotFactory(zot.Zot):
    """
    A factory class for creating and naming Zot files. Inherits from zot.Zot.

    Attributes:
        Inherits all attributes from the zot.Zot class.
    """

    def name_zot_files(self):
        """
        Generates a new filename based on the current file's name,
        incrementing an embedded numerical index by one.

        Returns:
            new_file (str): The new filename with the incremented index.
        """
        current_file = os.path.basename(__file__)
        index_number = current_file[3:-3]
        new_index_number = int(index_number) + 1
        new_file = current_file[:-4] + str(new_index_number) + ".py"

        return new_file

    def create_new_zot(self):
        """
        Creates a new Zot file by copying the content from the current script
        to a new file with an incremented index in its name.

        Side effects:
            Writes to a new file in the current directory.
            Prints out a confirmation message with the name of the created file.
        """
        current_script = __file__
        new_file = self.name_zot_files()
        with open(current_script, 'r') as file:
            content = file.read()

        with open(new_file, 'w') as file:
            file.write(content)

        print(f"created {new_file}")


def main():
    """
    Main function to create and modify a Zot instance.

    Side effects:
        Modifies the state of a zot.Zot instance.
        Prints out the template name and menu list of the modified Zot instance.
    """
    zot1 = zot.Zot(state=dna.Home())
    zot1._dna.change_state_next_phase()
    print(f"{zot1._dna.template_name} + \t + {zot1._dna.menu_list}")



if __name__ == "__main__":
    main()
