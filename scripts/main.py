import sys
import json
import os
import copy
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFileDialog, QMessageBox, QLabel, QListWidget,
    QListWidgetItem, QTabWidget, QGroupBox, QTextEdit, QMainWindow, QAction, qApp, QInputDialog
)
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from classes.controls_tab import ControlsTab
from classes.descriptions_tab import DescriptionsTab
from classes.options_tab import OptionsTab
from classes.sounds_tab import SoundsTab
from classes.visuals_tab import VisualsTab
from classes.interactions_tab import InteractionsTab
from classes.liquids_tab import LiquidsTab

def load_default_belly(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
default_belly_path = 'default/belly.json'

class VRDBEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.belly_data_buffer = []
        self.current_file_data = None
        self.current_file_path = None

    def initUI(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle('External Belly Editor')
        
        self.create_menu()
        self.create_layout()

    def create_menu(self):
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu('&File')
        
        new_file = QAction('&New File', self)
        new_file.setShortcut('Ctrl+N')
        new_file.setStatusTip('Create a new set of bellies')
        new_file.triggered.connect(self.create_new_file)
        file_menu.addAction(new_file)
        
        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open Bellies')
        open_action.triggered.connect(self.load_vrdb)
        file_menu.addAction(open_action)

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save Bellies')
        save_action.triggered.connect(self.save_vrdb)
        file_menu.addAction(save_action)

        save_as_action = QAction('Save &As...', self)
        save_as_action.setShortcut('Ctrl+Shift+S')
        save_as_action.setStatusTip('Save Bellies As...')
        save_as_action.triggered.connect(self.save_as_vrdb)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)
        
        # Help menu
        help_menu = menubar.addMenu('&Help')
        github_action = QAction('&GitHub', self)
        github_action.setStatusTip('Visit GitHub Repository')
        github_action.triggered.connect(self.open_github_repo)
        help_menu.addAction(github_action)

    def create_layout(self):
        self.layout = QVBoxLayout()

        # Create a title label (hidden initially)
        self.title_label = QLabel('File Title', self)
        self.title_label.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.title_label.setVisible(False)
        self.layout.addWidget(self.title_label)

        # Create a horizontal layout for the belly list and tabs
        self.horizontal_layout = QHBoxLayout()

        # Left side: Belly List
        self.left_group_box = QGroupBox('Belly List', self)
        self.left_group_box.setMaximumWidth(250)
        self.left_layout = QVBoxLayout(self.left_group_box)
        
        self.minWidth = 150
        self.maxWidth = 250

        self.belly_list = QListWidget()
        self.belly_list.setMinimumWidth(self.minWidth)
        self.belly_list.setMaximumWidth(self.maxWidth)
        self.belly_list.itemSelectionChanged.connect(self.on_belly_selected)
        self.left_layout.addWidget(self.belly_list)

        self.load_button = QPushButton('Load Bellies', self)
        self.load_button.setMinimumWidth(self.minWidth)
        self.load_button.setMaximumWidth(self.maxWidth)
        self.load_button.clicked.connect(self.load_vrdb)
        self.left_layout.addWidget(self.load_button)

        self.save_button = QPushButton('Save Bellies', self)
        self.save_button.setMinimumWidth(self.minWidth)
        self.save_button.setMaximumWidth(self.maxWidth)
        self.save_button.clicked.connect(self.save_vrdb)
        self.save_button.setEnabled(False)  # Initially disabled
        self.left_layout.addWidget(self.save_button)
        
        self.new_belly_button = QPushButton('Create Belly', self)
        self.new_belly_button.setMinimumWidth(self.minWidth)
        self.new_belly_button.setMaximumWidth(self.maxWidth)
        self.new_belly_button.clicked.connect(self.create_new_belly)
        self.new_belly_button.setEnabled(False)    # Initially disabled
        self.left_layout.addWidget(self.new_belly_button)
        
        self.delete_belly_button = QPushButton('Delete Belly', self)
        self.delete_belly_button.setMinimumWidth(self.minWidth)
        self.delete_belly_button.setMaximumWidth(self.maxWidth)
        self.delete_belly_button.clicked.connect(self.confirm_delete_belly)
        self.delete_belly_button.setEnabled(False)  # Initially disabled
        self.left_layout.addWidget(self.delete_belly_button)

        self.horizontal_layout.addWidget(self.left_group_box)

        # Right side: Tab Widget
        self.right_tab_widget = QTabWidget()
        self.right_tab_widget.setMinimumWidth(800)

        # JSON tab
        self.json_tab = QWidget()
        self.json_layout = QVBoxLayout(self.json_tab)
        self.json_scroll_area = QTextEdit()
        self.json_scroll_area.setReadOnly(True)
        self.json_layout.addWidget(self.json_scroll_area)
        self.right_tab_widget.addTab(self.json_tab, 'JSON')

        # Controls tab
        self.controls_tab = ControlsTab()
        self.right_tab_widget.addTab(self.controls_tab, 'Controls')

        # Descriptions tab
        self.descriptions_tab = DescriptionsTab()
        self.right_tab_widget.addTab(self.descriptions_tab, 'Descriptions')
        
        # Options tab
        self.options_tab = OptionsTab()
        self.right_tab_widget.addTab(self.options_tab, 'Options')

        # Sounds tab
        self.sounds_tab = SoundsTab()
        self.right_tab_widget.addTab(self.sounds_tab, 'Sounds')

        # Visuals tab
        self.visuals_tab = VisualsTab()
        self.right_tab_widget.addTab(self.visuals_tab, 'Visuals')

        # Interactions tab
        self.interactions_tab = InteractionsTab()
        self.right_tab_widget.addTab(self.interactions_tab, 'Interactions')

        # Liquids tab
        self.liquids_tab = LiquidsTab()
        self.right_tab_widget.addTab(self.liquids_tab, 'Liquids')

        self.horizontal_layout.addWidget(self.right_tab_widget)
        self.layout.addLayout(self.horizontal_layout)

        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
        
        self.enable_tabs(False)
        
    def enable_tabs(self, enabled):
        for index in range(self.right_tab_widget.count()):
            self.right_tab_widget.setTabEnabled(index, enabled)
            
    def create_new_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("VRDB files (*.vrdb)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getSaveFileName(self, "Create New VRDB File", "", "VRDB files (*.vrdb)")
        
        if file_path:
            try:
                default_belly = load_default_belly(default_belly_path)
                self.belly_data_buffer = [default_belly]
                self.current_file_data = self.belly_data_buffer.copy()
                self.current_file_path = file_path
                
                self.title_label.setText(os.path.basename(file_path))
                self.title_label.setVisible(True)
                self.display_bellies(self.belly_data_buffer)
                self.belly_list.setCurrentRow(0)
                self.enable_tabs(True)
                self.new_belly_button.setEnabled(True)
                self.save_button.setEnabled(True)
                self.delete_belly_button.setEnabled(True)
                self.right_tab_widget.setCurrentIndex(1)
                
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to create new VRDB file:\n{str(e)}')

    def load_vrdb(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("VRDB files (*.vrdb)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getOpenFileName(self, "Open VRDB File", "", "VRDB files (*.vrdb)")

        if file_path:
            try:
                # Set the title label text
                title = os.path.basename(file_path)
                title = title.split('_')[0]
                self.title_label.setText(title)
                self.title_label.setVisible(True)

                with open(file_path, 'r', encoding='utf-8') as f:
                    self.current_file_path = file_path
                    self.current_file_data = json.load(f)
                    self.belly_data_buffer = copy.deepcopy(self.current_file_data)
                    self.display_bellies(self.belly_data_buffer)
                    self.enable_tabs(True)
                    self.new_belly_button.setEnabled(True)
                    self.save_button.setEnabled(True)
                    self.delete_belly_button.setEnabled(True)
                    self.right_tab_widget.setCurrentIndex(1)
                    
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to load VRDB file:\n{str(e)}')

    def save_vrdb(self):
        if self.current_file_path:
            try:
                with open(self.current_file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.belly_data_buffer, f, ensure_ascii=False, indent=4)
                    QMessageBox.information(self, 'Saved', 'Bellies saved successfully.')
                    
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to save VRDB file:\n{str(e)}')
        
        else:
            QMessageBox.warning(self, 'Warning', 'No file opened yet. Please create or open a file first.')

    def save_as_vrdb(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("VRDB files (*.vrdb)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_path, _ = file_dialog.getSaveFileName(self, "Save VRDB File As", "", "VRDB files (*.vrdb)")

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.belly_data_buffer, f, ensure_ascii=False, indent=4)
                    self.current_file_path = file_path
                    self.title_label.setText(os.path.basename(file_path))
                    QMessageBox.information(self, 'Saved As', 'Bellies saved successfully.')
                    
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to save VRDB file:\n{str(e)}')

    def create_new_belly(self):
        belly_name, ok = QInputDialog.getText(self, 'Create Belly', 'Enter Belly Name:')
        if ok and belly_name:
            new_belly = {
                'name': belly_name,
                'controls': {},
                'descriptions': [],
                'options': [],
                'sounds': [],
                'visuals': [],
                'interactions': [],
                'liquids': []
            }
            self.belly_data_buffer.append(new_belly)
            self.display_bellies(self.belly_data_buffer)

    def confirm_delete_belly(self):
        current_row = self.belly_list.currentRow()
        if current_row >= 0:
            reply = QMessageBox.question(self, 'Confirm Delete',
                                         'Are you sure you want to delete this belly?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                del self.belly_data_buffer[current_row]
                self.display_bellies(self.belly_data_buffer)

    def display_bellies(self, bellies):
        self.belly_list.clear()
        for belly in bellies:
            self.belly_list.addItem(belly['name'])

    def on_belly_selected(self):
        current_row = self.belly_list.currentRow()
        if current_row >= 0 and current_row < len(self.belly_data_buffer):
            belly_data = self.belly_data_buffer[current_row]
            self.json_scroll_area.setPlainText(json.dumps(belly_data, indent=4))
        else:
            self.json_scroll_area.setPlainText("")  # Clear the JSON area if no belly is selected

    def toggle_developer_mode(self, checked):
        # Placeholder implementation for toggling developer mode
        if checked:
            QMessageBox.information(self, 'Developer Mode', 'Developer Mode Enabled')
        else:
            QMessageBox.information(self, 'Developer Mode', 'Developer Mode Disabled')

    def open_github_repo(self):
        url = "https://github.com/example/repository"
        QDesktopServices.openUrl(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = VRDBEditor()
    editor.show()
    sys.exit(app.exec_())
