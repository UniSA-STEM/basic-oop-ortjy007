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

# Testing Scenarios

# Generating three hackers and test Assets, Rig's and Hacker's methods

faye_v = Hacker('faye', 'f1')
spike_s = Hacker('spike', 's1')
jet_b = Hacker('jet', 'j1')

# 1 Rig's methods
# Generating random assets

asset1 = faye_v.rig.generate_asset()
asset2 = faye_v.rig.generate_asset()

asset3 = spike_s.rig.generate_asset()
asset4 = spike_s.rig.generate_asset()

asset5= spike_s.rig.generate_asset()
asset6 = spike_s.rig.generate_asset()

# Storing assets in Rig
print('\nfaye_v storing assets')
faye_v.rig.storing_assets(asset1)


print('\nspike_s storing assets')
spike_s.rig.storing_assets(asset3)
spike_s.rig.storing_assets(asset4)

print('\njet_b storing assets')
jet_b.rig.storing_assets(asset5)
jet_b.rig.storing_assets(asset6)

# Releasing assets
print('\nfaye_v releasing assets')
r_asset1 = faye_v.rig.releasing_asset(asset1)
r_asset2 = faye_v.rig.releasing_asset(asset2)

print('\nspike_s releasing assets')
r_asset3 = spike_s.rig.releasing_asset(asset3)
r_asset4 = spike_s.rig.releasing_asset(asset4)

print('\njet_b releasing all assets')
r_assets56 = []
r_assets56 = jet_b.rig.releasing_all_assets()

# Upgrading rigs (generating and storing hardware patches for this purpose)
print()
asset7 = Asset('hardware_patch')
spike_s.rig.storing_assets(asset7)
print()
faye_v.rig.storing_assets(asset7)

print('\nspike_s upgrading his rig')
spike_s.rig.upgrading(asset7)

print('\nfaye_v upgrading her rig')
faye_v.rig.upgrading(asset7)

print('\nfaye_v upgrading her rig again')
faye_v.rig.upgrading(asset7)

# Taking hits... without the need of data spikes as these will be deducted
# at the hackers end....
print("\nfaye_v's rig taking hits until destruction...")
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
faye_v.rig.taking_hits()
print(faye_v.rig)

# Repairing the damaged rig with a purpose generated crypto token and
# storing it in her rig
print()
asset8 = Asset('crypto_token')
faye_v.rig.storing_assets(asset8)
print("\nfaye_v repairing her rig")
faye_v.rig.repairing(asset8)
print(faye_v.rig)



"""def main():


if __name__ == "__main__":
    main()"""