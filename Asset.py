"""
File: Asset.py
Description: Module to define the Asset class and Methods part of
the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    """
    Representing digital assets can be moved between Hacker's inventory and
    their Rig's storage. Are used in actions or consumed during upgrades.
    Asset class with the following attributes:
    +name: str
    -description: str
    -encrypted=False

    And the following methods:
    +crypto_token: Rig_name # to acquire or repair rigs (H)
    +hardware_patch: rig_name # update rigs level & storage (H)
    +data_spikes: target_rig # check storage, update lists, update damage (R)
    +removable_drive: target_rig, destination_rig # found in rigs used for extraction (R)
    +security_rig: asset_name # used to encrypt or decrypt assets (H or R)

    Assets can be moved between hacker and rig , used in actions or consumed during upgrades
    """
    ASSETS = []  # wip to include all identified

    def __init__(self, name, description, encrypted=False) -> None:
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self) -> str:
        # return f'{self.name}\nRig name:{Asset.get_name}\nInventory:{self.__inventory}'
        # <name>:<description>[Encrypted]
        # <name>:<description>
        pass

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_encrypted(self, status) -> bool:
        return self.__encrypted

    # Setters
    def set_encrypted(self, status: bool) -> bool:
        self.__encrypted = status

    def crypto_token(self) -> str:
        # Hidden asset used to acquire or repair rigs
        pass

    def data_spike(self) -> str:
        # used in battles
        pass

    def removable_drive(self) -> str:
        # found in rigs and used for extraction
        pass

    def security_chip(self) -> str:
        # used to encrypt or decrypt assets
        pass

    def hardware_patch(self) -> str:
        # improves storage size and reduced damage
        pass
