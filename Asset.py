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
    Asset Class representing digital assets.
    Class level attributes:
    -ENCRYPTED: bool
    -ASSET_NAMES: list
    Instance level attributes:
    -name: str
    -encrypted: bool
    -description: str
    Methods w/decorators:
    +name @property getter + setter
    +encrypted @property getter + setter
    +description @property getter + setter
    """

    # Class level attributes
    ENCRYPTED = False  # set as default for all instances
    ASSET_NAMES = ['crypto_token', 'hardware_patch', 'data_spike',
                   'removable_drive', 'security_chip'
                   ]  # current list of assets

    def __init__(self, name: str, description=None):
        """
        Constructor method, the name attribute serves as both name and
        to select the corresponding description.
        :param name: str
        """
        self.name = name
        self.encrypted = Asset.ENCRYPTED
        self.description = description

    def __str__(self):
        """
        Values and format as requested in the specification.
        :return: str
        """
        if self.encrypted:
            return f'{self.__name}: {self.__description} [Encrypted]'
        else:
            return f'{self.__name}: {self.__description}'

    @property
    def name(self) -> str:
        """
        Name function w/ property decorator as getter.
        :return: str
        """
        return self.__name

    @name.setter
    def name(self, a_name: str) -> None:
        """
        Name method with setter decorator validating name against
        the list of given assets. If invalid input is given a default
        name is given to the asset.
        :param a_name: str
        :return: None
        """
        if isinstance(a_name, str) and a_name in Asset.ASSET_NAMES:
            print(f'{a_name} asset created.')
            self.__name = a_name
        else:
            print('Invalid input, default name used')
            self.__name = 'default_asset'

    @property
    def encrypted(self) -> bool:
        """
        Encrypted function w/ property decorator as getter.
        :return: bool
        """
        return self.__encrypted

    @encrypted.setter
    def encrypted(self, enc=False) -> None:
        """
        Encrypted method validated as boolean. If invalid input is
        given a default the False value is given to the asset.
        :param enc: bool
        :return: None
        """
        if isinstance(enc, bool):
            self.__encrypted = enc
        else:
            print('Invalid input, default False value used.')
            self.__encrypted = False

    @property
    def description(self) -> str:
        """
        Description function w/ property decorator as getter.
        :return: str
        """
        return self.__description

    @description.setter
    def description(self, name: str) -> None:
        """
        Matching asset name to description from specification document,
        if the name does not match is declared as an 'Unidentified asset'.
        :param name: str
        :return: None
        """
        if self.__name == 'crypto_token':
            self.__description = 'Used to acquire or repair rigs.(H)'
        elif self.__name == 'hardware_patch':
            self.__description = 'Used to update rigs -level & storage-.(H)'
        elif self.__name == 'data_spike':
            self.__description = 'Used in battles to damage rigs.(R)'
        elif self.__name == 'removable_drive':
            self.__description = 'Found in rigs and used for extraction.(R)'
        elif self.__name == 'security_chip':
            self.__description = 'Used to encrypt or decrypt assets.(H/R)'
        else:
            self.__description = 'Unidentified asset.'

    def __eq__(self, other):
        """
        Testing for Asset equality
        :param other: instance
        :return: str
        """
        if isinstance(other, Asset):
            return self.__name == other.__name
        else:
            return 'Not equal Assets'
