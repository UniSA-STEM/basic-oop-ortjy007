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
import Asset


class Hacker:
    """
    Hacker represents a person (with a cryptic and/or stylish pseudonym) who
    uses computers to gain unauthorized access to data.

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
    Acquiring_rig: Rig_name # linked to Hacker?
    Launching_data_spikes: target_rig  # same as launch attack?? consumes data
    spike from own storage
    Extracting_asset: target_rig, asset_names # only if the rig is broken and the
        assets are unsecured (non encrypted) assets (all of them) and consumes
        a movable drive, transfers assets to own storage
    Encrypting_asset: asset_name, security_chip # done inside their inventory or
        Rig's storage, check security chip first, update storage. Encrypted
        assets can not be transferred.
    Decrypting_asset: asset_name
    Storing_asset: storage_name # check capacity
    Retrieving_asset: checks the inventory and if found retrieves a
    specific asset
    Scanning_inventory: searches for a specific asset and returns True
    if found
    """

    def __init__(self, name: str, rig: str):
        """
        NOTE:
        On initiation instead of allocating a crypto token to storage to be issued
        to acquire a Rig, the crypto token gets passed directly to the Rig's
        acquisition with the inventory initiated but empty.
        """
        self.name = name
        self.trace_level = 0
        self.exposed = False
        self.inventory = []
        self.rig = rig

        Hacker.acquiring_rig('r1', Asset.Asset('crypto_token'))

        # pass in or instatiate an acquire Rig method

    def __str__(self) -> str:
        return f'{self.__name}\nRig name:{Asset.name}\nInventory:{self.__inventory}'

    @property
    def name(self) -> str:
        """Name property"""
        return self.__name

    @name.setter
    def name(self, h_name: str) -> None:
        self.__name = h_name if (h_name == re.search(r'[a-zA-Z]', h_name)
                                 or re.search(r'\d', h_name)) else 'Invalid name.'

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
    def rig(self) -> list:
        """rig property"""
        return self.__rig

    @rig.setter
    def rig(self, h_rig: list) -> None:
        self.__rig = h_rig

    # Class Methods
    def acquiring_rig(self, rig_name: str, asset: Asset) -> None:

        if isinstance(asset, Asset.Asset) and asset.name == 'crypto_token':
            self.__rig = Rig(rig_name)

            print(f'{self.__name} has been upgraded to '
                  f'{Rig.CONDITION[self.__condition]}.')
        else:
            print('Upgrade can only be done using a hardware_patch.\n')
        # print message announcing activation
        pass

    def launching_data_spikes(self) -> str:
        # consumes data spikes from their rigs storage
        pass

    def extracting_asset(self) -> str:
        pass

    def encrypting_asset(self, security_chip) -> bool:
        pass

    def decrypting_asset(self, security_chip) -> bool:
        pass

    def storing_asset(self, asset_name: str) -> str:
        # between inventory and rigs storage
        pass

    def retrieving_asset(self, asset_name: str) -> Asset:
        """
        If asset exist in inventory move it from inventory to a
        holding variable that gets passed as return.
        :param asset_name: str
        :return: asset
        """
        asset = None
        if Hacker.scanning_inventory(asset_name):
            asset = self.__inventory[self.__inventory.index(asset_name)]
            del self.__inventory[self.__inventory.index(asset_name)]
        return asset

    def scanning_inventory(self, asset_name: str) -> bool:
        """
        Scans the Hackers inventory and returns a boolean value.
        :param asset_name: str
        :return: bool
        """
        found_asset = False
        if asset_name in Asset.Asset.ASSET_NAMES:
            inventory = [Asset.Asset.name for Asset.Asset in self.__inventory]
            if asset_name in inventory:
                found_asset = True
                print(f'{asset_name} found.')
            else:
                print(f'{asset_name} not in inventory.')
        else:
            print(f'{asset_name} is not a valid asset')
        return found_asset
