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

    def write_method(self):
        current_script = __file__
        new_file = self.name_zot_files()
        with open(current_script, 'r') as file:
            content = file.read()

        with open(new_file, 'w') as file:
            file.write(content)

        print(f"created {new_file}")


def main():
    zot1 = zot.Zot(dna.Home())
    zot2 = ZotFactory(zot1)
    zot2.write_method()


if __name__ == "__main__":
    main()
