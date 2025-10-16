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
    -name: str
    -description: str
    -encryption=False

   Asset Class level attributes:
    +crypto_token: to acquire or repair rigs (H)
    +hardware_patch: update rigs level & storage (H)
    +data_spikes: check storage, update lists, update damage (R)
    +removable_drive: found in rigs used for extraction (R)
    +security_rig: used to encrypt or decrypt assets (H or R)

    Asset Class methods:
    Setters and Getters for name and encryption instance attributes
    Getter for description
    build_a_description: automatically assigns a description based on the name
    is_asset: to validate if it is an Asset Class

    Properties:
    a_name, a_description, a_encryption
    """

    # Class level attributes
    ASSET_NAMES = ['crypto_token', 'hardware_patch', 'data_spike',
                   'removable_drive', 'security_rig'
                   ]

    # Defining Asset Class, name, description and encryption status.
    def __init__(self, a_name: str, a_encryption=False) -> None:
        self.a_name = a_name
        self.a_encryption = a_encryption

    def __str__(self) -> str:
        return (f'\nName: {self.__a_name}\n'
                f'Description: {self.__a_description}\n'
                f'Encryption: {self.__a_encryption}')

    # Getters for all instance attributes
    def get_a_name(self) -> str:
        """
        Get the name of the asset
        :return: None
        """
        return self.__a_name

    def get_a_description(self) -> str:
        """
        Get the description of the asset
        :return: None
        """
        return self.__a_description

    def get_a_encryption(self) -> bool:
        """
        Get the encryption status of the asset
        :return: None
        """
        return self.__a_encryption

    # Setters
    def set_a_name(self, a_name: str) -> None:
        """
        Validating name against the given Class level asset list
        :param a_name: str
        :return: None
        """
        # print(f'The identified asset names are {Asset.ASSET_NAMES}.')
        self.__a_name = a_name if a_name in Asset.ASSET_NAMES \
            else 'unidentified'
        self.__a_description = self.build_a_description(self.__a_name)

    def set_a_encryption(self, status: bool) -> None:
        """
        Set asset to encrypted or decrypted, if input is invalid reset to
        default value (False)
        :param status: bool
        :return: None
        """
        if isinstance(status, bool):
            self.__a_encryption = status
        else:
            print(f'The encryption status can only be True or False, updating to '
                  f'default status (False)')
            self.__a_encryption = False

    def build_a_description(self, a_name: str) -> str:
        """
        Matching asset name to description, if not found declared 'Unidentified asset'
        :param a_name: str
        :return: self.a_description
        """
        if a_name == 'crypto_token':
            self.__a_description = 'Used to acquire or repair rigs.(H)'
        elif a_name == 'hardware_patch':
            self.__a_description = 'Used to update rigs -level & storage-.(H)'
        elif a_name == 'data_spike':
            self.__a_description = 'Used in battles to damage rigs.(R)'
        elif a_name == 'removable_drive':
            self.__a_description = 'Found in rigs and used for extraction.(R)'
        elif a_name == 'security_rig':
            self.__a_description = 'Used to encrypt or decrypt assets.(H/R)'
        else:
            self.__a_description = 'Unidentified asset.'
        return self.a_description

    def is_asset(self) -> bool:
        """
        Helper to check if object is an Asset
        :return: bool
        """
        return True if (isinstance(self, Asset) and self.__a_name
                        in Asset.ASSET_NAMES) else False

    # Properties for instance attributes
    a_name = property(get_a_name, set_a_name)
    a_description = property(get_a_description)
    a_encryption = property(get_a_encryption, set_a_encryption)


asset1 = Asset('funky')
print(asset1)

asset1.set_a_encryption(True)
asset1.set_a_name('security_rig')
print(asset1)

print()
print(asset1.a_name)
print(asset1.a_description)
print(asset1.a_encryption)

