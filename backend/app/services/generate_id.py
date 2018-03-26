from random import choice
import string
from uuid import uuid4


def generate_user_invcode():
    """
    Generates invitation code for user account
    :return: User Invitation Code
    :rtype: str
    """
    return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(6))


def generate_asset_tag():
    """
    Generates unique asset tag
    :return: Asset Tag
    :rtype: str
    """
    return ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(8))


def generate_uuid():
    """
        Generates a generic purpose UUID tag
        :return: UUID String
        :rtype: str
    """
    return str(uuid4())