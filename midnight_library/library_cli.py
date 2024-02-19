"""       Allow users to interact with the library system via the command line.
        Users should be able to add books, remove books, check out books, return books, and list all books."""

import cmd
from classes import Book, Library


class Library_Cli(cmd.Cmd):

    def preloop(self):
        global library
        library = Library("Midnight Library")

    prompt = '(cli) '
    intro = f'Welcome to the Library System. Type help for a list of commands'

    def do_help(self, line):
        print("""
                add,\t\t Add a new book to the library catalog
                check_out,\t Checks out a book
                list,\t\t List all books in the catalog
                name,\t\t Check the name of the library
                quit,\t\t Quit the CLI
                remove,\t\t Remove book from the catalog
                return,\t\t Return a book to the library
                """)

    def do_name(self):
        print(f"Library Name: {library.name}")

    def do_add(self, line):
        try:
            args = line.split(", ")
            if len(args) != 3:
                raise ValueError("arguments insufficient")
            title = args[0]
            author = args[1]
            isbn = args[2]
            print(title, author, isbn)
            book = Book(title, author, isbn)
            print(book.get_info())
            library.add_book(book)
        except ValueError:
            print("Try again. 'add title, author, isbn'")

    def do_remove(self, line):
        isbn = line
        try:
            print(f"remove books from the catalog")
            library.remove_book(isbn)
        except Exception as e:
            print(f"Error occurred: {e}")

    def do_check_out(self, line):
        isbn = line
        try:
            print("Checkout one book")
            library.check_out_book(isbn)
        except Exception as e:
            print(f"Error occurred: {e}")

    def do_return(self, line):
        isbn = line
        try:
            print("returning a book")
            library.return_book(isbn)
        except Exception as e:
            print(f"Error occurred: {e}")

    def do_list(self, line):
        try:
            print("Here is a list of all books")
            library.list_books()
        except Exception as e:
            print(f"Error occurred: {e}")

    def do_quit(self, line):
        """exit the CLI"""
        return True

    def postcmd(self, stop, line):
        print()
        return stop


if __name__ == '__main__':
    Library_Cli().cmdloop()
