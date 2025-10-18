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
    Retrieving_asset: storage_name(Rig), inventory(Hacker), asset_name # update
        inventory or Rig storage
    Scanning_inventory: #identify assents, quantity, status (encrypted/decrypted)
    """

    def __init__(self, name: str):
        self.name = name
        self.trace_level = 0
        self.exposed = False
        self.inventory = []

        # pass in or instatiate an acquire Rig method

    def __str__(self) -> str:
        return f'{self.__name}\nRig name:{Asset.__get_asset_name}\nInventory:{self.__inventory}'

    @property
    def name(self) -> str:
        """Name property"""
        return self.__name

    @name.setter
    def name(self, s_name: str) -> None:
        self.__name = s_name if (s_name == re.search(r'[a-zA-Z]', s_name)
                                 or re.search(r'\d', s_name)) else 'Invalid name.'

    @property
    def trace_level(self) -> int:
        """trace_level property"""
        return self.__trace_level

    @trace_level.setter
    def trace_level(self, s_trace_level: int) -> None:
        self.__trace_level = s_trace_level

    @property
    def exposed(self) -> bool:
        """exposed property"""
        return self.__exposed

    @exposed.setter
    def exposed(self, s_exposed: bool) -> None:
        self.__exposed = s_exposed

    @property
    def inventory(self) -> list:
        """inventory property"""
        return self.__inventory

    @inventory.setter
    def inventory(self, s_inventory: list) -> None:
        self.__inventory = s_inventory

    # Class Methods
    def acquiring_rig(self) -> str:
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

    def storing_asset(self, asset_name: str) -> list:
        # between inventory and rigs storage
        pass

    def retrieving_asset(self, asset_name: str) -> str:
        # between inventory and rigs storage
        pass

    def scanning_inventory(self, inventory: list) -> list:
        # by name and returning if found
        pass
