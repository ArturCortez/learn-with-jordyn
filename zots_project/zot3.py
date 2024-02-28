import zot
import dna
import os


class ZotFactory(zot.Zot):

    def name_zot_files(self):
        current_file = os.path.basename(__file__)
        index_number = current_file[3:-3]
        new_index_number = int(index_number) + 1
        new_file = current_file[:-4] + str(new_index_number) + ".py"

        return new_file

    def create_new_zot(self):
        current_script = __file__
        new_file = self.name_zot_files()
        with open(current_script, 'r') as file:
            content = file.read()

        with open(new_file, 'w') as file:
            file.write(content)

        print(f"created {new_file}")


def main():
    zot1 = zot.Zot(state=dna.Home())
    zot2 = ZotFactory(zot1)
    zot2.create_new_zot()
    zot1.next_dna_phase()
    #zot1.change_phase_contact_us()
    zot1.next_dna_phase()
    #zot1.change_phase_press()
    #zot1.set_random_state()
    print(zot1.template_name)

if __name__ == "__main__":
    main()
