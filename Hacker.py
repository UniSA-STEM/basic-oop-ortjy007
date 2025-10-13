"""
File: Hacker.py
Description: Module to define the Hacker class and Methods part of
the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    """
    Hacker represents a person (with a cryptic and/or stylish pseudonym) who
    uses computers to gain unauthorized access to data.
    Hacker class with the following attributes:
    +name: str
    -exposed: bool
    -trace_level: int
    -inventory: []

    And the following methods:
    acquire_rig: Rig_name # linked to Hacker?
    launch_data_spikes: target_rig  # same as launch attack?? consumes data
        spike from own storage
    extract_asset: target_rig, asset_names # only if the rig is broken and the
        assets are unsecured (non encrypted) assets (all of them) and consumes
        a movable drive, transfers assets to own storage
    encrypt_asset: asset_name, security_chip # done inside their inventory or
        Rig's storage, check security chip first, update storage. Encrypted
        assets can not be transferred.
    decrypt_asset: asset_name
    store_asset: storage_name # check capacity
    retrieve_asset: storage_name(Rig), inventory(Hacker), asset_name # update
        inventory or Rig storage
    scan_inventory: #identify assents, quantity, status (encrypted/decrypted)

    General functionality:
    _trace levels increase when performing risky actions like launching attacks
    or transferring sensitive assets
    _if trave levels exceeds 5 the hacker becomes exposed and certain actions
    are blocked until levels decrease

    String conversion method included: hackers name, rig name, trace level
    and inventory contents
    The inventory and Rig's storage are different lists
    """

    def __init__(self, name: str, ) -> None:
        self.__name = name
        self.__inventory = []
        self.__trace_level = 0
        self.__exposed = False

    def __str__(self) -> str:
        return f'{self.name}\nRig name:{Asset.get_name}\nInventory:{self.__inventory}'

    # Getters
    def get_name(self) -> str:
        return self.__name

    def get_trace_level(self) -> int:
        return self.__trace_level

    def get_exposed(self) -> bool:
        return self.__exposed

    # Setters
    def set_name(self) -> str:
        return self.__name

    def set_trace_level(self) -> int:
        return self.__trace_level

    def set_exposed(self) -> bool:
        return self.__exposed

    # Properties
    name = property (set_name, get_name)
    trace_level = property (get_trace_level, set_trace_level)
    exposed = property(get_exposed, set_exposed)

    def acquire_rig(self) -> str:
        # print message announcing activation
        pass

    def launch_data_spikes(self) -> str:
        # consumes data spikes from their rigs storage
        pass

    def extract_asset(self) -> str:
        pass

    def encrypt_asset(self, security_chip) -> bool:
        pass

    def decrypt_asset(self, security_chip) -> bool:
        pass

    def store_asset(self) -> list:
        # between inventory and rigs storage
        pass

    def retrieve_asset(self) -> str:
        # between inventory and rigs storage
        pass

    def scan_inventory(self) -> list:
        # by name and returning if found
        pass
