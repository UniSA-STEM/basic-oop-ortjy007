"""
File: Hacker.py
Description: Module to define the Hacker class and Methods part of
the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Hacker:
    """
    Hacker class with the following attributes:
    +name: str
    -expose_level: int
    -security_chip: bool
    -trace_level: int

    And the following methods:
    acquire_rig
    launch_data_spikes
    extract_asset
    encrypt_asset
    decrypt_asset
    store_asset
    retrieve_asset
    scan_inventory

    General functionality:
    _trace levels increase when performing risky actions like launching attacks
    or transferring sensitive assets
    _if trave levels exceeds 5 the hacker becomes exposed and certain actions
    are blocked until levels decrease

    String conversion method included: hackers name, rig name, trace level
    and inventory contents
    """

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__inventory =  # TODO call asset class, core assets as a list
        self.__trace_level = 0
        self.__exposed = False

    def __str__(self):
        print(f'{self.__name}')
        # hackers name, rig name, trace level, inventory contents
        pass

    def acquire_rig(self):
        # print message announcing activation
        pass

    def launch_data_spikes(self):
        # consumes data spikes from their rigs storage
        pass

    def extract_asset(self):
        pass

    def encrypt_asset(self, security_chip):
        pass

    def decrypt_asset(self, security_chip):
        pass

    def store_asset(self):
        # between inventory and rigs storage
        pass

    def retrieve_asset(self):
        # between inventory and rigs storage
        pass

    def scan_inventory(self):
        # by name and returning if found
        pass
