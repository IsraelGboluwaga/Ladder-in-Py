'''
From oppia's space project
12/06/2017
'''

# Lifting strength of a single Gyro in kilograms.
GYRO_LIFT_STRENGTH = 500

# This dictionary maps equipment identifiers to their weight in kilograms.
EQUIPMENT_WEIGHTS = {
    'major_water_pipe': 600,
    'major_wall_panel': 1750,
    'minor_water_pipe': 100,
    'minor_wall_panel': 300,
    'agricultural_canister': 80,
    'research_module': 400,
    'solar_panel': 225
}


# Example equipment containers a Gyro or team of Gyros will need to
# carry on a mission. These lists can serve as input to the
# is_container_liftable_solo function below.
container_1 = ['minor_water_pipe', 'minor_water_pipe', 'minor_water_pipe',
  'minor_water_pipe']
container_2 = ['solar_panel', 'solar_panel', 'solar_panel']
container_3 = ['research_module', 'agricultural_canister']

def is_equipment_liftable_solo(equipment_identifier):
    """
    Arguments:
    - equipment_identifier is a string from EQUIPMENT_WEIGHTS.
      Examples: 'solar_panel' or 'major_wall_panel'
    """
    return EQUIPMENT_WEIGHTS[equipment_identifier] <= GYRO_LIFT_STRENGTH

# Please review this function and simplify the return statement to a single
# line using the same pattern used in the is_equipment_liftable_solo function.
# Prefer simplicity when possible.

def is_container_liftable_solo(equipment_list):
    """Calculates the total weight of an equipment_list and returns True if a
      Gyro is able to lift a container of this equipment solo. Otherwise
      returns False.

    Arguments:
    - equipment_list: a list of equipment_identifier strings."""

    total_weight = 0
    for equipment_id in equipment_list:
        # Add the weight of each equipment_id to the total.
        total_weight += EQUIPMENT_WEIGHTS[equipment_id]

    ## YOUR WORK HERE!
    ## Please simplify the next 4 lines to a single line.
    return total_weight <= GYRO_LIFT_STRENGTH


## When coding in teams of developers you'll sometimes see TODOs where
## code is incomplete or has room for improvement. A good TODO includes
## an owner's name. Couple examples below.
def request_assistance(package_identifier):
    """Gyro requests assistance lifting the given package."""
    # TODO(sarahchen): implement using radio communications with the Gyro's
    # supervising Maverick. Currently outputs to console for verification.
    print "Squad lead: please assign support lifting %s" % package_identifier

def move_package_to_location(package_identifier, location):
    # TODO(sarahchen): implement.
    print "Moving %s to %s" % (package_identifier, location)

# These lines verify is_container_liftable_solo works accurately.
assert is_container_liftable_solo(container_1) == True
assert is_container_liftable_solo(container_2) == False
assert is_container_liftable_solo(container_3) == True
