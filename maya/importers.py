"""
Maya Importers.
"""
# local imports
from maya import cmds  # pylint: disable=import-error


def import_asset_shots(file_path="", file_type="mayaAscii", name_space=None, **kwargs):
    """
    Import Assets/Shot Object in the scene.

    params:
        file_path (str): File path to import.
        file_type (str): File type to import in the scene.
        name_space (str): Namespace for the imports.
        **kwargs: Key word arguments.
    """
    cmds.file(file_path, typ=file_type, namespace=name_space, **kwargs)
