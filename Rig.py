"""
File: Rig.py
Description: Module to define the Rig class and Methods part of
the Into the Grid OOP Basic Programming assessment COMP 1048 2025P6.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


STORAGE = []  # WIP to include all assets identified

class Rig:
    """
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

    launch_data_spikes: target_rig: str
        # update target_rig status and originator_rig storage lists

    rig_repair: target_rig: str # need a crypto_token, resets damage to 0 and broken to False

    rig_condition: target_rig: str

    rig_update: target_rig: str, hacker: str # requires Hardware patch, increases rig level, improves storage
        size, reduces attacks damage.

    extract_asset: target_rig: str, originator_rig: str, target_rig_staus: str, originator_rig_status: str
        # need to check staus of rig (not damaged), and
        asset (not encrypted) update both target and originator storage lists

    store_asset: bool? #add to storage list # amount of storage is level dependent,is there a maximum/minimum capacity?

    release_asset: bool
        # based on Hacker action

    scan_storage: str
        #list of items contained in the Rig's storage

    ##### Extract to be deleted:
    A Rig represents a computer object.
    Can take hits from data spikes, each hit increases the damage by 1,
    if damage is 2 (for a level0 rig) it becomes broken.
    """

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__storage_size = 0
        self.__damage = 0
        self.__broken = False
        self.__level = 0

    def __str__(self) -> str:
        # name, condition, upgrade level, stored assets
        return f'Name: {self.__name}\nCondition: {'Operational' 
        if not self.__broken else 'Broken'}'
        #f'Stored assets:{Rig.STORAGE}')

    # Getter
    def get_name(self) -> str:
        return self.__name

    def get_damage(self) -> int:
        return self.__damage

    def get_broken(self) -> bool:
        return self.__broken

    def get_level(self) -> int:
        return self.__level

    # Setter
    def set_name(self, name: str) -> str:
        if type(name) == str:
            self.__name = name
        else:
            print('Invalid name.')
        return self.__name

    def store_asset(self, asset_name: str) -> str:
        #if isinstance(asset_name, Asset) and

        # method o transfer asset to and from hackers inventory
        pass

    def release_asset(self, asset_name: str, asset_encrypted: bool) -> str:
        # method o transfer asset to and from hackers inventory
        # encrypted assets can not be transferred until decrypted
        pass

    def extract_asset(self, asset_name: str, asset_encrypted: bool) -> str:
        # through consuming a removable drive
        # transferring all to their own inventory
        pass

    def generate_asset(self) -> None:
        # no control over what type of asset but it generates one at the time
        pass

    def rig_repair(self, crypto_token: bool, counter: int, broken: bool) -> None:
        # Use of crypto token
        # if damaged the counter resets to 0
        # if not damaged print message
        pass

    def rig_condition(self, level: int) -> int:
        # based on damage and upgrade level 2-0?
        pass

    def rig_upgrade(self, hardware_patch: bool, level: int) -> int:
        # require a rig and hardware patch
        # increases the rigs level which affects the battle damage and amount of assets stored
        pass

    def scan_storage(self, storage: list) -> list:
        pass

    # Properties
    name = property(get_name, set_name)
    damage = property(get_damage)
    broken = property (get_broken)
    level = property (get_level)