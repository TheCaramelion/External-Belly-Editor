import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QCheckBox,
    QGroupBox, QGridLayout, QListWidget, QListWidgetItem,
    QDoubleSpinBox, QComboBox, QFrame, QPushButton, QColorDialog
)
from PyQt5.QtGui import QColor

from constants.visuals_tab import BELLY_REGION_AFFECT, UNDERGARMENT_AFFECT, UNDERGARMENT_NONE

class VisualsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Checkbox to toggle visibility of vore sprites settings
        self.affect_vore_sprites_checkbox = QCheckBox('Affect Vore Sprites')
        self.layout.addWidget(self.affect_vore_sprites_checkbox)

        # Main group box for Vore Sprites
        self.vore_sprites_groupbox = QGroupBox('Vore Sprites')
        self.vore_sprites_layout = QGridLayout(self.vore_sprites_groupbox)

        # ListWidget for Vore Sprite Modes
        self.vore_sprite_mode_label = QLabel('Vore Sprite Modes:')
        self.vore_sprite_mode_listwidget = QListWidget()
        self.vore_sprite_mode_listwidget.setSelectionMode(QListWidget.MultiSelection)
        modes = ['Normal belly sprite', 'Undergarment addition']
        for mode in modes:
            item = QListWidgetItem(mode)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.vore_sprite_mode_listwidget.addItem(item)

        self.vore_sprites_layout.addWidget(self.vore_sprite_mode_label, 0, 0)
        self.vore_sprites_layout.addWidget(self.vore_sprite_mode_listwidget, 0, 1)

        # Group box for Count Absorbed Prey and Absorbed Multiplier
        self.groupbox_absorbed_prey = QGroupBox('Absorbed Prey')
        self.layout_absorbed_prey = QGridLayout(self.groupbox_absorbed_prey)

        self.count_absorbed_prey_label = QLabel('Count absorbed prey for vore sprites:')
        self.count_absorbed_prey_checkbox = QCheckBox()
        self.layout_absorbed_prey.addWidget(self.count_absorbed_prey_label, 0, 0)
        self.layout_absorbed_prey.addWidget(self.count_absorbed_prey_checkbox, 0, 1)

        self.absorbed_multiplier_label = QLabel('Absorbed Multiplier:')
        self.absorbed_multiplier_spinbox = QDoubleSpinBox()
        self.absorbed_multiplier_spinbox.setRange(0.1, 3)
        self.absorbed_multiplier_spinbox.setSingleStep(0.1)
        self.layout_absorbed_prey.addWidget(self.absorbed_multiplier_label, 1, 0)
        self.layout_absorbed_prey.addWidget(self.absorbed_multiplier_spinbox, 1, 1)

        self.vore_sprites_layout.addWidget(self.groupbox_absorbed_prey, 1, 0)

        # Group box for Count Liquids and Liquid Multiplier
        self.groupbox_liquid_reagents = QGroupBox('Count Liquids')
        self.layout_liquid_reagents = QGridLayout(self.groupbox_liquid_reagents)

        self.count_liquid_reagents_label = QLabel('Count liquids for vore sprites:')
        self.count_liquid_reagents_checkbox = QCheckBox()
        self.layout_liquid_reagents.addWidget(self.count_liquid_reagents_label, 0, 0)
        self.layout_liquid_reagents.addWidget(self.count_liquid_reagents_checkbox, 0, 1)

        self.liquid_multiplier_label = QLabel('Liquid Multiplier:')
        self.liquid_multiplier_spinbox = QDoubleSpinBox()
        self.liquid_multiplier_spinbox.setRange(0.1, 10)
        self.liquid_multiplier_spinbox.setSingleStep(0.1)
        self.layout_liquid_reagents.addWidget(self.liquid_multiplier_label, 1, 0)
        self.layout_liquid_reagents.addWidget(self.liquid_multiplier_spinbox, 1, 1)

        self.vore_sprites_layout.addWidget(self.groupbox_liquid_reagents, 1, 1)

        # Group box for Count Items and Items Multiplier
        self.groupbox_count_items = QGroupBox('Count Items')
        self.layout_count_items = QGridLayout(self.groupbox_count_items)

        self.count_items_label = QLabel('Count items for vore sprites:')
        self.count_items_checkbox = QCheckBox()
        self.layout_count_items.addWidget(self.count_items_label, 0, 0)
        self.layout_count_items.addWidget(self.count_items_checkbox, 0, 1)

        self.items_multiplier_label = QLabel('Items Multiplier:')
        self.items_multiplier_spinbox = QDoubleSpinBox()
        self.items_multiplier_spinbox.setRange(0.1, 10)
        self.items_multiplier_spinbox.setSingleStep(0.1)
        self.layout_count_items.addWidget(self.items_multiplier_label, 1, 0)
        self.layout_count_items.addWidget(self.items_multiplier_spinbox, 1, 1)

        self.vore_sprites_layout.addWidget(self.groupbox_count_items, 2, 0)

        # Group box for Prey Health, Animation When Resist, and Vore Sprite Size Factor
        self.groupbox_prey_health = QGroupBox('Prey Related')
        self.layout_prey_health = QGridLayout(self.groupbox_prey_health)

        self.prey_health_label = QLabel('Prey health affects vore sprites:')
        self.prey_health_checkbox = QCheckBox()
        self.layout_prey_health.addWidget(self.prey_health_label, 0, 0)
        self.layout_prey_health.addWidget(self.prey_health_checkbox, 0, 1)

        self.animation_when_resist_label = QLabel('Animation when prey resist:')
        self.animation_when_resist_checkbox = QCheckBox()
        self.layout_prey_health.addWidget(self.animation_when_resist_label, 1, 0)
        self.layout_prey_health.addWidget(self.animation_when_resist_checkbox, 1, 1)

        self.vore_sprite_size_factor_label = QLabel('Vore Sprite Size Factor:')
        self.vore_sprite_size_factor_spinbox = QDoubleSpinBox()
        self.vore_sprite_size_factor_spinbox.setRange(0.1, 3)
        self.vore_sprite_size_factor_spinbox.setSingleStep(0.1)
        self.layout_prey_health.addWidget(self.vore_sprite_size_factor_label, 2, 0)
        self.layout_prey_health.addWidget(self.vore_sprite_size_factor_spinbox, 2, 1)

        self.vore_sprites_layout.addWidget(self.groupbox_prey_health, 2, 1)

        # Group box for Belly Sprite
        self.groupbox_belly_sprite = QGroupBox('Affecting sprites')
        self.layout_belly_sprite = QGridLayout(self.groupbox_belly_sprite)

        self.belly_sprite_size_factor_label = QLabel('Belly Sprite Size Factor:')
        self.belly_sprite_size_factor_spinbox = QDoubleSpinBox()
        self.belly_sprite_size_factor_spinbox.setRange(0.1, 3)
        self.belly_sprite_size_factor_spinbox.setSingleStep(0.1)
        self.layout_belly_sprite.addWidget(self.belly_sprite_size_factor_label, 0, 0)
        self.layout_belly_sprite.addWidget(self.belly_sprite_size_factor_spinbox, 0, 1)

        self.belly_sprite_affect_label = QLabel('Belly Sprite to affect:')
        self.belly_sprite_affect_combobox = QComboBox()
        self.belly_sprite_affect_combobox.addItems(BELLY_REGION_AFFECT)
        self.layout_belly_sprite.addWidget(self.belly_sprite_affect_label, 1, 0)
        self.layout_belly_sprite.addWidget(self.belly_sprite_affect_combobox, 1, 1)

        self.belly_sprite_undergarment_type_label = QLabel('Undergarment type to affect:')
        self.belly_sprite_undergarment_type_combobox = QComboBox()
        self.belly_sprite_undergarment_type_combobox.addItems(UNDERGARMENT_AFFECT)
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_type_label, 2, 0)
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_type_combobox, 2, 1)

        self.belly_sprite_undergarment_none_label = QLabel('Undergarment type if none equipped:')
        self.belly_sprite_undergarment_none_combobox = QComboBox()
        self.belly_sprite_undergarment_none_combobox.addItems(UNDERGARMENT_NONE)
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_none_label, 3, 0)
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_none_combobox, 3, 1)

        self.belly_sprite_undergarment_colour_button = QPushButton('Choose colour')
        self.belly_sprite_undergarment_colour_button.clicked.connect(self.choose_color)
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_colour_button, 4, 0, 1, 2)

        # Add the frame to display the chosen color
        self.belly_sprite_undergarment_color_frame = QFrame()
        self.belly_sprite_undergarment_color_frame.setFixedSize(30, 30)
        self.belly_sprite_undergarment_color_frame.setStyleSheet("background-color: black;")
        self.layout_belly_sprite.addWidget(self.belly_sprite_undergarment_color_frame, 4, 2)

        self.vore_sprites_layout.addWidget(self.groupbox_belly_sprite, 3, 0, 1, 2) 

        # Add main vore sprites group box to main layout
        self.layout.addWidget(self.vore_sprites_groupbox)

        # Connect checkbox to show/hide vore sprites settings
        self.affect_vore_sprites_checkbox.stateChanged.connect(self.toggle_vore_sprites_settings)

        # Initially hide vore sprites settings
        self.toggle_vore_sprites_settings(Qt.Unchecked)

        self.setLayout(self.layout)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            hex_color = color.name()
            self.set_color('belly_undergarment_color', hex_color)
            return hex_color
        return None

    def set_color(self, frame_id, hex_color):
        if frame_id == 'belly_undergarment_color':
            self.belly_sprite_undergarment_color_frame.setStyleSheet(f"background-color: {hex_color};")

    def toggle_vore_sprites_settings(self, state):
        visible = state == Qt.Checked
        self.vore_sprites_groupbox.setVisible(visible)

    def set_belly_data(self, belly_data):
        self.affect_vore_sprites_checkbox.setChecked(belly_data.get('affects_vore_sprites', ''))

        modes = belly_data.get('vore_sprite_flags', [])
        for index in range(self.vore_sprite_mode_listwidget.count()):
            item = self.vore_sprite_mode_listwidget.item(index)
            item.setCheckState(Qt.Checked if item.text() in modes else Qt.Unchecked)

        self.count_absorbed_prey_checkbox.setChecked(belly_data.get('count_absorbed_prey_for_sprite', ''))
        self.absorbed_multiplier_spinbox.setValue(belly_data.get('absorbed_multiplier', ''))
        self.count_liquid_reagents_checkbox.setChecked(belly_data.get('count_liquid_for_sprite', ''))
        self.liquid_multiplier_spinbox.setValue(belly_data.get('liquid_multiplier', ''))
        self.count_items_checkbox.setChecked(belly_data.get('count_items_for_sprite', ''))
        self.items_multiplier_spinbox.setValue(belly_data.get('items_multiplier', 1.0))
        self.prey_health_checkbox.setChecked(belly_data.get('health_impacts_size', ''))
        self.animation_when_resist_checkbox.setChecked(belly_data.get('resist_triggers_animation', ''))
        self.vore_sprite_size_factor_spinbox.setValue(belly_data.get('size_factor_for_sprite', ''))
        self.belly_sprite_affect_combobox.setCurrentText(belly_data.get('belly_sprite_to_affect'))
        self.belly_sprite_undergarment_type_combobox.setCurrentText(belly_data.get('undergarment_chosen'))
        self.belly_sprite_undergarment_none_combobox.setCurrentText(belly_data.get('undergarment_if_none'))
        

    def get_belly_data(self):
        modes = []
        for index in range(self.vore_sprite_mode_listwidget.count()):
            item = self.vore_sprite_mode_listwidget.item(index)
            if item.checkState() == Qt.Checked:
                modes.append(item.text())

        belly_data = {
            'affects_vore_sprites': self.affect_vore_sprites_checkbox.isChecked(),
            'vore_sprite_flags': modes,
            'count_absorbed_prey_for_sprite': self.count_absorbed_prey_checkbox.isChecked(),
            'absorbed_multiplier': self.absorbed_multiplier_spinbox.value(),
            'count_liquid_for_sprite': self.count_liquid_reagents_checkbox.isChecked(),
            'liquid_multiplier': self.liquid_multiplier_spinbox.value(),
            'count_items_for_sprite': self.count_items_checkbox.isChecked(),
            'items_multiplier': self.items_multiplier_spinbox.value(),
            'health_impacts_size': self.prey_health_checkbox.isChecked(),
            'resist_triggers_animation': self.animation_when_resist_checkbox.isChecked(),
            'size_factor_for_sprite': self.vore_sprite_size_factor_spinbox.value(),
            'belly_sprite_to_affect': self.belly_sprite_affect_combobox.currentText(),
            'undergarment_chosen': self.belly_sprite_undergarment_type_combobox.currentText(),
            'undergarment_if_none': self.belly_sprite_undergarment_none_combobox.currentText()
        }
        return belly_data