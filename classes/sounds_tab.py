import os
import pygame
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox, QPushButton, QSlider, QSpinBox, QHBoxLayout

# Updated sound paths
from constants.sounds_options import (
    VORE_SOUNDS, RELEASE_SOUNDS,
    FANCY_VORE_SOUNDS, FANCY_RELEASE_SOUNDS,
    NOISE_FREQUENCY
)

class SoundsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pygame.mixer.init()  # Initialize pygame.mixer

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(2)  # Reduce spacing between widgets
        self.layout.setContentsMargins(2, 2, 2, 2)  # Reduce margins around the layout

        # Fleshy Belly
        self.fleshy_belly_layout = QHBoxLayout()
        self.fleshy_belly_checkbox = QCheckBox('Fleshy Belly')
        self.fleshy_belly_layout.addWidget(self.fleshy_belly_checkbox)
        self.layout.addLayout(self.fleshy_belly_layout)

        # Internal Loop
        self.internal_loop_layout = QHBoxLayout()
        self.internal_loop_checkbox = QCheckBox('Internal Loop')
        self.internal_loop_layout.addWidget(self.internal_loop_checkbox)
        self.layout.addLayout(self.internal_loop_layout)

        # Use Fancy Sounds
        self.fancy_sounds_layout = QHBoxLayout()
        self.fancy_sounds_checkbox = QCheckBox('Use Fancy Sounds')
        self.fancy_sounds_checkbox.stateChanged.connect(self.update_sound_options)
        self.fancy_sounds_layout.addWidget(self.fancy_sounds_checkbox)
        self.layout.addLayout(self.fancy_sounds_layout)

        # Vore Sound
        self.vore_sound_layout = QHBoxLayout()
        self.vore_sound_label = QLabel('Vore Sound:')
        self.vore_sound_combobox = QComboBox()
        self.vore_sound_button = QPushButton('🔊')
        self.vore_sound_button.setFixedWidth(30)
        self.vore_sound_button.setMaximumWidth(30)
        self.vore_sound_button.clicked.connect(lambda: self.play_sound(self.vore_sound_combobox))
        self.vore_sound_layout.addWidget(self.vore_sound_label)
        self.vore_sound_layout.addWidget(self.vore_sound_combobox)
        self.vore_sound_layout.addWidget(self.vore_sound_button)
        self.layout.addLayout(self.vore_sound_layout)

        # Release Sound
        self.release_sound_layout = QHBoxLayout()
        self.release_sound_label = QLabel('Release Sound:')
        self.release_sound_combobox = QComboBox()
        self.release_sound_button = QPushButton('🔊')
        self.release_sound_button.setFixedWidth(30)
        self.release_sound_button.setMaximumWidth(30)
        self.release_sound_button.clicked.connect(lambda: self.play_sound(self.release_sound_combobox))
        self.release_sound_layout.addWidget(self.release_sound_label)
        self.release_sound_layout.addWidget(self.release_sound_combobox)
        self.release_sound_layout.addWidget(self.release_sound_button)
        self.layout.addLayout(self.release_sound_layout)

        # Sound Volume
        self.sound_volume_layout = QHBoxLayout()
        self.sound_volume_label = QLabel('Sound Volume:')
        self.sound_volume_slider = QSlider(Qt.Horizontal)
        self.sound_volume_slider.setRange(0, 100)
        self.sound_volume_slider.setValue(100)
        self.sound_volume_slider.valueChanged.connect(self.sync_volume_spinbox)
        self.sound_volume_spinbox = QSpinBox()
        self.sound_volume_spinbox.setRange(0, 100)
        self.sound_volume_spinbox.valueChanged.connect(self.sync_volume_slider)
        self.sound_volume_layout.addWidget(self.sound_volume_label)
        self.sound_volume_layout.addWidget(self.sound_volume_slider)
        self.sound_volume_layout.addWidget(self.sound_volume_spinbox)
        self.layout.addLayout(self.sound_volume_layout)

        # Noise Frequency
        self.noise_frequency_layout = QHBoxLayout()
        self.noise_frequency_label = QLabel('Noise Frequency:')
        self.noise_frequency_combo = QComboBox()
        self.noise_frequency_combo.addItems(NOISE_FREQUENCY)
        self.noise_frequency_combo.currentIndexChanged.connect(self.noise_frequency_changed)
        self.noise_frequency_layout.addWidget(self.noise_frequency_label)
        self.noise_frequency_layout.addWidget(self.noise_frequency_combo)
        self.layout.addLayout(self.noise_frequency_layout)

        self.noise_frequency_spinbox = QSpinBox()
        self.noise_frequency_spinbox.setRange(15000, 70000)
        self.noise_frequency_spinbox.setValue(42500)
        self.noise_frequency_spinbox.setVisible(False)  # Initially hidden
        self.noise_frequency_layout.addWidget(self.noise_frequency_spinbox)
        
        self.setLayout(self.layout)

        # Initialize with classic sounds
        self.update_sound_options()

    def sync_volume_slider(self, value):
        self.sound_volume_slider.setValue(value)

    def sync_volume_spinbox(self, value):
        self.sound_volume_spinbox.setValue(value)

    def update_sound_options(self):
        if self.fancy_sounds_checkbox.isChecked():
            self.vore_sound_combobox.clear()
            self.vore_sound_combobox.addItems(FANCY_VORE_SOUNDS.keys())

            self.release_sound_combobox.clear()
            self.release_sound_combobox.addItems(FANCY_RELEASE_SOUNDS.keys())
        else:
            self.vore_sound_combobox.clear()
            self.vore_sound_combobox.addItems(VORE_SOUNDS.keys())

            self.release_sound_combobox.clear()
            self.release_sound_combobox.addItems(RELEASE_SOUNDS.keys())

    def play_sound(self, combobox):
        sound_name = combobox.currentText()
        if self.fancy_sounds_checkbox.isChecked():
            sound_dict = FANCY_VORE_SOUNDS if combobox == self.vore_sound_combobox else FANCY_RELEASE_SOUNDS
        else:
            sound_dict = VORE_SOUNDS if combobox == self.vore_sound_combobox else RELEASE_SOUNDS

        sound_file_name = sound_dict.get(sound_name)
        if sound_file_name:
            sound_path = os.path.abspath(os.path.join(os.getcwd(), sound_file_name))
            print("Attempting to load sound from:", sound_path)  # Print the resolved path
            
            try:
                pygame.mixer.music.load(sound_path)
                pygame.mixer.music.set_volume(self.sound_volume_slider.value() / 100.0)
                pygame.mixer.music.play()
            except pygame.error as e:
                print("Error playing sound:", e)
        else:
            print(f"Sound file not found for '{sound_name}'. Available keys in dictionary:", sound_dict.keys())

    def noise_frequency_changed(self, index):
        selected_frequency = self.noise_frequency_combo.currentText()
        if selected_frequency == "Custom":
            self.noise_frequency_spinbox.setVisible(True)
        else:
            self.noise_frequency_spinbox.setVisible(False)

    def set_belly_data(self, belly_data):
        self.fleshy_belly_checkbox.setChecked(belly_data.get('is_wet', False))
        self.internal_loop_checkbox.setChecked(belly_data.get('wet_loop', False))
        self.fancy_sounds_checkbox.setChecked(belly_data.get('fancy_vore', False))
        self.vore_sound_combobox.setCurrentText(belly_data.get('vore_sound', ''))
        self.release_sound_combobox.setCurrentText(belly_data.get('release_sound', ''))
        self.sound_volume_slider.setValue(belly_data.get('sound_volume', 100))
        self.sound_volume_spinbox.setValue(belly_data.get('sound_volume', 100))
        self.noise_frequency_combo.setCurrentText(belly_data.get('noise_frequency', ''))

        # Set visibility of custom noise frequency spinbox based on stored data
        if belly_data.get('noise_frequency') == "Custom":
            self.noise_frequency_spinbox.setValue(belly_data.get('noise_freq', 42500))
            self.noise_frequency_spinbox.setVisible(True)
        else:
            self.noise_frequency_spinbox.setVisible(False)

    def get_belly_data(self):
        belly_data = {
            'is_wet': self.fleshy_belly_checkbox.isChecked(),
            'wet_loop': self.internal_loop_checkbox.isChecked(),
            'fancy_vore': self.fancy_sounds_checkbox.isChecked(),
            'vore_sound': self.vore_sound_combobox.currentText(),
            'release_sound': self.release_sound_combobox.currentText(),
            'sound_volume': self.sound_volume_slider.value(),
            'noise_frequency': self.noise_frequency_combo.currentText()
        }

        # Store custom noise frequency value if currently visible
        if self.noise_frequency_spinbox.isVisible():
            belly_data['noise_freq'] = self.noise_frequency_spinbox.value()

        return belly_data
