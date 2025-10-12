"""
File: Rig.py
Description: Module to define the Rig class and Methods part of
the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    """
    represents a computer object
    can take hits from data spikes, each hit increases the damage by 1
    if damage is 2 (for a level0 rig) it becomes broken

    """

    def __init__(self, name, storage, storage_size, damage=0, broken=False, upgrade_level=0,
                 data_spikes=2, removable_drives=1):
        pass

    def __str__(self):
        # name, condition, upgrade level, stored assets
        pass

    def store_asset(self):
        # method o transfer asset to and from hackers inventory
        pass

    def release_asset(self):
        # method o transfer asset to and from hackers inventory
        # encrypted assets can not be transferred until decrypted
        pass

    def extract_asset(self):
        # through consuming a removable drive
        # transferring all to their own inventory
        pass

    def generate_asset(self):
        # no control over what type of asset but it generates one at the time
        pass

    def rig_repair(self, counter: int, broken: bool):
        # Use of crypto token
        # if damaged the counter resets to 0
        # if not damaged print message
        pass

    def rig_condition(self):
        # based on damage and upgrade level 2-0?
        pass

    def rig_upgrade(self, hardware_patch):
        # require a rig and hardware patch
        # increases the rigs level which affects the battle damage and amount of assets stored
        pass