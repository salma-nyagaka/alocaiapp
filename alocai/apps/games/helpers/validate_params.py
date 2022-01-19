from rest_framework.serializers import ValidationError

from ..models import Game
from ....helpers.serialization_errors import error_dict


def validate_params(params):
    """
    Function that validates
    params
    Args:
        params(dict): request parameters
    """
    final_data = []

    # check if key or value has been provided
    if (not params) or ("pen_drive_space" not in params):
        raise ValidationError(
            error_dict["required"].format("pen_drive_space in params")
        )
    if params["pen_drive_space"] == "":
        raise ValidationError(
            error_dict["empty"].format("pen_drive_space value in params")
        )
    if int(params["pen_drive_space"]) < 1:
        raise ValidationError(
            error_dict["positive"].format("pen_drive_space value in params")
        )

    # If key has been provided then fetch records
    else:
        pen_drive_space = params["pen_drive_space"]
        initial_dict = {}
        db_objects = Game.objects.only("space").order_by("space")

        # Create an array from containing the id
        # as a key and space as the value
        for object in db_objects:
            final_data.append({"id": object.id, "space": object.space})

        response_data = compute_space(final_data, pen_drive_space)

    return response_data

total_space = ''
empty_space = ''

def compute_space(data, space):
    """Compute space from the pen drive
    from the list of objects"""

    # Add space values to a list
    if len(data) == 0:
        raise ValidationError(error_dict["does_not_exist"].format(
            "Games records"))
    else:

        # get the game space values that can fit
        # to the pen drive
        sum_of_space = 0
        items = []
        global empty_space
        global total_space 
        for db_data in data:
            sum_of_space = sum_of_space + db_data["space"]
            if sum_of_space < int(space):
                items.append(Game.objects.get(id=db_data['id']))
        
                empty_space = int(space) - sum_of_space
                total_space = sum_of_space
        return items, total_space, empty_space
