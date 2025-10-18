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
import Rig
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
    Acquiring_rig: Using the Rig module to acquire a Rig after
    cyber token validation.
    Scanning_inventory: searches for a specific asset and returns True
    if found.
    Storing_asset: storage asset in inventory after validation.
    Retrieving_asset: checks the inventory and if found retrieves a
    specific asset.
    Extracting_assets: extracting assets from target rig transferred to
    Hackers inventory

    Encrypting_asset: asset_name, security_chip # done inside their inventory or
    Rig's storage, check security chip first, update storage. Encrypted
    assets can not be transferred.
    Decrypting_asset: asset_name
    Launching_data_spikes: target_rig  # same as launch attack?? consumes data
    spike from own storage
    """

    USED_ASSETS = []  # used for recycling :)

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
        self.inventory = [Asset.Asset('crypto_token')]
        self.rig = rig

        # Retrieving initial crypto token from inventory
        # token_for_rig = Hacker.retrieving_asset(Hacker,'crypto_token')

        # Acquiring a Rig as part of the constructor as instructed in brief
        # Hacker.acquiring_rig(Hacker, 'r2', token_for_rig)

    def __str__(self) -> str:
        return f'{self.__name}\nRig name:{Asset.Asset.name}\nInventory:{self.__inventory}'

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
    def rig(self) -> Rig:
        """rig property"""
        return self.__rig

    @rig.setter
    def rig(self, h_rig: Rig) -> None:
        self.__rig = h_rig

    # Class Methods
    def acquiring_rig(self, r_name: str) -> None:
        """
        Rig acquisition for Hacker's use following the cyber token asset validation
        if stored in inventory. Check if there is no active rig, token gets deleted
        from inventory and recycled.
        :param r_name: str
        :return: None
        """
        if not self.__rig:
            if Hacker.scanning_inventory('crypto_token'):
                Hacker.USED_ASSETS.append(Hacker.retrieving_asset('crypto_token'))
                self.__inventory.remove(Asset.Asset.name == 'crypto_token')
                self.__rig = Rig.Rig(r_name)
                print(f'{r_name} Rig has been acquired and is operational.')
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

    def storing_asset(self, asset: Asset) -> None:
        """
        Storing assets in the Hacker's inventory after validation
        and printing the revised contents of inventory w/ decryption
        status.
        :param asset: Asset
        :return:
        """
        if isinstance(asset, Asset.Asset) and asset.encrypted != True:
            self.__inventory.append(asset)

            # Extracting the names and encryption status of the assets
            # into a temp list
            tmp_list = []

            for item in self.__inventory:
                tmp_list.append(item.name)
                tmp_list.append(item.encrypted)
                tmp_list.append('/')
            print(f'Stored assets:', *tmp_list)

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
        if Hacker.scanning_inventory(asset_name):
            r_asset = self.__inventory[self.__inventory.index(asset_name)]
            del self.__inventory[self.__inventory.index(asset_name)]
        return r_asset

    def extracting_assets(self, target: str) -> None:
        """
        Extracting assets from a target rig. Validating if we have a Rig,
        if Hacker is exposed and if it is a valid Hacker.
        :param target: Hacker
        :return: None
        """
        # Temp list to hold the names of extracted asets
        e_asset = []

        if self.__rig is None:
            print('A Rig is needed to extract assets.')
        elif self.__exposed:
            print("Your can't extract assets while exposed.")
        elif isinstance(target, Hacker):
            if target.Rig.Rig.broken:
                for item in target.Rig.Rig.storage:
                    if not item.encrypted:
                        self.__inventory.append(item)
                        e_asset.append(item.name)
                        target.Rig.Rig.storage.remove(item)
                print(f'The following assets were extracted {e_asset}.')
            else:
                print(f'No items can be extracted unless the target Rig '
                      f'is broken')
        else:
            print('Extracting assets unsuccessful.')

    def encrypting_asset(self, security_chip) -> bool:
        pass

    def decrypting_asset(self, security_chip) -> bool:
        pass

    def launching_data_spikes(self) -> str:
        # consumes data spikes from their rigs storage
        pass
