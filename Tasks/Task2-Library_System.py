from abc import ABC, abstractmethod

class LibraryItem(ABC):

    def __init__(self, title: str):
        self._status = True
        self.title = title

    @abstractmethod
    def check_in(self):
        pass

    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class Book(LibraryItem):

    def __init__(self, title: str, author: str):
        super().__init__(title)
        self.author = author

    def check_out(self):
        if self._status:
            print(f"Book '{self.title}' by {self.author} has been checked out.")
            self._status = False
        else:
            print(f"Book '{self.title}' is already checked out.")

    def check_in(self):
        if not self._status:
            print(f"Book '{self.title}' by {self.author} has been returned.")
            self._status = True
        else:
            print(f"Book '{self.title}' is already available.")

    def get_status(self):
        status = "Available" if self._status else "Not Available"
        print(f"Book '{self.title}' by {self.author} is {status}.")


class Magazine(LibraryItem):

    def __init__(self, title: str, issue_number: int):
        super().__init__(title)
        self.issue_number = issue_number

    def check_out(self):
        if self._status:
            print(f"Magazine '{self.title}' [Issue #{self.issue_number}] has been checked out.")
            self._status = False
        else:
            print(f"Magazine '{self.title}' is already checked out.")

    def check_in(self):
        if not self._status:
            print(f"Magazine '{self.title}' [Issue #{self.issue_number}] has been returned.")
            self._status = True
        else:
            print(f"Magazine '{self.title}' is already available.")

    def get_status(self):
        status = "Available" if self._status else "Not Available"
        print(f"Magazine '{self.title}' [Issue #{self.issue_number}] is {status}.")
