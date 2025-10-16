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
from Asset import Asset

import Hacker


class Rig:
    """
    Rig class with the following attributes:
    +name: str
    -damage: int
    -broken: bool
    -level: int
    -storage: list
    -storage_size: int

    Rig class methods:
    scan_storage: Generates a list of items contained in the Rig's
    storage including encryption status.
    generate_asset: Generate a random asset from the Asset module
    store_asset: Saves asset in Rig's storage.
    use_asset: Delete's asset fom Rig's storage either used in actions
    or consumed during upgrades.
    transfer_asset:
    extract_asset:
    rig_repair: Repairs a Rig's if the Rig is damaged and a crypto_token is
    given; damage gets reset to 0 and broken status changed to False.
    rig_condition: Prints the condition of the Rig (0-2).
    rig_update: Upgrades Rig's level if a hardware_patch is given.

    Properties:
    name, storage, damage, broken, level
    """

    def __init__(self, r_name: str) -> None:
        self.r_name = r_name
        self.__storage_size = 5
        self.__storage = [Asset.ASSET_NAMES[1], Asset.ASSET_NAMES[1],
                          Asset.ASSET_NAMES[3]
                          ]
        self.__damage = 0
        self.__broken = False if self.__damage != 2 else True
        self.__upgrade_level = 0

    def __str__(self) -> str:
        # name, condition, upgrade level, stored assets
        return f'Name: {self.__r_name}\nCondition: {'Operational'
        if not self.__broken else 'Broken'}'
        # f'Stored assets:{Rig.STORAGE}')

    # Getters
    def get_r_name(self) -> str:
        return self.__r_name

    def get_storage(self) -> list:
        return self.__storage

    def get_damage(self) -> int:
        return self.__damage

    def get_broken(self) -> bool:
        return self.__broken

    def get_upgrade_level(self) -> int:
        return self.__upgrade_level

    # Setters
    def set_r_name(self, r_name: str) -> None:
        """
        Validating rig name (letters and numbers only)
        :param r_name: str
        :return: None
        """
        if r_name == re.search(r'[a-zA-Z]', r_name) or re.search(r'\d', r_name):
            self.__r_name = r_name
        else:
            print(f'Invalid name. Letters and numbers only.')

    def set_storage_size(self, size: int) -> None:
        """
        Validating storage size with an integer between 1 - 10, if invalid
        input the storage size is reset to a default value of 5
        :param size: int
        :return: None
        """
        if isinstance(size, int) and size > 0 and size <= 10:
            self.__storage_size = size
        else:
            self.__storage_size = 5
            print('The Rig storage size needs to be a number between 1 - 10.\n'
                  'Rig storage size reset to 5')

    def set_damage(self, damage: int) -> None:
        """
        Validating storage size with an integer between 0 - 2, if invalid
        input damage is set to a default value of 0
        :param damage: int
        :return: None
        """
        if isinstance(damage, int) and damage >= 0 and damage <= 2:
            self.__damage = damage
        else:
            self.__damage = 0
            print('The damage can only be between 0 - 2.\n'
                  'Rig damage reset to 0.')

    def set_broken(self, is_broken: bool) -> None:
        """
        Validating broken status as boolean, if invalid input the status
        is reset to a default value of False.
        :param is_broken:
        :return:
        """
        if isinstance(is_broken, bool):
            self.__broken = is_broken
        else:
            self.__broken = False
            print('Broken status can only be True or False.\n'
                  'Rig broken status reset to False')

    def set_upgrade_level(self) -> None:
        if self.__damage < 2:
            self.__damage += 1
        else:
            print('The Rig has maximum damage and is broken')

    def scan_storage(self) -> list:
        """
        Method to retrieve a list of contents in the Rig's storage including
        its maximum capacity and whether the asset is encrypted or not
        :return: self.__storage
        """
        print(f"\n{self.__r_name}'s storage capacity is: {self.__storage_size}")
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
        select = randint(0, len(Asset.asset_names) - 1)
        new_asset = Asset.Asset(Asset.asset_names[select])
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
        print(f"\n{self.__r_name}'s condition is {condition[self.__damage]}")
        return None

    def rig_upgrade(self, asset) -> None:
        if asset.get_name == 'hardware_patch':
            self.__upgrade_level += 1
            print(f"{self.__r_name}'s has been updated to level {self.__upgrade_level}.")
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
#r2.generate_asset()

