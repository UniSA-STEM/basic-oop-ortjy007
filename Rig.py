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
from random import randint

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
    scan_storage: Generates a list of items contained in the Rig's
    storage including encryption status.

    generate_asset: Generate a random asset from the Asset module

    store_asset: Saves asset in Rig's storage.

    use_asset: Delete's asset fom Rig's storage either used in actions
    or consumed during upgrades.

    transfer_asset: target_rig: str, originator_rig: str, target_rig_staus: str,
    originator_rig_status: str # need to check staus of rig (not damaged), and
    asset (not encrypted) update both target and originator storage lists.

    extract_asset:

    rig_repair: Repairs a Rig's if the Rig is damaged and a crypto_token is
    given; damage gets reset to 0 and broken status changed to False.

    rig_condition: Prints the condition of the Rig (0-2).

    rig_update: Upgrades Rig's level if a hardware_patch is given.

    and the following properties:
    name

    storage

    damage

    broken

    level
    """

    def __init__(self, name: str) -> None:
        self.__name = name if (name == re.search(r'[a-zA-Z]', name)
                               or re.search(r'\d', name)) else 'Invalid name.'
        self.__storage_size = 5
        self.__storage = [Asset.Asset('data_spike'), Asset.Asset('data_spike'),
                          Asset.Asset('removable_drive')
                          ]
        self.__damage = 0
        self.__broken = False if self.__damage != 2 else True
        self.__upgrade_level = 0

    def __str__(self) -> str:
        # name, condition, upgrade level, stored assets
        return f'Name: {self.__name}\nCondition: {'Operational'
        if not self.__broken else 'Broken'}'
        # f'Stored assets:{Rig.STORAGE}')

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
        return self.__upgrade_level

    def scan_storage(self) -> list:
        """
        Method to retrieve a list of contents in the Rig's storage including
        its maximum capacity and whether the asset is encrypted or not
        :return: self.__storage
        """
        print(f"\n{self.__name}'s storage capacity is: {self.__storage_size}")
        print(f'And contains the following assets:')
        for item in self.__storage:
            print(f'{item.get_name} ({'encrypted' if item.get_encrypted
            else 'decrypted'})')
        return self.__storage

    def generate_asset(self) -> Asset:
        """
        Generating a random asset from the Asset types valid in the
        Asset module
        :return: new asset
        """
        select = randint(0, len(Asset.Asset.types_) - 1)
        new_asset = Asset.Asset(Asset.Asset.types_[select])
        print(f'The following asset has been created: {new_asset.get_name}')
        return new_asset

    def store_asset(self, asset) -> list:
        """
        Method to transfer save asset in Rig's storage
        :param asset: validated as asset
        :return: self.__storage
        """
        # Validating asset and storage capacity
        if asset.is_asset() and len(self.__storage) <= self.__storage_size:
            self.__storage.append(asset)
            print(f"asset {asset.get_name} has been put in the Rig's storage")
        elif not asset.is_asset():
            print('non-assets cannot be saved in storage')
        elif len(self.__storage) >= self.__storage_size:
            print(f'Storage is a maximum capacity, asset cannot be saved')
        return self.__storage

    def use_asset(self, asset):
        """
        Method to remove assets from storage
        :param asset: validated as asset
        :return: self.__storage
        """
        # Validating asset and checking if it exists in storage
        if asset.is_asset() and asset in self.__storage:
            self.__storage.remove(asset)
            print(f'asset {asset.get_name} has been used and removed '
                  f'from storage')
        elif not asset.is_asset():
            print('"non-assets cannot be used')
        return self.__storage

    def transfer_asset(self, name: str, asset_encrypted: bool, hacker_name: str) -> list:
        hacker_name = Hacker.Hacker.get_name
        if name in self.__storage and asset_encrypted == False:
            released_asset = name
            # Hacker.get_name.inventory

        # method o transfer asset to and from hackers inventory
        # encrypted assets can not be transferred until decrypted
        pass

    def extract_asset(self, name: str, asset_encrypted: bool) -> str:
        # through consuming a removable drive
        # transferring all to their own inventory
        pass

    def rig_repair(self, asset) -> None:
        """
        Method to repair a damaged Rig
        :param asset: validated as 'crypto_token'
        :return: None
        """
        if not self.__broken:
            print('Rig is not broken no repairs needed')
        elif not asset.get_name == 'crypto_token':
            print('Invalid asset, you need a Rig crypto_token to repair a Rig')
        else:
            self.__damage = 0
            print(f'Rig repaired: damage level reset to {self.__damage}')
        return None

    def rig_condition(self) -> None:
        """
        Method to check the condition of a Rig
        :return: None
        """
        condition = {0: 'Pristine', 1: '50%', 2: 'Broken'}
        print(f"\n{self.__name}'s condition is {condition[self.__damage]}")
        return None

    def rig_upgrade(self, asset) -> None:
        if asset.get_name == 'hardware_patch':
            self.__upgrade_level += 1
            print(f"{self.__name}'s has been updated to level {self.__upgrade_level}.")
        return None

    # Properties
    name = property(get_name)
    storage = property(get_storage)
    damage = property(get_damage)
    broken = property(get_broken)
    level = property(get_level)


r2 = Rig('r2')
"""
print(r2.get_broken)
r2.rig_condition()

asset1 = Asset.Asset('crypto_token')
asset2 = Asset.Asset('hardware_patch')
print(asset1.is_asset())
print(asset1.get_name)
r2.rig_repair(asset1)
r2.rig_upgrade(asset2)
"""
r2.generate_asset()
