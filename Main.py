import SortingAlgorithms as alg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PyQt5.QtGui import QIcon
import os
from drawtree import draw_bst
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QButtonGroup
import cv2 as cv
import sys
import random as rn
import Sorting
import webbrowser
from PyQt5.QtWidgets import QMessageBox


class designWindow(QtWidgets.QMainWindow, Sorting.Ui_MainWindow):
    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)
        self.desiredList = []
        self.facebookButton.clicked.connect(lambda _: self.openLink("https://www.facebook.com/Fehmidenguir"))
        self.linkedinButton.clicked.connect(
            lambda _: self.openLink("https://www.linkedin.com/in/fehmi-denguir-5a8603134/"))
        self.instagramButton.clicked.connect(lambda _: self.openLink("https://www.instagram.com/fehmidenguir/"))
        self.inputField.textChanged.connect(self.input)
        self.sortMethod.currentTextChanged.connect(self.input)
        self.sortMethod.currentTextChanged.connect(self.changePicture)
        self.sortMethod.currentTextChanged.connect(self.changeUI)
        self.randomizeButton.clicked.connect(self.randomInput)
        self.errorCounter = 0
        self.animateButton.setDisabled(True)
        self.radioButtonGroup = QButtonGroup()
        self.radioButtonList = [self.fastSpeedButton, self.mediumSpeedButton, self.slowSpeedButton]
        for i in self.radioButtonList:
            self.radioButtonGroup.addButton(i)
            i.setDisabled(True)
        self.speed = 1
        self.radioButtonGroup.buttonClicked.connect(self.changeSpeed)
        self.animateButton.clicked.connect(self.animate)
        self.videoButton.clicked.connect(self.showVideo)
        self.linkButton.clicked.connect(self.moreInformations)

    def changeUI(self):
        if self.sortMethod.currentText() == "Binary search":
            for i in self.radioButtonList:
                i.setVisible(False)
            self.animateButton.setText("Show Tree")
        else:
            for i in self.radioButtonList:
                i.setVisible(True)
            self.animateButton.setText("Animate")

    def changeSpeed(self):
        if (self.radioButtonGroup.checkedButton().text()) == self.slowSpeedButton.text():
            self.speed = 250
        elif (self.radioButtonGroup.checkedButton().text()) == self.mediumSpeedButton.text():
            self.speed = 100
        else:
            self.speed = 1
        print(self.speed)

    def changePicture(self):
        if self.sortMethod.currentText() == "Merge sort":
            self.exampleImage.setPixmap(QtGui.QPixmap("Mergesort.png"))
        elif self.sortMethod.currentText() == "Quick sort":
            self.exampleImage.setPixmap(QtGui.QPixmap("Quicksort.png"))
        elif self.sortMethod.currentText() == "Insertion sort":
            self.exampleImage.setPixmap(QtGui.QPixmap("insertionsort.png"))
        elif self.sortMethod.currentText() == "Selection sort":
            self.exampleImage.setPixmap(QtGui.QPixmap("selection-short.png"))
        elif self.sortMethod.currentText() == "Bubble sort":
            self.exampleImage.setPixmap(QtGui.QPixmap("bubblesort.png"))
        else:
            self.exampleImage.setPixmap(QtGui.QPixmap("Binarysearchtree.jpg"))

    def openLink(self, link):
        webbrowser.open(link, new=2)

    def input(self):
        try:
            self.correctInput()
        except:
            self.wrongInput()

    def correctInput(self):
        self.desiredList = list(map(int, self.inputField.text().split())).copy()
        if (len(self.inputField.text()) >= 1):
            self.inputField.setStyleSheet("color:green;")
            self.stateField.setText("Valid input ✅")
            self.stateField.setStyleSheet("color:green;")
            if self.sortMethod.currentText() == "Merge sort":
                self.resultField.setText(" ".join(str(e) for e in alg.mergeSort(self.desiredList)))
            elif self.sortMethod.currentText() == "Quick sort":
                self.resultField.setText(" ".join(str(e) for e in alg.quick_sort(self.desiredList)))
            elif self.sortMethod.currentText() == "Insertion sort":
                self.resultField.setText(" ".join(str(e) for e in alg.insertion_sort(self.desiredList)))
            elif self.sortMethod.currentText() == "Selection sort":
                self.resultField.setText(" ".join(str(e) for e in alg.selection_sort(self.desiredList)))
            elif self.sortMethod.currentText() == "Bubble sort":
                self.resultField.setText(" ".join(str(e) for e in alg.bubble_sort(self.desiredList)))
            else:
                self.resultField.setText(" ".join(str(e) for e in alg.treesort(self.desiredList)))
            for i in self.radioButtonList:
                i.setDisabled(False)
            self.animateButton.setDisabled(False)
        else:
            self.inputField.setStyleSheet("color:black;")
            self.stateField.setText("")
            self.stateField.setStyleSheet("color:black;")
            self.resultField.setText("")
        if ((len(self.inputField.text()) >= 2)):
            if (self.inputField.text()[-2] == "-"):
                self.errorCounter -= 1

    def wrongInput(self):
        enteredList = self.inputField.text()
        self.stateField.setText("Incorrect input format , please correct it. ❌")
        self.stateField.setStyleSheet("color:red;")
        self.inputField.setStyleSheet("color:red;")
        self.resultField.setText("Wrong input format , please type a valid list. ❌")
        self.resultField.setStyleSheet("color:red;")
        if not enteredList[-1] == "-":
            self.showErrorWindow()
            self.errorCounter -= 1
            self.inputField.setText(self.inputField.text()[:-1])
        else:
            self.errorCounter += 1
        if self.errorCounter >= 2:
            self.errorCounter -= 2
            self.showErrorWindow()
            self.inputField.setText(self.inputField.text()[:-1])
        self.inputField.setStyleSheet("color:green;")
        self.resultField.setStyleSheet("color:black;")
        self.errorCounter = max(0, self.errorCounter)

    def randomInput(self):
        randomList = [rn.randrange(-99, 99) for x in range(4, 35)]
        self.inputField.setText(" ".join(str(e) for e in randomList))

    def showErrorWindow(self):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon("error.png"))
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Only integers seperated with spaces are accepted in this field...")
        msg.setInformativeText('Please try again..')
        msg.setWindowTitle("Incorrect input")
        msg.exec_()

    def moreInformations(self):
        link = ""
        if self.sortMethod.currentText() == "Merge sort":
            link = "https://www.geeksforgeeks.org/merge-sort/"
        elif self.sortMethod.currentText() == "Quick sort":
            link = "https://www.geeksforgeeks.org/quick-sort/"
        elif self.sortMethod.currentText() == "Insertion sort":
            link = "https://www.geeksforgeeks.org/insertion-sort/"
        elif self.sortMethod.currentText() == "Selection sort":
            link = "https://www.geeksforgeeks.org/selection-sort/"
        elif self.sortMethod.currentText() == "Bubble sort":
            link = "https://www.geeksforgeeks.org/bubble-sort/"
        else:
            link = "https://www.geeksforgeeks.org/binary-search-tree-data-structure/"
        self.openLink(link)

    def showVideo(self):
        video = ""
        if self.sortMethod.currentText() == "Merge sort":
            video = "Merge Sort - GeeksforGeeks.mp4"
        elif self.sortMethod.currentText() == "Quick sort":
            video = "Quick Sort - GeeksforGeeks.mp4"
        elif self.sortMethod.currentText() == "Insertion sort":
            video = "Insertion Sort - GeeksforGeeks.mp4"
        elif self.sortMethod.currentText() == "Selection sort":
            video = "Selection Sort - GeeksforGeeks.mp4"
        elif self.sortMethod.currentText() == "Bubble sort":
            video = "Bubble Sort - GeeksforGeeks.mp4"
        else:
            video = "Tree Sort - GeeksforGeeks.mp4"
        cap = cv.VideoCapture(video)

        while (cap.isOpened()):
            ret, frame = cap.read()
            try:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            except:
                cap.release()
                cv.destroyWindow(video)
            cv.imshow(video, gray)
            if cv.waitKey(25) & 0xFF == ord('q') or cv.getWindowProperty(video, 0) < 0:
                break
        cap.release()
        cv.destroyWindow(video)

    def animate(self):
        if self.sortMethod.currentText() == "Binary search":
            sys.stdout = open('tree.txt', 'w')
            draw_bst(list(map(int, self.inputField.text().split())).copy())
            sys.stdout.close()
            os.chdir("C:\\Users\Denguiros\PycharmProjects\Tri")
            os.startfile('tree.txt')
        else:
            A = list(map(int, self.inputField.text().split())).copy()
            N = len(A)
            # Get appropriate generator to supply to matplotlib FuncAnimation method.
            if self.sortMethod.currentText() == "Merge sort":
                title = "Merge sort"
                generator = alg.mergesort(A, 0, N - 1)
            elif self.sortMethod.currentText() == "Quick sort":
                title = "Quicksort"
                generator = alg.quicksort(A, 0, N - 1)
            elif self.sortMethod.currentText() == "Insertion sort":
                title = "Insertion sort"
                generator = alg.insertionsort(A)
            elif self.sortMethod.currentText() == "Selection sort":
                title = "Selection sort"
                generator = alg.selectionsort(A)
            else:
                title = "Bubble sort"
                generator = alg.bubblesort(A)
            # Initialize figure and axis.
            fig, ax = plt.subplots()
            ax.set_title(title)

            # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
            # list of rectangles (with each bar in the bar plot corresponding
            # to one rectangle), which we store in bar_rects.
            bar_rects = ax.bar(range(len(A)), A, align="edge")

            # Place a text label in the upper-left corner of the plot to display
            # number of operations performed by the sorting algorithm (each "yield"
            # is treated as 1 operation).
            text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

            # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
            # To track the number of operations, i.e., iterations through which the
            # animation has gone, define a variable "iteration". This variable will
            # be passed to update_fig() to update the text label, and will also be
            # incremented in update_fig(). For this increment to be reflected outside
            # the function, we make "iteration" a list of 1 element, since lists (and
            # other mutable objects) are passed by reference (but an integer would be
            # passed by value).
            # NOTE: Alternatively, iteration could be re-declared within update_fig()
            # with the "global" keyword (or "nonlocal" keyword).
            iteration = [0]

            def update_fig(A, rects, iteration):
                for rect, val in zip(rects, A):
                    rect.set_height(val)
                iteration[0] += 1
                text.set_text("# of operations: {}".format(iteration[0]))

            anim = animation.FuncAnimation(fig, func=update_fig,
                                           fargs=(bar_rects, iteration), frames=generator, interval=self.speed,
                                           repeat=False)
            plt.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = designWindow()
    form.show()
    form.update()
    app.exec_()


if __name__ == "__main__":
    main()
