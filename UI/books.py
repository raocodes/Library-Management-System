import re

import requests
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog

import DB.books
import DB.library
import DB.members
import GeneratedUI.addbooksdialog
import GeneratedUI.bookdetails
import GeneratedUI.deletebooksdialog
import GeneratedUI.issuebook


# Validator
def check(data, field):
    regex = {
        "title": r"^[A-Za-z0-9\s\-,\.;:()]+$",
        "author": r"^[A-Za-z\s\-,\.()]+$",
        "genre": r"^[A-Za-z\s\-]+$",
    }
    validate = re.search(regex[field], data)
    if validate is None:
        return False
    else:
        return True


# Dialog window to add more users to the member table
class AddBookDialog(QDialog, GeneratedUI.addbooksdialog.Ui_addbookdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        # Calls the function to create all the elements in the dialog window
        self.setupUi(self)

        # Setting field margins
        self.inputgenre.setTextMargins(5, 0, 5, 0)
        self.inputtotal.setTextMargins(5, 0, 5, 0)
        self.inputauthor.setTextMargins(5, 0, 5, 0)
        self.inputtitle.setTextMargins(5, 0, 5, 0)
        self.isbnfield.setTextMargins(5, 0, 5, 0)
        self.totalfieldisbn.setTextMargins(5, 0, 5, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)
        self.clearbuttonisbn.clicked.connect(self.clearfieldsisbn)
        self.closebuttonisbn.clicked.connect(self.close)
        self.searchbuttonisbn.clicked.connect(self.getsearchresultsisbn)
        self.submitbuttonisbn.clicked.connect(self.addisbnbook)

        # Enter action for fields
        self.inputtitle.returnPressed.connect(self.submitbutton.click)
        self.inputauthor.returnPressed.connect(self.submitbutton.click)
        self.inputgenre.returnPressed.connect(self.submitbutton.click)
        self.inputtotal.returnPressed.connect(self.submitbutton.click)
        self.isbnfield.returnPressed.connect(self.searchbuttonisbn.click)
        self.totalfieldisbn.returnPressed.connect(self.submitbuttonisbn.click)

        self.isbndata = None  # Data from search is stored in here to enter into the db

        # Setting font sizes
        font = self.titleisbn.font()
        font.setPixelSize(12)
        self.titleisbn.setFont(font)

        font = self.authorisbn.font()
        font.setPixelSize(12)
        self.authorisbn.setFont(font)

        font = self.publisherisbn.font()
        font.setPixelSize(12)
        self.publisherisbn.setFont(font)

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.inputtitle.setText("")
        self.inputauthor.setText("")
        self.inputgenre.setText("")
        self.inputtotal.setText("")
        self.error.setText("")

    def clearfieldsisbn(self):
        self.isbnfield.setText("")
        self.authorisbn.setText("-")
        self.titleisbn.setText("-")
        self.publisherisbn.setText("-")
        self.errorisbn.setText("")
        self.totalfieldisbn.setText("")

    def getfields(self):
        title = self.inputtitle.text()
        author = self.inputauthor.text()
        genre = self.inputgenre.text()
        totalcopies = self.inputtotal.text()

        if check(title, "title") is False:
            self.error.setText("Error: Enter a valid title!")
            return

        if check(author, "author") is False:
            self.error.setText("Error: Enter a valid Author Name!")
            return

        if check(genre, "genre") is False:
            self.error.setText("Error: Enter a valid genre!")
            return

        if totalcopies.isnumeric() is False:
            self.error.setText("Error: Enter a number for total copies!")
            return

        totalcopies = int(totalcopies)
        if totalcopies < 1 or totalcopies > 100:
            self.error.setText("Error: Enter in the range 1-100")
            return

        self.error.setText("")

        DB.books.insert(title, author, genre, totalcopies)
        self.adminwindow.loadbook()  # Refreshes the book table after adding books
        self.adminwindow.mainwindow.loadbooks()  # Refreshes the mainwindow book list
        self.close()

    def getsearchresultsisbn(self):
        isbn = self.isbnfield.text()
        if isbn.isnumeric() is False:
            self.errorisbn.setText("Error: Invalid ISBN!")
            return
        self.errorisbn.setText("")

        link = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn

        try:
            response = requests.get(link, timeout=2)
        except (requests.ConnectionError, requests.Timeout):
            self.errorisbn.setText("Error: Unable to search - Network issue")
            return

        if response.status_code != 200:
            self.errorisbn.setText("Error: Unable to search for book!")
            return

        if response.json()["totalItems"] == 0:
            self.errorisbn.setText("Error: Could not find book!")
            return

        self.errorisbn.setText("")

        book = response.json()["items"][0]

        self.isbndata = dict()
        keys = ["title", "authors", "publisher", "categories"]
        for key in keys:
            try:
                if isinstance(book["volumeInfo"][key], list):
                    self.isbndata[key] = ", ".join(book["volumeInfo"][key])
                else:
                    self.isbndata[key] = book["volumeInfo"][key]
            except KeyError as err:
                self.isbndata[key] = "🤷🏻‍"

        self.titleisbn.setText(self.isbndata["title"])
        self.authorisbn.setText("By: " + self.isbndata["authors"])
        self.publisherisbn.setText("Published by: " + self.isbndata["publisher"])

    def addisbnbook(self):
        if self.isbndata is None:
            self.errorisbn.setText("Error: Search for the book first!")
            return
        else:
            self.errorisbn.setText("")

        totalcopies = self.totalfieldisbn.text()
        if totalcopies.isnumeric() is False:
            self.errorisbn.setText("Error: Enter a number for total copies!")
            return
        else:
            totalcopies = int(totalcopies)
            if totalcopies < 1 or totalcopies > 100:
                self.errorisbn.setText("Error: Enter in the range 1-100")
                return
            else:
                self.errorisbn.setText("")

        DB.books.insert(
            self.isbndata["title"],
            self.isbndata["authors"],
            self.isbndata["categories"],
            totalcopies,
        )
        self.isbndata = None  # Invalidating it for future entries
        self.adminwindow.loadbook()  # Refreshes the book table after adding books
        self.adminwindow.mainwindow.loadbooks()  # Refreshes the mainwindow book list
        self.close()


class DeleteBookDialog(QDialog, GeneratedUI.deletebooksdialog.Ui_deletebookdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        # Calls the function to create all the elements in the dialog window
        self.setupUi(self)

        # Button actions
        self.deletebutton.clicked.connect(self.deletebook)
        self.closebutton.clicked.connect(self.close)

        # Timer for timeouts
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.errorlabel.setText(""))

    def makedialog(self):
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.errorlabel.setText("")
        self.exec()  # Runs the dialog window

    def getlist(self):
        self.booklist.clear()
        bookdata = DB.books.readall()
        if len(bookdata) != 0:
            position = 0
            for row in bookdata:
                self.booklist.insertItem(position, f"{row[0]} - {row[1]} by {row[2]}")
                position = position + 1

    def deletebook(self):
        bookdata = self.booklist.selectedItems()
        if len(bookdata) == 0:
            self.errorlabel.setText(f"Error: No book selected!")
            self.timer.start(3000)
            return
        else:
            self.errorlabel.setText("")
            book = bookdata[0].text()
            idtodelete = book.split("-")[0].rstrip()
            if DB.books.delete(idtodelete) is False:
                self.errorlabel.setText("Error: Book issued by a member!")
                self.timer.start(3000)
                return
            self.getlist()
            self.adminwindow.loadbook()  # Refreshes the book table after deleting books
            self.errorlabel.setText(f"{book.split('-')[1].strip()} has been deleted!")
            self.adminwindow.mainwindow.loadbooks()  # Refreshes the mainwindow book list


class BookDetailsDialog(QDialog, GeneratedUI.bookdetails.Ui_bookdetaildialog):
    def __init__(self):
        super().__init__()

        # Calls the function to create all the elements in the dialog window
        self.setupUi(self)

    def makedialog(self, item):
        self.setfields(item)  # Sets the detail fields in the dialog window
        self.exec()  # Runs the dialog window

    def setfields(self, item):
        text = item.text()
        beg = text.find("<") + 5
        end = text.find(">")
        idtodisplay = int(text[beg:end])
        data = DB.books.readwithid(idtodisplay)
        self.idfield.setText(str(data[0][0]))
        self.titlefield.setText(data[0][1])
        self.authorfield.setText(data[0][2])
        self.ratingfield.setText(str(data[0][3]))
        self.genrefield.setText(data[0][4])
        self.datefield.setText(data[0][5])
        self.totalfield.setText(str(data[0][6]))
        self.issuedfield.setText(str(data[0][7]))


class IssueBooksDialog(QDialog, GeneratedUI.issuebook.Ui_issuebookdialog):
    def __init__(self, mainwindow):
        super().__init__()

        # Used to launch the admin window after closing the dialog
        self.mainwindow = mainwindow
        # Calls the function to create all the elements in the dialog window
        self.setupUi(self)

        self.item = None  # This field will contain the book that is to be issued

        # Button actions
        self.closebutton.clicked.connect(self.close)
        self.issuebutton.clicked.connect(self.issuebook)

        # Timer for timeouts
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.issuelabel.setText(""))

    def makedialog(self, item):
        self.item = item
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.issuelabel.setText("")

        # Enabling issue button
        self.issuebutton.setDisabled(False)
        self.issuebutton.setStyleSheet(
            """
QPushButton#issuebutton{
	background-color: FireBrick;
	border-radius: 5px;
	color: white;
}

QPushButton#issuebutton:hover{
	border: 2px solid teal;
}
        """
        )

        self.exec()  # Runs the dialog window

    def getlist(self):
        self.memlist.clear()
        memdata = DB.members.readall()
        if len(memdata) != 0:
            position = 0
            for row in memdata:
                self.memlist.insertItem(position, f"{row[0]} - {row[1]} - ({row[2]})")
                position = position + 1

    def issuebook(self):
        memdata = self.memlist.selectedItems()
        if len(memdata) == 0:
            self.issuelabel.setText(f"Error: No member selected!")
            self.timer.start(3000)
            return
        else:
            text = self.item.text()
            beg = text.find("<") + 5
            end = text.find(">")
            bookid = int(text[beg:end])
            text = memdata[0].text()
            splittext = text.split("-")
            memid = int(splittext[0])
            DB.library.insert(memid, bookid)
            self.issuelabel.setText(f"Book issued to {splittext[1].strip()}")
            # Refreshing book list after issuing a book
            self.mainwindow.loadbooks()

        # Disabling button till dialog is reopened
        self.issuebutton.setDisabled(True)
        self.issuebutton.setStyleSheet(
            """
QPushButton#issuebutton{
	background-color: #656565;
	border-radius: 5px;
	color: white;
}

QPushButton#issuebutton:hover{
	border: 2px solid teal;
}
        """
        )
