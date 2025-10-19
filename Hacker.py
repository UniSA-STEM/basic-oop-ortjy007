"""
File: Hacker.py
Description: Module to define the Hacker class and Methods part of
the Into the Grid OOP Basic Programming assessment COMP 1048 2025P6.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import re
from Rig import Rig
from Asset import Asset
import sys
import os

class Hacker:
    """
    Hacker represents a person (with a cryptic and/or stylish pseudonym) who
    uses computers to gain unauthorized access to data.

    Class attributes:
    USED_ASSETS: []  used for recycling

    Instance attributes:
    +name: str
    -exposed: bool
    -trace_level: int
    -inventory: []

    Methods w/decorators:
    +name @property getter + setter
    +encrypted @property getter + setter
    +description @property getter + setter

    And the following methods:
    acquiring_rig: Using the Rig module to acquire a Rig after
    cyber_token validation.
    scanning_inventory: searches for a specific asset and returns True
    if found.
    storing_asset: storage asset in inventory after validation.
    retrieving_asset: checks the inventory and if found retrieves a
    specific asset.
    extracting_assets: extracting assets from target rig transferred to
    Hackers inventory.
    encrypting_decrypting_assets: as noted after security_chip validation.
    launching_data_spikes: attack on a Hackers rig after data_spike
    validation.
    exposing: trace level <= 5 the exposed variable changes to True.
    -recycling: storing the used assets for recycling....
    """

    USED_ASSETS = []  # used for recycling :)

    def __init__(self, name: str, rig: str):
        """
        NOTE:
        On initiation instead of allocating a crypto token to storage to be issued
        to acquire a Rig, the crypto token gets passed directly to the Rig's
        acquisition with the inventory initiated but empty.
        """

        # Using redirecting the standard output stream while the assets
        # are created during initialization

        or_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

        self.name = name
        self.trace_level = 0
        self.exposed = False
        self.inventory = [Asset('crypto_token')]
        self.rig = Rig(rig)

        # Standard output stream restored
        sys.stdout.close()
        sys.stdout = or_stdout

        print(f'{name} Hacker and {rig} Rig created during initialization\n'
              f'... whatever happens, happens...\n\n')

    def __str__(self) -> str:
        inv_names= []

        for Asset.name in self.__inventory:
            inv_names.append(Asset.name)
        return f'Hacker Name: {self.__name}\nRig name: {self.__rig}\nInventory: {self.__inventory}'

    @property
    def name(self) -> str:
        """Name property"""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:

        if name == re.search(r'[a-zA-Z]', name) or re.search(r'\d', name):
            self.__name = name
        else:
            print('Invalid name, default name used.')

    @property
    def trace_level(self) -> int:
        """trace_level property"""
        return self.__trace_level

    @trace_level.setter
    def trace_level(self, h_trace_level: int) -> None:
        self.__trace_level = h_trace_level

    @property
    def exposed(self) -> bool:
        """exposed property"""
        return self.__exposed

    @exposed.setter
    def exposed(self, h_exposed: bool) -> None:
        self.__exposed = h_exposed

    @property
    def inventory(self) -> list:
        """inventory property"""
        return self.__inventory

    @inventory.setter
    def inventory(self, h_inventory: list) -> None:
        self.__inventory = h_inventory

    @property
    def rig(self) -> Rig:
        """rig property"""
        return self.__rig

    @rig.setter
    def rig(self, h_rig: Rig) -> None:
        self.__rig = h_rig

    # Class Methods
    def acquiring_rig(self, r_name: str) -> None:
        """
        Rig acquisition for Hacker's use following the cyber token asset
        validation if stored in inventory. Token gets deleted from inventory
         and recycled.
        :param r_name: str
        :return: None
        """
        # Validating crypto token
        if 'crypto_token' in Asset.ASSET_NAMES:
            inventory = [Asset.name for Asset.name in self.__inventory]
            if 'crypto_token' in inventory:

                # Recycling data spike
                self.__recycling('crypto_token')

                # Generating new Rig
                self.__rig = Rig(r_name)
                print(f'{r_name} Rig has been acquired and is operational.\n'
                      f'One crypto token removed from inventory')
            else:
                print('Acquiring a Rig can only be done using a valid '
                      'crypto token.\n')
        else:
            print('You can only have one active Rig. No rig acquired.')

    def scanning_inventory(self, asset_name: str) -> bool:
        """
        Scans the Hackers inventory for a specific asset, returns a
        boolean value.
        :param asset_name: str
        :return: bool
        """
        found_asset = False

        # Validating asset name and checking inventory list
        if asset_name in Asset.ASSET_NAMES:
            inventory = [Asset.name for Asset.name in self.__inventory]
            if asset_name in inventory:
                found_asset = True
                print(f'{asset_name} found.')
            else:
                print(f'{asset_name} not in inventory.')
        else:
            print(f'{asset_name} is not a valid asset, no search carried out.')
        return found_asset

    def storing_asset(self, asset: Asset) -> None:
        """
        Storing assets in the Hacker's inventory after validation
        and printing the revised contents of inventory w/ decryption
        status.
        :param asset: Asset
        :return:
        """
        # Validating asset and storing it
        if isinstance(asset, Asset) and asset.encrypted != True:
            self.__inventory.append(asset)

            # Extracting the names and encryption status of the assets
            # into a temp list
            tmp_list = []
            group_s = 3

            for item in self.__inventory:
                tmp_list.append('A')
                tmp_list.append(item.name)
                tmp_list.append('has been stored.')

            # printing in legible groups
            for i in range(0, len(tmp_list), group_s):
                group = tmp_list[i:i + group_s]
            print(*group)

        else:
            print('Only decrypted valid assets can be saved')

    def retrieving_asset(self, asset_name: str) -> Asset:
        """
        If asset exist in inventory move it from inventory to a
        holding variable that gets passed as return.
        :param asset_name: str
        :return: asset
        """
        r_asset = None
        if asset_name in self.__inventory:
            r_asset = self.__inventory[self.__inventory.index(asset_name)]
            del self.__inventory[self.__inventory.index(asset_name)]
            print(f'{asset_name} retrieved successfully.')
        return r_asset

    def extracting_assets(self, target: Rig) -> None:
        """
        Extracting assets from a target rig. Validating if we have a Rig,
        if the Hacker is exposed and if it is a valid Hacker.
        :param target: Rig
        :return: None
        """
        # Temp list to hold the names of extracted assets
        e_asset = []

        # Validating Rig existence, exposure and valid target - broken -
        # in that order
        if self.__rig is None:
            print('A Rig is needed to extract assets.')
        elif self.__exposed:
            print("Your can't extract assets while exposed.")
        elif isinstance(target, Hacker):
            if target.rig.broken:
                for item in target.rig.storage:
                    if not item.encrypted:
                        self.__inventory.append(item)
                        e_asset.append(item.name)
                        target.rig.storage.remove(item)

                        self.trace_level += 1
                print(f'The following assets were extracted {e_asset}.')
            else:
                print(f'No items can be extracted unless the target Rig '
                      f'is broken')
        else:
            print('Extracting assets unsuccessful.')

    def encrypting_decrypting_asset(self, asset: Asset) -> None:
        """
        Encrypting and decrypting valid assets after security chip validation.
        :param asset: Asset
        :return: None
        """
        # Checking if asset is valid
        if isinstance(asset, Asset):

            # Validating security chip
            if 'security_chip' in Asset.ASSET_NAMES:
                inventory = [Asset.name for Asset.name in self.__inventory]
                if 'security_chip' in inventory:

                    # Recycling security chip
                    self.__recycling('security_chip')

                    # Updating asset status
                    if asset.encrypted:
                        asset.encrypted = False
                        print(f'{asset.name} has been decrypted.')
                    elif not asset.encrypted:
                        asset.encrypted = True
                        print(f'{asset.name} has been encrypted.')
            else:
                print('Need a valid security chip to proceed with decryption/encryption.')
        else:
            print('Only valid assets can be decrypted/encrypted.')

    def launching_data_spikes(self, target: Rig) -> None:
        """
        Launching data spikes attacks after validating data_spike token, rig, exposure
        and target rig. Data_spike automatically deleted from inventory. Trace level
        increased by 1.
        :param target: Rig
        :return: None
        """
        # Validating Rig, exposure, target and token in that order
        if self.__rig is None:
            print('A Rig is needed to launch attacks.')
        elif self.__exposed:
            print("Your can't attack while exposed.")
        elif not isinstance(target, Rig):
            print('The target needs to be a valid Rig.')
        elif 'data_spike' in Asset.ASSET_NAMES:
            inventory = [Asset.name for Asset.name in self.__inventory]
            if 'data_spike' in inventory:

                # Recycling data spike
                self.__recycling('data_spike')

                # Attack and message to user
                Hacker.target.taking_hits()
                print(f'Attack successful.')

                self.trace_level += 1
        else:
            print(f'Attack unsuccessful.')

    def exposing(self):
        """
        exposing method to update the trace value if trace level reaches
        5 otherwise it will revert to False.
        :return: None
        """
        if self.__trace_level == 5:
            self.__exposed = True
        if self.__trace_level < 5:
            self.__exposed = False

    def __recycling(self, asset_name: str) -> None:
        """
        private method to identify, remove and recycle asset once its
        existence has been validated
        :param asset_name: str
        :return: None
        """
        inv_names = []

        for Asset.name in self.__inventory:
            inv_names.append(Asset.name)
        ndx = inv_names.index(asset_name)
        tmp = self.__inventory[ndx]
        Hacker.USED_ASSETS.append(tmp)
        self.__inventory.remove(Asset.name == asset_name)
