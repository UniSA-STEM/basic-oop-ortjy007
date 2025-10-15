"""
File: Rig.py
Description: Module to define the Rig class and Methods part of
the Into the Grid OOP Basic Programming assessment COMP 1048 2025P6.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import re
import Asset
import Hacker


class Rig:
    """
    Rig class with the following attributes:

    +name: str

    -damage: int

    -broken: bool

    -level: int # # Using a hardware_patch, affects battles damage and amount
    of assets stored

    -storage: list # Starts with two data_spikes and one removable_drive

    -storage_size: int # check if this is independent or part of the storage
    attribute

    the following methods:
    scan_storage: str #list of items contained in the Rig's storage

    generate_asset: # one per turn? and what asset can be generated?, level
    dependent? to be saved as asset

    store_asset: list # Saves asset in Rig's storage

    use_asset: list # Delete's asset fom Rig's storage either used in actions
    or consumed during upgrades

    transfer_asset: target_rig: str, originator_rig: str, target_rig_staus: str,
    originator_rig_status: str # need to check staus of rig (not damaged), and
    asset (not encrypted) update both target and originator storage lists

    extract_asset:

    rig_repair: target_rig: str # need a crypto_token, resets damage to 0 and
    broken to False

    rig_condition: target_rig: str

    rig_update: target_rig: str, hacker: str # requires Hardware patch, increases rig level, improves storage
        size, reduces attacks damage.

    and the following properties:
    name

    storage

    damage

    broken

    level

    ##### Extract to be deleted:
    A Rig represents a computer object.
    Can take hits from data spikes, each hit increases the damage by 1,
    if damage is 2 (for a level0 rig) it becomes broken.
    """

    def __init__(self, name: str) -> None:
        self.__name = name if (name == re.search(r'[a-zA-Z]', name)
                               or re.search(r'\d', name)) else 'Invalid name.'
        self.__storage_size = 5
        self.__storage = []
        self.__damage = 0
        self.__broken = False
        self.__level = 0

    def __str__(self) -> str:
        # name, condition, upgrade level, stored assets
        return f'Name: {self.__name}\nCondition: {'Operational' 
        if not self.__broken else 'Broken'}'
        #f'Stored assets:{Rig.STORAGE}')

    @property
    def get_name(self) -> str:
        return self.__name

    @property
    def get_storage(self) -> list:
        return self.__storage

    @property
    def get_damage(self) -> int:
        return self.__damage

    @property
    def get_broken(self) -> bool:
        return self.__broken

    @property
    def get_level(self) -> int:
        return self.__level

    def scan_storage(self, storage: list) -> list:
        pass

    def generate_asset(self) -> None:
        # no control over what type of asset but it generates one at the time
        pass

    def store_asset(self, asset) -> list:
        """
        Method to transfer save asset in Rig's storage
        :param asset:
        :return: self.__storage
        """
        # Validating asset and storage capacity
        if asset.is_asset() and len(self.__storage) <= self.__storage_size:
            self.__storage.append(asset)
            print(f"asset {asset.get_name} has been put in the Rig's storage")
        elif not asset.is_asset():
            print('"non-assets cannot be saved in storage')
        elif len(self.__storage) >= self.__storage_size:
            print(f'Storage is a maximum capacity, asset cannot be saved')
        return self.__storage

    def use_asset(self, asset):
        if asset.is_asset() and asset in self.__storage:
            self.__storage.remove(asset)
            print(f'asset {asset.get_name} has been used and removed from storage')
        elif not asset.is_asset():
            print('"non-assets cannot be used')
        return self.__storage

    def transfer_asset(self, asset_name: str, asset_encrypted: bool, hacker_name: str) -> list:
        hacker_name = Hacker.Hacker.get_name
        if asset_name in self.__storage and asset_encrypted == False:
            released_asset = asset_name
            Hacker.name.inventory

        # method o transfer asset to and from hackers inventory
        # encrypted assets can not be transferred until decrypted
        pass

    def extract_asset(self, asset_name: str, asset_encrypted: bool) -> str:
        # through consuming a removable drive
        # transferring all to their own inventory
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

    # Properties
    name = property(get_name)
    storage = property(get_storage)
    damage = property(get_damage)
    broken = property (get_broken)
    level = property (get_level)