import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QColorDialog
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QImage

def load_images_and_overlays(base_path):
    images = {}
    for file_name in os.listdir(base_path):
        if file_name.endswith(".png") and "-" not in file_name:
            base_name = file_name.split(".png")[0]
            overlay_files = sorted(
                [f for f in os.listdir(base_path) if f.startswith(base_name + "-") and f.endswith(".png")],
                key=lambda x: int(x.split('-')[1].split('.')[0])
            )
            images[base_name] = (os.path.join(base_path, file_name), [os.path.join(base_path, f) for f in overlay_files])
    return images

def apply_color_overlay(image, color):
    image = image.convertToFormat(QImage.Format_ARGB32)

    for y in range(image.height()):
        for x in range(image.width()):
            pixel = image.pixel(x, y)
            alpha = QColor(pixel).alpha()
            if alpha > 0:
                image.setPixelColor(x, y, QColor(color.red(), color.green(), color.blue(), alpha))

    return image

def combine_overlays(base_image_path, overlay_paths, colors):
    base_image = QImage(base_image_path)
    combined_image = QImage(base_image.size(), QImage.Format_ARGB32)
    combined_image.fill(Qt.transparent)

    painter = QPainter(combined_image)
    painter.drawImage(0, 0, base_image)

    for overlay_path, color in zip(overlay_paths, colors):
        overlay_image = QImage(overlay_path)
        colored_overlay = apply_color_overlay(overlay_image, color)
        painter.drawImage(0, 0, colored_overlay)

    painter.end()
    return QPixmap.fromImage(combined_image)

class BellyFullscreenStyles(QWidget):
    def __init__(self, base_path):
        super().__init__()
        self.base_path = base_path
        self.images = load_images_and_overlays(self.base_path)
        self.color_overlays = {style: [QColor() for _ in range(len(overlays[1]))] for style, overlays in self.images.items()}
        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.grid_layout = QVBoxLayout()
        self.main_layout.addLayout(self.grid_layout)
        self.color_frames = []
        self.load_styles()

    def load_styles(self):
        for style, (base_image_path, overlay_paths) in self.images.items():
            base_image = QLabel()
            base_pixmap = QPixmap(base_image_path)
            base_image.setPixmap(base_pixmap.scaledToWidth(200))
            self.grid_layout.addWidget(base_image)

            color_frame_layout = QHBoxLayout()
            for index in range(len(overlay_paths)):
                color_frame = QFrame()
                color_frame.setFixedSize(30, 30)
                self.color_frames.append(color_frame)
                color_frame_layout.addWidget(color_frame)
                color_frame.setStyleSheet("background-color: black;")
                color_frame.mousePressEvent = lambda event, cf=color_frame: self.choose_color_for_frame(cf)
            self.grid_layout.addLayout(color_frame_layout)

    def choose_color_for_frame(self, color_frame):
        color = QColorDialog.getColor()
        if color.isValid():
            color_frame.setStyleSheet(f"background-color: {color.name()};")
            self.update_color_overlays()
            self.update_images()

    def update_color_overlays(self):
        for style, overlays in self.images.items():
            for index in range(len(overlays[1])):
                color_frame_index = list(self.images.keys()).index(style) * len(overlays[1]) + index
                color = self.color_frames[color_frame_index].palette().color(QPalette.Background)
                self.color_overlays[style][index] = color

    def update_images(self):
        for style, (base_image_path, overlay_paths) in self.images.items():
            colors = self.color_overlays[style]
            combined_pixmap = combine_overlays(base_image_path, overlay_paths, colors)

def integrate_belly_fullscreen_styles(base_path, layout):
    belly_styles = BellyFullscreenStyles(base_path)
    layout.addWidget(belly_styles)
