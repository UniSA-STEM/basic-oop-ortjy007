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
    A Rig represents a computer object.
    Can take hits from data spikes, each hit increases the damage by 1,
    if damage is 2 (for a level0 rig) it becomes broken.

    Rig class with the following attributes:
    +name: str
    -damage: int
    -broken: bool
    -level: int # # Using a hardware_patch, affects battles damage and amount of assets stored
    -storage: list # Starts with two data_spikes and one removable_drive
    -storage_size: int # check if this is independent or part of the storage attribute

    And the following methods:
    generate_asset:
        # one per turn? and what asset can be generated?, level dependent? to be saved as asset
    launch_data_spikes: target_rig
        # update target_rig status and originator_rig storage lists
    rig_repair: target_rig # need a crypto_token, resets damage to 0 and broken to False
    rig_condition: target_rig
    extract_asset: target_rig, originator_rig, target_rig_staus, originator_rig_status
        # need to check staus of rig (not damaged), and
        asset (not encrypted) update both target and originator storage lists
    store_asset: add to storage list # amount of storage is level dependent,is there a maximum/minimum capacity?
    release_asset: bool
        # based on Hacker action
    scan_inventory: str
        #list of items contained in the Rig's storage
    """

    def __init__(self, name, storage, storage_size, damage=0, broken=False, level=0,
                 data_spikes=2, removable_drives=1) -> None:
        self.name = name
        self.__storage = storage
        self.__storage_size = storage_size
        self.__damage = damage
        self.__broken = broken
        self.__level = level
        self.__data_spikes = data_spikes
        self.__removable_drives = removable_drives

    def __str__(self) -> str:
        # name, condition, upgrade level, stored assets
        return (f'{self.name}\nCondition:{self.__broken}\nUpgrade level:{self.__level}\n'
                f'Stored assets:{self.__storage}')

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
