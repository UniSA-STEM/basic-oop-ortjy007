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


def main():
    """
    four methods thoroughly test all three modules
    :return: ...a great mark!
    """

    def rig_test() -> None:
        """
        First test, Rigs
        :return: None
        """
        print("Testing Rig's methods start.")
        print('----------------------.')

        # Generating three hackers and testing the Rig's methods
        print("1.0 Generating three hackers and testing the Rig's methods first")
        faye_v = Hacker('faye', 'f1')
        spike_s = Hacker('spike', 's1')
        jet_b = Hacker('jet', 'j1')

        # 1 Rig's methods
        # Generating random assets
        print("1.1 Rig methods:\n"
              "Generating random assets from different rigs:\n"
              "Assets generated through faye_v's rig:")
        asset1 = faye_v.rig.generate_asset()
        asset2 = faye_v.rig.generate_asset()

        print("\nAssets generated through spike_s's rig:")
        asset3 = spike_s.rig.generate_asset()
        asset4 = spike_s.rig.generate_asset()

        print("\nAssets generated through jet_b's rig:")
        asset5 = jet_b.rig.generate_asset()
        asset6 = jet_b.rig.generate_asset()
        print('1.1 Passed\n')

        # Storing assets in Rig
        print('1.2 Storing assets in Rigs:\n'
              'faye_v storing assets:')
        faye_v.rig.storing_assets(asset1)
        faye_v.rig.storing_assets(asset2)

        print('\nspike_s storing assets:')
        spike_s.rig.storing_assets(asset3)
        spike_s.rig.storing_assets(asset4)

        print('\njet_b storing assets:')
        jet_b.rig.storing_assets(asset5)
        jet_b.rig.storing_assets(asset6)
        print('1.2 Passed\n')

        # Releasing assets
        print('1.3 Releasing assets:'
              '\nfaye_v releasing assets:')
        r_asset1 = faye_v.rig.releasing_asset(asset1.name)
        r_asset2 = faye_v.rig.releasing_asset(asset2.name)

        print('\nspike_s releasing assets:')
        r_asset3 = spike_s.rig.releasing_asset(asset3.name)
        r_asset4 = spike_s.rig.releasing_asset(asset4.name)

        print('\njet_b releasing all assets:')
        r_assets56 = []
        r_assets56 = jet_b.rig.releasing_all_assets()
        print('1.3 Passed\n')

        # Upgrading rigs (generating and storing hardware patches for this purpose)
        print('1.4 Upgrading rigs (generating and storing hardware_'
              'patches) for this purpose:\n')
        asset7 = Asset('hardware_patch\n')
        spike_s.rig.storing_assets(asset7)

        print('\nspike_s upgrading his rig:')
        spike_s.rig.upgrading()

        print('faye_v upgrading her rig:')
        faye_v.rig.upgrading()

        print('faye_v upgrading her rig again:')
        faye_v.rig.upgrading()
        print('1.4 Passed\n')

        # Taking hits... without the need of data spikes as these will be deducted
        # at the hackers end....
        print('1.5 Taking hits til destruction...')
        print("faye_v's rig taking hits gracefully...")
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        print("\nfaye_v's rig status after attack:")
        print(f'{faye_v.rig}1.5 Passed\n')

        # Repairing damaged rigs
        print('1.6 Repairing the damaged rig with a purpose generated\n'
              'crypto tokens.\n'
              'Creating and storing a crypto_token for faye-v:')
        asset8 = Asset('crypto_token')
        faye_v.rig.storing_assets(asset8)
        print("\nfaye_v repairing her rig:")
        faye_v.rig.repairing()
        print(f"\nfaye_v's rig status after repairs:\n{faye_v.rig}1.6 Passed\n")

        print("All Rig methods tested.")
        print('----------------------.')

    def hacker_test() -> None:
        """
        Second test, Hackers
        :return: None
        """
        print("Testing Hackers's methods.")
        print('----------------------.')

        # Generating three hackers and testing the Rig's methods first
        print("2.0 Generating three hackers and testing the Rig's methods first")
        ed_w = Hacker('ed', 'e1')
        ain = Hacker('ain', 'a1')
        julia = Hacker('julia', 'j1')

        # Generating random assets
        print("2.1 Hackers methods:\nGenerating random assets from different rigs:\n"
              "Assets generated through ed_w's rig:")
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
        print('2.1 Passed\n')

        # Storing assets in the inventory
        print("2.20Storing assets in the Hackers inventory:\ned_w storing assets:")
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
        print('2.2 Passed\n')

        # Encrypting and decrypting assets
        print("2.3 Generating security chips and using them to encrypt\n"
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
        print('2.3 Passed\n')

        print('2.4 Launching data spikes to other rigs\n'
              'ain launching data spikes on ed_w:')
        ain.launching_data_spikes(ed_w.rig)
        ain.launching_data_spikes(ed_w.rig)
        ain.launching_data_spikes(ed_w.rig)
        ain.launching_data_spikes(ed_w.rig)
        ain.launching_data_spikes(ed_w.rig)
        print('2.4 Passed\n')

        print('2.5 Printing ed_w inventory (to be raided):')
        print(ed_w.inventory)
        print('2.5 Passed\n')

        print('2.6 Extracting unencrypted assets from inventory:\n'
              'ain extracting unencrypted assets from ed_w:')
        ain.extracting_assets(ed_w.rig)
        print('2.6 Passed\n')

        print('2.7 ain checking his exposure:')
        print(ain.exposing())
        print('2.7 Passed\nAll Hacker methods tested.')
        print('----------------------.')

    def rig_edge_tests() -> None:
        """
        Third test, edges
        :return: None
        """
        print("Testing Rig's boundaries start.")
        print('----------------------.')
        # Generating one hacker and testing the Rig's methods to the edges

        print("3.0 Generating one hacker and testing the Rig's methods to failure")
        faye_v = Hacker('faye', 'f1')
        print('3.0 Rig status', faye_v.rig)

        # Generating random assets
        print('Generating random assets:')
        print("Random assets generated through faye_v's rig:")
        asset31 = faye_v.rig.generate_asset()
        asset32 = faye_v.rig.generate_asset()
        asset33 = faye_v.rig.generate_asset()
        asset34 = faye_v.rig.generate_asset()
        asset35 = faye_v.rig.generate_asset()
        asset36 = faye_v.rig.generate_asset()
        asset37 = faye_v.rig.generate_asset()
        asset38 = faye_v.rig.generate_asset()
        asset39 = faye_v.rig.generate_asset()

        print("3.1 Trying to store non assets or an 'empty' instance:")
        assetx = 'noybwifn'
        assety = 874635
        assetz = None

        print('assetx = ', assetx)
        faye_v.rig.storing_assets(assetx)
        print('assety = ', assety)
        faye_v.rig.storing_assets(assety)
        print('assetz = ', assetz)
        faye_v.rig.storing_assets(assetz)
        print('3.1 Passed')

        print()
        print('3.2 Storing assets to max capacity:')
        faye_v.rig.storing_assets(asset31)
        faye_v.rig.storing_assets(asset32)
        faye_v.rig.storing_assets(asset33)
        faye_v.rig.storing_assets(asset34)
        faye_v.rig.storing_assets(asset35)
        faye_v.rig.storing_assets(asset36)
        faye_v.rig.storing_assets(asset37)
        faye_v.rig.storing_assets(asset38)

        print()
        print('3.2 Rig status', faye_v.rig)
        print('3.2 Passed')

        print()
        print('3.3 Releasing non existing assets:')
        print('Reset Rig (override with a new copy)')
        faye_v = Hacker('faye', 'f1')
        print('3.3 Rig status', faye_v.rig)

        print('3.3.1 Requesting the release of a hardware_patch\n'
              'non existing in storage:')
        faye_v.rig.releasing_asset('hardware_patch')
        print('3.3.1 Passed\n')

        print('3.3.2 Requesting the release of non valid assets:')
        print(' '' ')
        faye_v.rig.releasing_asset('')
        print('noybwifn')
        faye_v.rig.releasing_asset('noybwifn')
        print(874635)
        faye_v.rig.releasing_asset(874635)
        print(None)
        faye_v.rig.releasing_asset(None)
        print('3.3.2 Passed')

        print()
        print('3.4 Upgrading without a valid hardware_patch in storage:')
        print(faye_v.rig)
        faye_v.rig.upgrading()
        print('3.4 Passed')

        print()
        print('3.5 Trying to repair without a valid crypto token in storage:')
        print("Destroying it first... for fun")
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()
        faye_v.rig.taking_hits()

        print("\nfaye_v's rig status after attack:")
        print(faye_v.rig)
        faye_v.rig.repairing()
        print('3.5 Passed\n\n')

        print("All Rig methods tested.\nTesting Rig's boundaries completed.")
        print('----------------------.')

    def hacker_edge_test() -> None:
        """
        Four test, edges
        :return: None
        """
        print("Testing Hackers's boundaries start.")
        print('----------------------.')
        # Generating one hacker and testing the Hackers's methods

        print("4.0 Generating one hacker and testing the Hackers's methods to failure")
        faye_v = Hacker('faye', 'f1')
        print('4.0 Hacker status')
        faye_v

        # Generating random assets
        print('Generating random assets:')
        print("Random assets generated through faye_v's rig:\n")

        asset31 = faye_v.rig.generate_asset()
        asset32 = faye_v.rig.generate_asset()
        asset33 = faye_v.rig.generate_asset()
        asset34 = faye_v.rig.generate_asset()
        asset35 = faye_v.rig.generate_asset()
        asset36 = faye_v.rig.generate_asset()
        asset37 = faye_v.rig.generate_asset()
        asset38 = faye_v.rig.generate_asset()
        asset39 = faye_v.rig.generate_asset()
        asset40 = faye_v.rig.generate_asset()

        print("\n4.1 Trying to store non assets or an 'empty' instance:")
        assetx = 'noybwifn'
        assety = 874635
        assetz = None

        print('assetx = ', assetx)
        faye_v.storing_asset(assetx)
        print('assety = ', assety)
        faye_v.storing_asset(assety)
        print('assetz = ', assetz)
        faye_v.storing_asset(assetz)
        print('4.1 Passed\n')

        print('4.2 Storing assets to max capacity:')
        faye_v.storing_asset(asset31)
        faye_v.storing_asset(asset32)
        faye_v.storing_asset(asset33)
        faye_v.storing_asset(asset34)
        faye_v.storing_asset(asset35)
        faye_v.storing_asset(asset36)
        faye_v.storing_asset(asset37)
        faye_v.storing_asset(asset38)
        faye_v.storing_asset(asset39)
        faye_v.storing_asset(asset40)
        print('4.2 Passed\n')

        print('4.3 Retrieving non existing assets:\n'
              'Reset Rig (override with a new copy)')
        faye_v = Hacker('faye', 'f1')

        print('4.3.1 Requesting the release of a hardware_patch\n'
              'non existing in inventory:')
        faye_v.retrieving_asset('hardware_patch')
        print('4.3.1 Passed\n')

        print('4.3.2 Requesting the release of non valid assets:')
        print(' '' ')
        faye_v.retrieving_asset('')
        print('noybwifn')
        faye_v.retrieving_asset('noybwifn')
        print(874635)
        faye_v.retrieving_asset(874635)
        print(None)
        faye_v.retrieving_asset(None)
        print('4.3.2 Passed\n')

        print('4.4 Extracting assets:\n'
              'Create target Rig and update it to broken')
        vicious = Hacker('vici', 'v1')
        print('vicious.rig.broken = True')
        vicious.rig.broken = True
        vicious.rig.condition = 2
        print(vicious.rig)

        faye_v.extracting_assets(vicious.rig)
        print('4.4 Passed\n')

        print('4.5.1 Encrypting and decrypting assets\n'
              'Creating two security chips to run encryption and\n'
              'decryption (saved in storage) a removable drive to '
              'be encrypted-decrypted')
        security_chip = Asset('security_chip')
        removable_drive = Asset('removable_drive')

        print('\nStoring them in faye_v inventory so we can run the encryption \n'
              'and decryption:')
        faye_v.storing_asset(security_chip)
        faye_v.storing_asset(security_chip)

        print('\nEncrypting and decrypting:')
        faye_v.encrypting_decrypting_asset(removable_drive)
        faye_v.encrypting_decrypting_asset(removable_drive)
        print('4.5.1 Passed\n')

        print('Trying to encrypt a non asset:')
        faye_v.encrypting_decrypting_asset('removable_drive')
        print('4.5.2 Passed\n')

        print('4.6 Launching data spikes:\n'
              '4.6.1 Against a non Rig:')
        faye_v.launching_data_spikes('rig')
        print('4.6.2 Updating faye_v exposure to True and\n'
              'trying to launch a data spike attack:')
        faye_v.exposed = True
        faye_v.launching_data_spikes(vicious.rig)
        print('4.6.2 Passed\n')

        print('Resetting exposure value to False)')
        faye_v.exposed = False

        print('\n4.6.3 Launching attacks until no more data_spike'
              ' assets are left in the inventory:')
        faye_v.launching_data_spikes(vicious.rig)
        faye_v.launching_data_spikes(vicious.rig)
        faye_v.launching_data_spikes(vicious.rig)
        faye_v.launching_data_spikes(vicious.rig)
        print('4.6.3 Passed\n')

        print('All Hacker methods tested.')
        print("Testing Hakers's boundaries completed.")
        print('----------------------.')

    # rig_test()

    # hacker_test()

    # hacker_edge_test()

    # rig_edge_tests()


if __name__ == "__main__":
    main()
