# main.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen

class Circle:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circles")
        self.setGeometry(100, 100, 400, 300)
        self.button = self.create_button("Create", 150, 250, 100, 30)
        self.circles = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

    def create_button(self, text, x, y, w, h):
        button = self.button = self.button = self.button
        button.setGeometry(x, y, w, h)
        button.setText(text)
        button.clicked.connect(self.create_circles)
        return button

    def create_circles(self):
        r = 50 + int(self.width() / 20)
        color = QColor(int(255 * random.random()), int(255 * random.random()), int(255 * random.random()))
        self.circles.append(Circle(self.width() / 2, self.height() / 2, r, color))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for circle in self.circles:
            painter.setPen(QPen(circle.color, 2))
            painter.drawEllipse(circle.x - circle.r, circle.y - circle.r, 2 * circle.r, 2 * circle.r)

    def update(self):
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
