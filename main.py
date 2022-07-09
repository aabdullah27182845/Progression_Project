import os
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QUrl
import math

def readingFile():
    file = open("experienceInfo.txt", 'r')
    lines = file.readlines()
    file.close()
    return lines
    

def writingToFile(newValues):
    print(newValues)
    file = open("experienceInfo.txt", 'w')
    for i in range(len(newValues)):
        file.writelines(newValues[i])
    file.close()


def learningCurve(Level):
    e = math.e
    output = 10000*(1-e**(-0.075*Level))
    output = int(output)
    return output


def findLevelAndXp(currentExperience):
    level = 0
    currentExperience = int(currentExperience)
    while currentExperience >= 0:
        currentExperience -= learningCurve(level)
        level += 1
    return [level - 1, currentExperience + learningCurve(level -1)]


def currentXpRange(Level, currentExperience):
    for i in range(Level):
        currentExperience = int(currentExperience) - learningCurve(i)
    return currentExperience


def normalise(Level, currentExperience):
    percentage = (int(currentExperience)/learningCurve(Level)) * 100
    if percentage < 100:
        return percentage
    else:
        return -1

def rollOver(Level, currentExperience):
    for i in range(Level + 1):
        currentExperience = int(currentExperience) - learningCurve(i)
    carryPercentage = (int(currentExperience) / learningCurve(Level + 1)) * 100
    return carryPercentage

def checkRollOver(Level, currentExperience):
    for i in range(Level + 1):
        currentExperience = int(currentExperience) - learningCurve(i)
    if currentExperience >= 0:
        return True
    else:
        return False
 


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("UserInterface.ui", self)

        self.ReadingButton.clicked.connect(self.readingButtonClick)
        self.MeditationButton.clicked.connect(self.meditationButtonClicked)
        self.GymButton.clicked.connect(self.gymButtonClicked)
        self.SocialButton.clicked.connect(self.socialButtonClicked)
        self.ProgButton.clicked.connect(self.progButtonClicked)
        self.ReadingButton4x.clicked.connect(self.extraReadingButtonClicked)
        self.MeditationButton4x.clicked.connect(self.extraMeditationButtonClicked)
        self.GymButton4x.clicked.connect(self.extraGymButtonClicked)
        self.SocialButton4x.clicked.connect(self.extraSocialButtonClicked)
        self.ProgButton4x.clicked.connect(self.extraProgButtonClicked)

        self.setReadingProgressBar()
        self.setMeditationProgressBar()
        self.setGymProgressBar()
        self.setSocialProgressBar()
        self.setProgProgressBar()


    def setReadingProgressBar(self):
        info = readingFile()
        tupleData = findLevelAndXp(info[0])
        self.ReadingLevel.setText("Level " + str(tupleData[0]))
        percentage = int((tupleData[1] / learningCurve(tupleData[0])) * 100)
        self.ReadingProgressBar.setValue(percentage)
        

    def setMeditationProgressBar(self):
        info = readingFile()
        tupleData = findLevelAndXp(info[1])
        self.MeditationLevel.setText("Level " + str(tupleData[0]))
        percentage = int((tupleData[1] / learningCurve(tupleData[0])) * 100)
        self.MeditationProgressBar.setValue(percentage)

    def setGymProgressBar(self):
        info = readingFile()
        tupleData = findLevelAndXp(info[2])
        self.GymLevel.setText("Level " + str(tupleData[0]))
        percentage = int((tupleData[1] / learningCurve(tupleData[0])) * 100)
        self.GymProgressBar.setValue(percentage)

    def setSocialProgressBar(self):
        info = readingFile()
        tupleData = findLevelAndXp(info[3])
        self.SocialLevel.setText("Level " + str(tupleData[0]))
        percentage = int((tupleData[1] / learningCurve(tupleData[0])) * 100)
        self.SocialProgressBar.setValue(percentage)

    def setProgProgressBar(self):
        info = readingFile()
        tupleData = findLevelAndXp(info[4])
        self.ProgLevel.setText("Level " + str(tupleData[0]))
        percentage = int((tupleData[1] / learningCurve(tupleData[0])) * 100)
        self.ProgProgressBar.setValue(percentage)
       

    def readingButtonClick(self):
        
        info = readingFile()
        info[0] = str(int(info[0]) + 100) + "\n"
        writingToFile(info)

        levelLabel = self.ReadingLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[0])
        
        if checkRollOver(level, info[0]) != True:
            percentage = int(normalise(level, xp))
            self.ReadingProgressBar.setValue(percentage)
        else:
            self.ReadingLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.ReadingProgressBar.setValue(int(rolledPercentage))
            

    def meditationButtonClicked(self):

        info = readingFile()
        info[1] = str(int(info[1]) + 100) + "\n"
        writingToFile(info)

        levelLabel = self.MeditationLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[1])

        if checkRollOver(level, info[1]) != True:
            percentage = int(normalise(level, xp))
            self.MeditationProgressBar.setValue(percentage)
        else:
            self.MeditationLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.MeditationProgressBar.setValue(int(rolledPercentage))
        

    def gymButtonClicked(self):

        info = readingFile()
        info[2] = str(int(info[2]) + 100) + "\n"
        writingToFile(info)

        levelLabel = self.GymLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[2])

        if checkRollOver(level, info[2]) != True:
            percentage = int(normalise(level, xp))
            self.GymProgressBar.setValue(percentage)
        else:
            self.GymLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.GymProgressBar.setValue(int(rolledPercentage))

    def socialButtonClicked(self):

        info = readingFile()
        info[3] = str(int(info[3]) + 100) + "\n"
        writingToFile(info)

        levelLabel = self.SocialLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[3])

        if checkRollOver(level, info[3]) != True:
            percentage = int(normalise(level, xp))
            self.SocialProgressBar.setValue(percentage)
        else:
            self.SocialLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.SocialProgressBar.setValue(int(rolledPercentage))

        
    def progButtonClicked(self):
        
        info = readingFile()
        info[4] = str(int(info[4]) + 100) + "\n"
        writingToFile(info)

        levelLabel = self.ProgLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[4])

        if checkRollOver(level, info[4]) != True:
            percentage = int(normalise(level, xp))
            self.ProgProgressBar.setValue(percentage)
        else:
            self.ProgLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.ProgProgressBar.setValue(int(rolledPercentage))
            

    def extraReadingButtonClicked(self):

        info = readingFile()
        info[0] = str(int(info[0]) + 700) + "\n"
        writingToFile(info)

        levelLabel = self.ReadingLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[0])
        
        if checkRollOver(level, info[0]) != True:
            percentage = int(normalise(level, xp))
            self.ReadingProgressBar.setValue(percentage)
        else:
            self.ReadingLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.ReadingProgressBar.setValue(int(rolledPercentage))

    def extraMeditationButtonClicked(self):
        info = readingFile()
        info[1] = str(int(info[1]) + 700) + "\n"
        writingToFile(info)

        levelLabel = self.MeditationLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[1])

        if checkRollOver(level, info[1]) != True:
            percentage = int(normalise(level, xp))
            self.MeditationProgressBar.setValue(percentage)
        else:
            self.MeditationLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.MeditationProgressBar.setValue(int(rolledPercentage))

    def extraGymButtonClicked(self):

        info = readingFile()
        info[2] = str(int(info[2]) + 700) + "\n"
        writingToFile(info)

        levelLabel = self.GymLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[2])

        if checkRollOver(level, info[2]) != True:
            percentage = int(normalise(level, xp))
            self.GymProgressBar.setValue(percentage)
        else:
            self.GymLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.GymProgressBar.setValue(int(rolledPercentage))


    def extraSocialButtonClicked(self):

        info = readingFile()
        info[3] = str(int(info[3]) + 700) + "\n"
        writingToFile(info)

        levelLabel = self.SocialLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[3])

        if checkRollOver(level, info[3]) != True:
            percentage = int(normalise(level, xp))
            self.SocialProgressBar.setValue(percentage)
        else:
            self.SocialLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.SocialProgressBar.setValue(int(rolledPercentage))


    def extraProgButtonClicked(self):

        info = readingFile()
        info[4] = str(int(info[4]) + 700) + "\n"
        writingToFile(info)

        levelLabel = self.ProgLevel.text()
        level = int(levelLabel[6])
        xp = currentXpRange(level, info[4])

        if checkRollOver(level, info[4]) != True:
            percentage = int(normalise(level, xp))
            self.ProgProgressBar.setValue(percentage)
        else:
            self.ProgLevel.setText("Level " + str(level + 1))
            rolledPercentage = rollOver(level, xp)
            self.ProgProgressBar.setValue(int(rolledPercentage))


def main():
    app = QApplication(sys.argv)
    mainWindow = Main()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedWidth(845)
    widget.setFixedHeight(461)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        pass

if __name__ == "__main__":
    main()
