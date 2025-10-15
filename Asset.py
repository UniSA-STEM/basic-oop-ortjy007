"""
File: Asset.py
Description: Module to define the Asset class and Methods part of
the Into the Grid OOP Basic Programming assessment COMP 1048 2025P6.
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

    The following are identified Assets, no methods except getters and setters:

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
    ASSETS = []  # WIP to include all identified
    TYPES_ = []  # WIP to include all types_

    # Defining Asset Class, name, description and encryption status.

    def __init__(self, type_) -> None:
        self.__type_ = type_

        Asset.TYPES_ = ['crypto_token', 'hardware_patch', 'data_spikes', 'removable_drive', 'security_rig']

        if type_ == 'crypto_token':
            self.__description = 'Used to acquire or repair rigs.(H)'
        elif type_ == 'hardware_patch':
            self.__description = 'Used to update rigs -level & storage-.(H)'
        elif type_ == 'data_spikes':
            self.__description = 'Used in battles to damage rigs.(R)'
        elif type_ == 'removable_drive':
            self.__description = 'Found in rigs and used for extraction.(R)'
        elif type_ == 'security_rig':
            self.__description = 'Used to encrypt or decrypt assets.(H/R)'
        else:
            self.__description = 'Unidentified asset.'

        self.__name = type_ if type_ in Asset.TYPES_ else 'unidentified'
        self.__encrypted = False

    def __str__(self) -> str:
        return (f'\nType: {self.__name}\n'
                f'Description: {self.__description}\n'
                f'Encrypted: {self.__encrypted}')

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_encrypted(self) -> bool:
        return self.__encrypted

    # Setters
    def set_encrypted(self, status: bool) -> bool:
        """
        Set asset to encrypted or decrypted
        :param status: bool
        :return: self.__encrypted
        """
        self.__encrypted = status
        return self.__encrypted

    # Properties
    name = property(get_name)
    description = property(get_description)
    encrypted = property(get_encrypted)
