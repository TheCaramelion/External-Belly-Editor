from PyQt5.QtWidgets import(
    QWidget, QLabel, QGroupBox, QGridLayout, QLineEdit,
    QDoubleSpinBox, QCheckBox, QComboBox
)
from constants.options_options import (
    CONTAMINATION_FLAVORS, EGG_OPTIONS, CONTAMINATION_COLOURS,
    DRAIN_FINISHING_OPTIONS, VORE_PRIVACY_OPTIONS)
from scripts.math import math

class OptionsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.layout = QGridLayout(self)
        
        self.field_width = 200
        
        self.can_taste_switch = QCheckBox('Can Taste')
        self.layout.addWidget(self.can_taste_switch, 0, 0, 1, 1)
        
        self.entrance_logs_switch = QCheckBox('Entrance Logs')
        self.layout.addWidget(self.entrance_logs_switch, 0, 1, 1, 1)
        
        self.is_feedable_switch = QCheckBox('Feedable')
        self.layout.addWidget(self.is_feedable_switch, 1, 0, 1, 1)
        
        self.item_digestion_logs_switch = QCheckBox('Item Digestion Logs')
        self.layout.addWidget(self.item_digestion_logs_switch, 1, 1, 1, 1)
        
        self.display_absorbed_switch = QCheckBox('Display Absorbed Examines')
        self.layout.addWidget(self.display_absorbed_switch, 2, 0, 1, 1)
        
        self.vore_spawn_blacklist_switch = QCheckBox('Vore Spawn Blacklist')
        self.layout.addWidget(self.vore_spawn_blacklist_switch, 2, 1, 1, 1)
        
        self.recycling_switch = QCheckBox('Recycling')
        self.layout.addWidget(self.recycling_switch, 3, 0, 1, 1)
        
        self.storing_nutrition_switch = QCheckBox('Storing Nutrition')
        self.layout.addWidget(self.storing_nutrition_switch, 3, 1, 1, 1)
        
        self.emote_groupbox = QGroupBox('Idle Emotes')
        self.emote_layout = QGridLayout(self.emote_groupbox)
        
        self.emote_switch = QCheckBox('Activate', self)
        self.emote_switch.toggled.connect(self.toggle_emote)
        self.emote_layout.addWidget(self.emote_switch, 0, 0, 1, 1)
        
        # Delay Label
        self.delay_label = QLabel('Delay:')
        self.emote_layout.addWidget(self.delay_label, 0, 1, 1, 1)
        
        # Delay
        self.emote_delay_input = QDoubleSpinBox()
        self.emote_delay_input.setDecimals(0)
        self.emote_delay_input.setRange(1, 999)
        self.emote_delay_input.setMaximumWidth(self.field_width)
        self.emote_layout.addWidget(self.emote_delay_input, 1, 1, 1, 1)
        
        self.layout.addWidget(self.emote_groupbox, 5, 0, 1, 1)
        
        self.digestion_groupbox = QGroupBox('Digestion Damage')
        self.digestion_layout = QGridLayout(self.digestion_groupbox)
        
        self.precision = 2
        self.step_value = 0.1
        self.min_damage = 0.0
        self.max_damage = 6.0
        self.max_oxy_damage = 16.0
        
        # Brute Label
        self.brute_label = QLabel('Brute:')
        self.digestion_layout.addWidget(self.brute_label, 0, 0, 1, 1)
        
        # Burn Label
        self.burn_label = QLabel('Burn:')
        self.digestion_layout.addWidget(self.burn_label, 0, 1, 1, 1)
        
        # Toxin Label
        self.toxin_label = QLabel('Toxin')
        self.digestion_layout.addWidget(self.toxin_label, 0, 2, 1, 1)
        
        # Brute
        self.brute_input = QDoubleSpinBox()
        self.brute_input.setDecimals(self.precision)
        self.brute_input.setRange(self.min_damage, self.max_damage)
        self.brute_input.setSingleStep(self.step_value)
        self.brute_input.setMaximumWidth(self.field_width)
        self.digestion_layout.addWidget(self.brute_input, 1, 0, 1, 1)
        
        # Burn
        self.burn_input = QDoubleSpinBox()
        self.burn_input.setDecimals(self.precision)
        self.burn_input.setRange(self.min_damage, self.max_damage)
        self.burn_input.setSingleStep(self.step_value)
        self.burn_input.setMaximumWidth(self.field_width)
        self.digestion_layout.addWidget(self.burn_input, 1, 1, 1, 1)
        
        # Toxin
        self.toxin_input = QDoubleSpinBox()
        self.toxin_input.setDecimals(self.precision)
        self.toxin_input.setRange(self.min_damage, self.max_damage)
        self.toxin_input.setSingleStep(self.step_value)
        self.toxin_input.setMaximumWidth(self.field_width)
        self.digestion_layout.addWidget(self.toxin_input, 1, 2, 1, 1)
        
        # Suffocation Label
        self.suffocation_label = QLabel('Suffocation:')
        self.digestion_layout.addWidget(self.suffocation_label, 2, 0, 1, 1)
        
        # Clone Label
        self.clone_label = QLabel('Clone:')
        self.digestion_layout.addWidget(self.clone_label, 2, 1, 1, 1)
        
        # Suffocation
        self.suffocation_input = QDoubleSpinBox()
        self.suffocation_input.setDecimals(self.precision)
        self.suffocation_input.setRange(self.min_damage, self.max_oxy_damage)
        self.suffocation_input.setSingleStep(self.step_value)
        self.suffocation_input.setMaximumWidth(self.field_width)
        self.digestion_layout.addWidget(self.suffocation_input, 3, 0, 1, 1)
        
        # Clone
        self.clone_input = QDoubleSpinBox()
        self.clone_input.setDecimals(self.precision)
        self.clone_input.setRange(self.min_damage, self.max_damage)
        self.clone_input.setSingleStep(self.step_value)
        self.clone_input.setMaximumWidth(self.field_width)
        self.digestion_layout.addWidget(self.clone_input, 3, 1, 1, 1)
        
        self.layout.addWidget(self.digestion_groupbox, 5, 1, 1, 1)
        
        self.contamination_groupbox = QGroupBox('Contamination')
        self.contamination_layout = QGridLayout(self.contamination_groupbox)
        
        self.contaminates_switch = QCheckBox('Contaminates', self)
        self.contaminates_switch.toggled.connect(self.toggle_contamination)
        self.contamination_layout.addWidget(self.contaminates_switch, 0, 0, 1, 1)
        
        # Flavor Label
        self.flavor_label = QLabel('Flavor:')
        self.contamination_layout.addWidget(self.flavor_label, 1, 0, 1, 1)
        
        # Flavor
        self.flavor_combobox = QComboBox()
        self.flavor_combobox.addItems(CONTAMINATION_FLAVORS)
        self.contamination_layout.addWidget(self.flavor_combobox, 2, 0, 1, 1)
        
        # Color Label
        self.color_label = QLabel('Color:')
        self.contamination_layout.addWidget(self.color_label, 1, 1, 1, 1)
        
        # Color
        self.color_combobox = QComboBox()
        self.color_combobox.addItems(CONTAMINATION_COLOURS)
        self.contamination_layout.addWidget(self.color_combobox, 2, 1, 1, 1)
        
        self.layout.addWidget(self.contamination_groupbox, 6, 0, 1, 1)
        
        # Egg
        self.egg_groupbox = QGroupBox('Egg')
        self.egg_layout = QGridLayout(self.egg_groupbox)
        
        self.egg_min_size = 0
        self.egg_max_size = 200
        
        self.egg_type_label = QLabel('Type:')
        self.egg_layout.addWidget(self.egg_type_label, 0, 0, 1, 1)
        
        self.egg_name_label = QLabel('Custom Name:')
        self.egg_layout.addWidget(self.egg_name_label, 0, 1, 1, 1)
        
        self.egg_size_label = QLabel('Custom Size:')
        self.egg_layout.addWidget(self.egg_size_label, 0, 2, 1, 1)
        
        self.egg_type_combobox = QComboBox()
        self.egg_type_combobox.addItems(EGG_OPTIONS)
        self.egg_type_combobox.setMaximumWidth(self.field_width)
        self.egg_layout.addWidget(self.egg_type_combobox, 1, 0, 1, 1)
        
        self.egg_name_input = QLineEdit()
        self.egg_name_input.setMaximumWidth(self.field_width)
        self.egg_layout.addWidget(self.egg_name_input, 1, 1, 1, 1)
        
        self.egg_size_input = QDoubleSpinBox()
        self.egg_size_input.setDecimals(0)
        self.egg_size_input.setRange(self.egg_min_size, self.egg_max_size)
        self.egg_size_input.setMaximumWidth(self.field_width)
        self.egg_layout.addWidget(self.egg_size_input, 1, 2, 1, 1)
        
        self.layout.addWidget(self.egg_groupbox, 6, 1, 1, 1)
        
        self.toggle_vore_privacy_label = QLabel('Vore Privacy:')
        self.layout.addWidget(self.toggle_vore_privacy_label, 7, 0, 1, 1)
        
        self.drain_finishing_label = QLabel('Drain Finishing Mode:')
        self.layout.addWidget(self.drain_finishing_label, 7, 1, 1, 1)
        
        self.toggle_vore_privacy_combobox = QComboBox()
        self.toggle_vore_privacy_combobox.addItems(VORE_PRIVACY_OPTIONS)
        self.toggle_vore_privacy_combobox.setMaximumWidth(self.field_width)
        self.layout.addWidget(self.toggle_vore_privacy_combobox, 8, 0, 1, 1)
        
        self.drain_finishing_combobox = QComboBox()
        self.drain_finishing_combobox.addItems(DRAIN_FINISHING_OPTIONS)
        self.drain_finishing_combobox.setMaximumWidth(self.field_width)
        self.layout.addWidget(self.drain_finishing_combobox, 8, 1, 1, 1)
        
        self.size_label = QLabel('Shrink/Grow Size:')
        self.layout.addWidget(self.size_label, 9, 0, 1, 1)
        
        self.selective_mode_preference_label = QLabel('Selective Mode Preference:')
        self.layout.addWidget(self.selective_mode_preference_label)
        
        self.size_input = QDoubleSpinBox()
        self.size_input.setMaximumWidth(self.field_width)
        self.size_input.setRange(25, 200)
        self.size_input.setSingleStep(self.step_value)
        self.size_input.setDecimals(0)
        self.layout.addWidget(self.size_input, 9, 1, 1, 1)
        
        self.nutritional_percent_tag = QLabel('Nutritional Gain:')
        self.layout.addWidget(self.nutritional_percent_tag, 10, 0, 1, 1)
        
        self.bulge_size_tag = QLabel('Required Examine Size:')
        self.layout.addWidget(self.bulge_size_tag, 10, 1, 1, 1)
        
        self.nutritional_percent_input = QDoubleSpinBox()
        self.nutritional_percent_input.setMaximumWidth(self.field_width)
        self.nutritional_percent_input.setRange(0.01, 100)
        self.nutritional_percent_input.setDecimals(0)
        self.layout.addWidget(self.nutritional_percent_input, 11, 0, 1, 1)
        
        self.bulge_size_input = QDoubleSpinBox()
        self.bulge_size_input.setMaximumWidth(self.field_width)
        self.bulge_size_input.setRange(0, 200)
        self.bulge_size_input.setDecimals(0)
        self.layout.addWidget(self.bulge_size_input, 11, 1, 1, 1)
        
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        
    def toggle_emote(self, checked):
        if checked:
            self.emote_switch.setText('Active')
        else:
            self.emote_switch.setText('Disabled')
        self.delay_label.setVisible(checked)
        self.emote_delay_input.setVisible(checked)
    
    def toggle_contamination(self, checked):
        self.flavor_label.setVisible(checked)
        self.color_label.setVisible(checked)
        self.flavor_combobox.setVisible(checked)
        self.color_combobox.setVisible(checked)
        
    def set_belly_data(self, belly_data):
        self.can_taste_switch.setChecked(belly_data.get('can_taste', ''))
        self.entrance_logs_switch.setChecked(belly_data.get('entrance_logs', ''))
        self.is_feedable_switch.setChecked(belly_data.get('is_feedable', ''))
        self.display_absorbed_switch.setChecked(belly_data.get('display_absorbed_examine', ''))
        self.vore_spawn_blacklist_switch.setChecked(belly_data.get('vorespawn_blacklist', ''))
        self.recycling_switch.setChecked(belly_data.get('recycling', ''))
        self.storing_nutrition_switch.setChecked(belly_data.get('storing_nutrition', ''))
        self.item_digestion_logs_switch.setChecked(belly_data.get('item_digest_logs', ''))
        self.emote_switch.setChecked(belly_data.get('emote_active', ''))
        self.emote_delay_input.setValue(belly_data.get('emote_time', ''))
        self.brute_input.setValue(belly_data.get('digest_brute', ''))
        self.burn_input.setValue(belly_data.get('digest_burn', ''))
        self.toxin_input.setValue(belly_data.get('digest_tox', ''))
        self.suffocation_input.setValue(belly_data.get('digest_oxy', ''))
        self.clone_input.setValue(belly_data.get('digest_clone', ''))
        self.contaminates_switch.setChecked(belly_data.get('contaminates', ''))
        self.flavor_combobox.setCurrentText(belly_data.get('contamination_flavor', ''))
        self.color_combobox.setCurrentText(belly_data.get('contamination_color', ''))
        self.egg_type_combobox.setCurrentText(belly_data.get('egg_type', ''))
        self.egg_name_input.setText(belly_data.get('egg_name', ''))
        self.egg_size_input.setValue(belly_data.get('egg_size', ''))
        self.toggle_vore_privacy_combobox.setCurrentText(belly_data.get('eating_privacy_local', ''))
        self.drain_finishing_combobox.setCurrentText(belly_data.get('drainmode', ''))
        self.size_input.setValue(belly_data.get('shrink_grow_size', ''))
        self.nutritional_percent_input.setValue(belly_data.get('nutrition_percent', ''))
        self.bulge_size_input.setValue(belly_data.get('bulge_size', ''))
        
        self.toggle_emote(belly_data.get('emote_active', ''))
        self.toggle_contamination(belly_data.get('contaminates', ''))
        
    def get_belly_data(self):
        belly_data = {
            'can_taste': self.can_taste_switch.isChecked(),
            'entrance_logs': self.entrance_logs_switch.isChecked(),
            'is_feedable': self.entrance_logs_switch.isChecked(),
            'display_absorbed_examine': self.display_absorbed_switch.isChecked(),
            'vorespawn_blacklist': self.vore_spawn_blacklist_switch.isChecked(),
            'recycling': self.recycling_switch.isChecked(),
            'storing_nutrition': self.storing_nutrition_switch.isChecked(),
            'item_digestion_logs': self.item_digestion_logs_switch.isChecked(),
            'emote_active': self.emote_switch.isChecked(),
            'emote_time': self.emote_delay_input.value(),
            'digest_brute': math.clamp(self.brute_input.value(), self.min_damage, self.max_damage),
            'digest_burn': math.clamp(self.burn_input.value(), self.min_damage, self.max_damage),
            'digest_tox': math.clamp(self.toxin_input.value(), self.min_damage, self.max_damage),
            'digest_oxy': math.clamp(self.suffocation_input.value(), self.min_damage, self.max_oxy_damage),
            'digest_clone': math.clamp(self.clone_input.value(), self.min_damage, self.max_damage),
            'contaminates': self.contaminates_switch.isChecked(),
            'contamination_flavor': self.flavor_combobox.currentText(),
            'contamination_color': self.color_combobox.currentText(),
            'egg_type': self.egg_type_combobox.currentText(),
            'egg_name': None if self.egg_name_input.text() == "" else self.egg_name_input.text,
            'egg_size': 0 if self.egg_size_input.value() == 0 else math.clamp(self.egg_size_input, 25, 200),
            'eating_privacy_local': self.toggle_vore_privacy_combobox.currentText(),
            'drainmode': self.drain_finishing_combobox.currentText(),
            'shrink_grow_size': self.size_input.value(),
            'nutritional_percent': self.nutritional_percent_input.value(),
            'bulge_size': self.bulge_size_input.value()
        }
        return belly_data
