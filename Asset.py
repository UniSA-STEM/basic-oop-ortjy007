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
    Asset class with the following attributes:
    +name: str
    -description: str
    -encrypted=False

    And the following Assets:
    +crypto_token: Rig_name # to acquire or repair rigs (H)
    +hardware_patch: rig_name # update rigs level & storage (H)
    +data_spikes: target_rig # check storage, update lists, update damage (R)
    +removable_drive: target_rig, destination_rig # found in rigs used for extraction (R)
    +security_rig: asset_name # used to encrypt or decrypt assets (H or R)

    ##### Extract to be deleted:
    Assets can be moved between hacker and rig , used in actions or consumed during upgrades
    Representing digital assets can be moved between Hacker's inventory and
    their Rig's storage. Are used in actions or consumed during upgrades.
    """
    ASSETS = []  # wip to include all identified

# Defining Asset Class, name, description and encryption status.

    def __init__(self, name, description) -> None:
        self.__name = name
        self.__description = description
        self.__encrypted = False


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

    def get_encrypted(self) -> bool:
        return self.__encrypted

    # Setters
    def set_name(self, name: str) -> str:
        if type(name) == str:
            self.__name = name
        else:
            print('Invalid name.')
        return self.__name

    def set_description(self, description: str) -> str:
        """
        Asset description validated as a str
        :param description: str
        :return: self.__description
        """
        self.__description = description
        if type(description) == str:
            self.__description = description
        else:
            print('Invalid name.')
        return self.__description

    def set_encrypted(self, status: bool) -> bool:
        """
        Set asset to encrypted or decrypted
        :param status: bool
        :return: self.__encrypted
        """
        self.__encrypted = status
        return self.__encrypted

    # Properties
    name = property (get_name, set_name)
    description = property (get_description, set_description)
    encrypted = property(get_encrypted)