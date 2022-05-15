import sqlite3
import re
import os
import requests

from PySide6.QtWidgets import QDialog

import UI.addbooksdialog as addbkdialog
import UI.deletebooksdialog as delbkdialog
import UI.bookdetails as bookdetails
import UI.issuebook as issuebook

import Utils.members as mem
import Utils.library as lib

from Utils.foldermaker import home


# Dialog window to add more users to the member table
class AddBookDialog(QDialog, addbkdialog.Ui_addbookdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

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

        self.isbndata = None  # Data from search is stored in here to enter into the db

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.inputtitle.setText('')
        self.inputauthor.setText('')
        self.inputgenre.setText('')
        self.inputtotal.setText('')
        self.error.setText('')

    def clearfieldsisbn(self):
        self.isbnfield.setText('')
        self.authorisbn.setText('-')
        self.titleisbn.setText('-')
        self.publisherisbn.setText('-')
        self.errorisbn.setText('')
        self.totalfieldisbn.setText('')

    def getfields(self):
        title = self.inputtitle.text()
        author = self.inputauthor.text()
        genre = self.inputgenre.text()
        totalcopies = self.inputtotal.text()

        if check(title, 'title') is False:
            self.error.setText('Error: Enter a valid title!')
            return
        else:
            self.error.setText('')

        if check(author, 'author') is False:
            self.error.setText('Error: Enter a valid First and Last Name!')
            return
        else:
            self.error.setText('')

        if check(genre, 'genre') is False:
            self.error.setText('Error: Enter a valid genre!')
            return
        else:
            self.error.setText('')

        if totalcopies.isnumeric() is False:
            self.error.setText('Error: Enter a number for total copies!')
            return
        else:
            totalcopies = int(totalcopies)
            if totalcopies < 1 or totalcopies > 100:
                self.error.setText('Error: Enter in the range 1-100')
                return
            else:
                self.error.setText('')

        insert(title, author, genre, totalcopies)
        self.adminwindow.loadbook()  # Refreshes the book table after adding books
        self.close()

    def getsearchresultsisbn(self):
        isbn = self.isbnfield.text()
        if isbn.isnumeric() is False:
            self.errorisbn.setText('Error: Invalid ISBN!')
            return
        else:
            self.errorisbn.setText('')

        link = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn

        # Checking internet before sending API request
        try:
            requests.get('https://www.google.com/', timeout=1)
        except (requests.ConnectionError, requests.Timeout):
            self.errorisbn.setText('Error: No internet connection!')
            return
        self.errorisbn.setText('')

        response = requests.get(link)
        if response.status_code != 200:
            self.errorisbn.setText('Error: Unable to search for book!')
            return
        else:
            self.errorisbn.setText('')

        book = response.json()['items'][0]

        self.isbndata = {
            'title': book['volumeInfo']['title'],
            'authors': ', '.join(book['volumeInfo']['authors']),
            'publisher': book['volumeInfo']['publisher'],
            'genre': ', '.join(book['volumeInfo']['categories'])
        }

        self.titleisbn.setText(self.isbndata['title'])
        self.authorisbn.setText('By: ' + self.isbndata['authors'])
        self.publisherisbn.setText('Published by: ' + self.isbndata['publisher'])


class DeleteBookDialog(QDialog, delbkdialog.Ui_deletebookdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Button actions
        self.deletebutton.clicked.connect(self.deletebook)
        self.closebutton.clicked.connect(self.close)

    def makedialog(self):
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.errorlabel.setText('')
        self.exec()  # Runs the dialog window

    def getlist(self):
        self.booklist.clear()
        bookdata = readall()
        if len(bookdata) != 0:
            position = 0
            for row in bookdata:
                self.booklist.insertItem(position, f"{row[0]} - {row[1]} by {row[2]}")
                position = position + 1
            self.booklist.item(0).setSelected(True)

    def deletebook(self):
        bookdata = self.booklist.currentItem()
        if bookdata is not None:
            self.errorlabel.setText('')
            idtodelete = bookdata.text().split('-')[0].rstrip()
            if delete(idtodelete) is False:
                self.errorlabel.setText('Error: Book issued by a member!')
            self.getlist()
            self.adminwindow.loadbook()  # Refreshes the book table after deleting books
        else:
            self.errorlabel.setText('Error: Select an entry!')


class BookDetailsDialog(QDialog, bookdetails.Ui_bookdetaildialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

    def makedialog(self, item):
        self.setfields(item)  # Sets the detail fields in the dialog window
        self.exec()  # Runs the dialog window

    def setfields(self, item):
        text = item.text()
        beg = text.find('<') + 5
        end = text.find('>')
        idtodisplay = int(text[beg:end])
        data = readwithid(idtodisplay)
        self.idfield.setText(str(data[0][0]))
        self.titlefield.setText(data[0][1])
        self.authorfield.setText(data[0][2])
        self.ratingfield.setText(str(data[0][3]))
        self.genrefield.setText(data[0][4])
        self.datefield.setText(data[0][5])
        self.totalfield.setText(str(data[0][6]))
        self.issuedfield.setText(str(data[0][7]))


class IssueBooksDialog(QDialog, issuebook.Ui_issuebookdialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        self.item = None  # This field will contain the book that is to be issued

        # Button actions
        self.closebutton.clicked.connect(self.close)
        self.issuebutton.clicked.connect(self.issuebook)

    def makedialog(self, item):
        self.item = item
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.issuelabel.setText('')
        self.exec()  # Runs the dialog window

    def getlist(self):
        self.memlist.clear()
        memdata = mem.readall()
        if len(memdata) != 0:
            position = 0
            for row in memdata:
                self.memlist.insertItem(position, f"{row[0]} - {row[1]} - ({row[2]})")
                position = position + 1
            self.memlist.item(0).setSelected(True)

    def issuebook(self):
        memdata = self.memlist.currentItem()
        if memdata is not None:
            text = self.item.text()
            beg = text.find('<') + 5
            end = text.find('>')
            bookid = int(text[beg:end])
            text = memdata.text()
            splittext = text.split('-')
            memid = int(splittext[0])
            lib.insert(memid, bookid)
            self.issuelabel.setText(f'Book issued to {splittext[1].strip()}')


###############################################
# All the helper functions for the dialog boxes
###############################################


def initialise():
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Books(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    rating INTEGER,
    genre TEXT NOT NULL,
    add_date TEXT NOT NULL,
    copies_total INTEGER NOT NULL,
    copies_issued INTEGER NOT NULL
    CHECK (rating > 0 AND rating < 6)
    )
    ''')

    connection.commit()
    connection.close()


def check(data, field):
    regex = {
        'title': "^[A-Za-z0-9\s\-,\.;:()]+$",
        'author': "^[A-Z][a-z]+\s[A-Z][a-z]+$",
        'genre': "^[A-Za-z\s\-]+$"
    }
    validate = re.search(regex[field], data)
    if validate is None:
        return False
    else:
        return True


def insert(title, author, genre, totalcopies):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Books(title, author, rating, genre, add_date, copies_total, copies_issued) 
    VALUES(?, ?, NULL, ?, datetime('now','localtime'), ?, 0)''', (title, author, genre, totalcopies,))

    connection.commit()
    connection.close()


def delete(idtodelete):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM Books WHERE id=?", (idtodelete,))
    except sqlite3.IntegrityError:
        return False

    connection.commit()
    connection.close()
    return True


def readall():
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readsorted(sortingdata):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    # viewfilter and genre
    constraint = ''
    if sortingdata[0]['available']:
        constraint = ' WHERE copies_issued < copies_total'
        if sortingdata[2] != 'No Genre':
            constraint = constraint + ' AND genre = ' + f"\'{sortingdata[2]}\'"
    elif sortingdata[0]['all']:
        if sortingdata[2] != 'No Genre':
            constraint = ' WHERE genre = ' + f"\'{sortingdata[2]}\'"

    # sortfilter
    sortconstraint = ' ORDER BY '
    if sortingdata[1]['title']:
        sortconstraint = sortconstraint + 'title'
    elif sortingdata[1]['author']:
        sortconstraint = sortconstraint + 'author'
    elif sortingdata[1]['rating']:
        sortconstraint = sortconstraint + 'rating DESC'

    maincommand = 'SELECT * FROM Books'
    command = maincommand + constraint + sortconstraint

    cursor.execute(command)
    data = cursor.fetchall()

    connection.close()
    return data


def readgenre():
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT DISTINCT genre FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readwithid(idtodisplay):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Books WHERE id = ?', (idtodisplay,))
    data = cursor.fetchall()

    connection.close()
    return data


initialise()  # Makes sure the table is available
