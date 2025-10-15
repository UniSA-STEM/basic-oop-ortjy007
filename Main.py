"""
File: main.py
Description: Driver for the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

#from Hacker import Hacker
import Rig
import Asset


"""
sample scenarios to test
"""
def main():

    #h1 = Hacker('h1')
    #print(h1)

    r1 = Rig.Rig('r1')
    print(r1)

    print(r1.get_damage)
    print(r1.get_name)
    print(r1.get_broken)
    print(r1.get_level)


    asset1 = Asset.Asset('crypto_token')
    asset2 = Asset.Asset('hardware_patch')
    print('1',asset1.get_name)
    print('2',asset1.get_encrypted)
    print('3', asset1.get_description)

    print(f'{asset1.is_asset()}')
    print(f'{asset2.is_asset()}')

    print(type(asset1))
    r1.store_asset(asset1)
    r1.store_asset(asset2)
    print(r1.get_storage[0].get_name, r1.get_storage[1].get_name )


if __name__ == "__main__":
    main()