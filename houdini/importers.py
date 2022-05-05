"""
Houdini Importers.
"""
# local imports
import hou  # pylint: disable=import-error


def import_asset_shots(file_path="", name=None, **kwargs):
    """
    Import Assets/Shot Object in the scene.

    params:
        file_path (str): File path to import.
        file_type (str): File type to import in the scene.
        name (str): Asset name.
        **kwargs: Key word arguments.
    """
    obj = hou.node('/obj/')
    node = obj.createNode('geo', name)
    alembic = hou.node(node.path() + '/alembic1/').parm('fileName').set(file_path)
