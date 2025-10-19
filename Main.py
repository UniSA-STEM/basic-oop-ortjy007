"""
File: main.py
Description: Driver for the Hacker-Rig-Asset combo.
Author: Jorge Ortega
ID: 110482203
Username: ortjy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Hacker import Hacker
from Rig import Rig
from Asset import Asset

"""
Final test for all three modules, the Asset module is being tested
implicitly by running the other modules.

The Rig's methods tested (in that order):
+ generate_asset 
+ storing_assets
+ releasing_asset
+ releasing_all_assets
+ upgrading
+ taking_hits
+ repairing

The Hacker's methods tested (in that order):
+ generate_asset (R)
+ storing_assets
+ scanning_inventory
+ encrypting_decrypting_asset
+ retrieving_assets
+ launching_data_spikes
+ extracting_assets
+ exposing

The recycling method is used throughout the other methods.
Note that the acquiring_rig method runs automatically upon initiation.
"""

def rig_test() -> None:
    """
    First test, Rigs
    :return: None
    """
    # Generating three hackers and testing the Rig's methods
    print("Generating three hackers and testing the Rig's methods first")
    faye_v = Hacker('faye', 'f1')
    spike_s = Hacker('spike', 's1')
    jet_b = Hacker('jet', 'j1')

    # 1 Rig's methods
    # Generating random assets
    print('1 Rig methods:\nGenerating random assets from different rigs:')
    print("Assets generated through faye_v's rig:")
    asset1 = faye_v.rig.generate_asset()
    asset2 = faye_v.rig.generate_asset()

    print("\nAssets generated through spike_s's rig:")
    asset3 = spike_s.rig.generate_asset()
    asset4 = spike_s.rig.generate_asset()

    print("\nAssets generated through jet_b's rig:")
    asset5 = jet_b.rig.generate_asset()
    asset6 = jet_b.rig.generate_asset()

    # Storing assets in Rig
    print('\nfaye_v storing assets:')
    faye_v.rig.storing_assets(asset1)
    faye_v.rig.storing_assets(asset2)

    print('\nspike_s storing assets:')
    spike_s.rig.storing_assets(asset3)
    spike_s.rig.storing_assets(asset4)

    print('\njet_b storing assets:')
    jet_b.rig.storing_assets(asset5)
    jet_b.rig.storing_assets(asset6)

    # Releasing assets
    print('\nfaye_v releasing assets:')
    r_asset1 = faye_v.rig.releasing_asset(asset1)
    r_asset2 = faye_v.rig.releasing_asset(asset2)

    print('\nspike_s releasing assets:')
    r_asset3 = spike_s.rig.releasing_asset(asset3)
    r_asset4 = spike_s.rig.releasing_asset(asset4)

    print('\njet_b releasing all assets:')
    r_assets56 = []
    r_assets56 = jet_b.rig.releasing_all_assets()

    # Upgrading rigs (generating and storing hardware patches for this purpose)
    print()
    print('Upgrading rigs (generating and storing hardware '
          'patches for this purpose:')
    asset7 = Asset('hardware_patch')
    spike_s.rig.storing_assets(asset7)

    print('\nspike_s upgrading his rig:')
    spike_s.rig.upgrading(asset7)

    print('\nfaye_v upgrading her rig:')
    faye_v.rig.upgrading(asset7)

    print('\nfaye_v upgrading her rig again:')
    faye_v.rig.upgrading(asset7)

    # Taking hits... without the need of data spikes as these will be deducted
    # at the hackers end....
    print("\nfaye_v's rig taking hits until destruction...")
    faye_v.rig.taking_hits()
    faye_v.rig.taking_hits()  #
    faye_v.rig.taking_hits()
    faye_v.rig.taking_hits()
    faye_v.rig.taking_hits()
    faye_v.rig.taking_hits()
    faye_v.rig.taking_hits()
    print("\nfaye_v's rig status after attack:")
    print(faye_v.rig)

    # Repairing the damaged rig with a purpose generated crypto token and
    # storing it in her rig
    print('Creating and storing a crypto_token for faye-v:')
    asset8 = Asset('crypto_token')
    faye_v.rig.storing_assets(asset8)
    print("\nfaye_v repairing her rig:")
    faye_v.rig.repairing(asset8)
    print("\nfaye_v's rig status after repairs:")
    print(faye_v.rig)

def hacker_test() -> None:
    """
    Second test, Hackers
    :return: None
    """
    # Generating three hackers and testing the Rig's methods first
    print("Generating three hackers and testing the Rig's methods first")
    ed_w = Hacker('ed', 'e1')
    ain = Hacker('ain', 'a1')
    julia = Hacker('julia', 'j1')

    # Generating random assets
    print('1 Hackers methods:\nGenerating random assets from different rigs:')
    print("Assets generated through ed_w's rig:")
    asset10 = ed_w.rig.generate_asset()
    asset11 = ed_w.rig.generate_asset()
    asset12 = ed_w.rig.generate_asset()

    print("Assets generated through ain's rig:")
    asset13 = ain.rig.generate_asset()
    asset14 = ain.rig.generate_asset()
    asset15 = ain.rig.generate_asset()

    print("Assets generated through julia's rig:")
    asset16 = julia.rig.generate_asset()
    asset17 = julia.rig.generate_asset()
    asset18 = julia.rig.generate_asset()

    # Storing assets in the inventory
    print("Storing assets in the Hackers inventory:")
    print('\ned_w storing assets:')
    ed_w.storing_asset(asset10)
    ed_w.storing_asset(asset11)
    ed_w.storing_asset(asset12)

    print('\nain storing assets:')
    ain.storing_asset(asset13)
    ain.storing_asset(asset14)
    ain.storing_asset(asset15)

    print('\njulia storing assets:')
    julia.storing_asset(asset16)
    julia.storing_asset(asset17)
    julia.storing_asset(asset18)

    # Encrypting and decrypting assets
    print("Generating security chips and using them to encrypt "
          "and decrypt assets in storage:")
    asset20 = Asset('security_chip')
    ed_w.storing_asset(asset13)
    ed_w.storing_asset(asset14)
    ed_w.storing_asset(asset15)
    ed_w.storing_asset(asset16)
    ed_w.storing_asset(asset17)
    ed_w.storing_asset(asset18)

    print('\ned_w scanning inventory:')
    ed_w.scanning_inventory('hardware_patch')
    ed_w.scanning_inventory('removable_drive')
    ed_w.scanning_inventory('crypto_token')

    print('\ned_w encrypting assets:')
    ed_w.encrypting_decrypting_asset(asset14)

    print('\ned_w decrypting assets:')
    ed_w.encrypting_decrypting_asset(asset14)

    print('\ned_w encrypting assets:')
    ed_w.encrypting_decrypting_asset(asset17)

    print('\ned_w decrypting assets:')
    ed_w.encrypting_decrypting_asset(asset17)

    print('\nain launching data spikes on ed_w:')
    ain.launching_data_spikes(ed_w.rig)
    ain.launching_data_spikes(ed_w.rig)
    ain.launching_data_spikes(ed_w.rig)
    ain.launching_data_spikes(ed_w.rig)
    ain.launching_data_spikes(ed_w.rig)

    print('\nPrinting ed_w inventory (to be raided):')
    print(ed_w.inventory)

    print('\nain extracting unencrypted assets from ed_w:')
    ain.extracting_assets(ed_w.rig)

    print('\nain checking his exposure:')
    print(ain.exposing())

def edge_tests() -> None:
    pass

def main():
    pass

if __name__ == "__main__":
    main()
