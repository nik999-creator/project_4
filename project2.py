from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import*
from PyQt5 import QtGui

notes = {
    "Ukraine": {
        "текст": "Українська дівчина",
        "image": "UkraineGirl.jpg"
    },
    "Japan": {
        "текст": "Японська дівчина",
        "image": "JapanGirl.jpg"
    },
    "Italy": {
        "текст": "Итальянська дівчина",
        "image": "ItalyGirl.jpg"
    },
    "China": {
        "текст": "Китайськая дівчина",
        "image": "ChinaGirl.jpg"
    },
    "German": {
        "текст": "Німецка дівчина",
        "image": "GermanGirl.jpg"
    },
    "Grek": {
        "текст": "Дівчина з Греції",
        "image": "GrekGirl.jpg"
    },
    "India": {
        "текст": "Індійська дівчина",
        "image": "IndiaGirl.jpg"
    },
    "Norvegia": {
        "текст": "Дівчина з Норвегії",
        "image": "NorvegiaGirl.jpg"
    },
}

#сторюємо вікно
app = QApplication([])

win = QWidget()
win.setWindowTitle("Жінки різних країн")
win.resize(900, 600)

#створюємо віджет для текста
text_label = QLabel("")
text_label.setWordWrap(True)

#віджет зображення
image_label = QLabel("")
image_label.setFixedSize(300, 300)

list_country = QListWidget()
list_country.addItems(notes.keys())

def show_note():
    key = list_country.selectedItems()[0].text()
    note = notes[key]
    
    text_label.setText(note["текст"])
    
    pixmap = QPixmap(note["image"])
    pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio)
    image_label.setPixmap(pixmap)

list_country.itemClicked.connect(show_note)

#колонки
layout = QHBoxLayout()

left_col = QVBoxLayout()
left_col.addWidget(QLabel("Список країн:"))
left_col.addWidget(list_country)

right_col = QVBoxLayout()
right_col.addWidget(image_label)
right_col.addWidget(text_label)

layout.addLayout(left_col, stretch=1)
layout.addLayout(right_col, stretch=2)

win.setLayout(layout)

win.show()
app.exec()