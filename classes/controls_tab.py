from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QCheckBox, QGroupBox
)

from constants.controls_options import MODE_ADDONS_OPTIONS, MODE_OPTIONS, ITEM_MODE_OPTIONS

class ControlsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        # Name
        self.name_label = QLabel('Name:')
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        # Mode
        self.mode_label = QLabel('Mode:')
        self.layout.addWidget(self.mode_label)

        self.mode_combobox = QComboBox()
        self.mode_combobox.addItems(MODE_OPTIONS)
        self.layout.addWidget(self.mode_combobox)

        # Item Mode
        self.item_mode_label = QLabel('Item Mode:')
        self.layout.addWidget(self.item_mode_label)

        self.item_mode_combobox = QComboBox()
        self.item_mode_combobox.addItems(ITEM_MODE_OPTIONS)
        self.layout.addWidget(self.item_mode_combobox)

        # Mode Addons
        self.mode_addons_groupbox = QGroupBox('Mode Addons')
        self.mode_addons_layout = QVBoxLayout()

        # Checkboxes for addons
        self.addon_checkboxes = []
        for addon in MODE_ADDONS_OPTIONS:
            checkbox = QCheckBox(addon)
            self.mode_addons_layout.addWidget(checkbox)
            self.addon_checkboxes.append(checkbox)

        self.mode_addons_groupbox.setLayout(self.mode_addons_layout)
        self.layout.addWidget(self.mode_addons_groupbox)

        self.setLayout(self.layout)

    def set_belly_data(self, belly_data):
        self.name_input.setText(belly_data.get('name', ''))
        self.mode_combobox.setCurrentText(belly_data.get('mode', ''))
        self.item_mode_combobox.setCurrentText(belly_data.get('item_mode', ''))
        self.load_addons(belly_data.get('addons', []))

    def get_belly_data(self):
        belly_data = {
            'name': self.name_input.text(),
            'mode': self.mode_combobox.currentText(),
            'item_mode': self.item_mode_combobox.currentText(),
            'addons': self.get_addons()
        }
        return belly_data

    def clear_fields(self):
        self.name_input.clear()
        self.mode_combobox.setCurrentIndex(0)
        self.item_mode_combobox.setCurrentIndex(0)
        self.uncheck_all_addons()

    def load_addons(self, addons):
        self.uncheck_all_addons()
        for addon_checkbox in self.addon_checkboxes:
            if addon_checkbox.text() in addons:
                addon_checkbox.setChecked(True)

    def get_addons(self):
        addons = []
        for checkbox in self.addon_checkboxes:
            if checkbox.isChecked():
                addons.append(checkbox.text())
        return addons

    def uncheck_all_addons(self):
        for checkbox in self.addon_checkboxes:
            checkbox.setChecked(False)
