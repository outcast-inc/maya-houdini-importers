"""
Houdini Importers.
"""
# local imports
import hou  # pylint: disable=import-error
from asset_types import ASSET_TYPES


def import_asset_shots(file_path="", name=None, asset_type=None, **kwargs):
    """
    Import Assets/Shot Object in the scene.

    params:
        file_path (str): File path to import.
        name (str): Asset name.
        asset_type (str): Asset format type.
        **kwargs: Key word arguments.
    """
    obj = hou.node('/obj/')
    asset_data = ASSET_TYPES[asset_type]

    node_obj = obj.createNode(asset_data["main"], name)

    if asset_type == 'camera':
        node_obj.parm(asset_data["parm"]).set(file_path)
        node_obj.parm('buildHierarchy').pressButton()
    else:
        node = node_obj.createNode(asset_data["child"])
        node.parm(asset_data["parm"]).set(file_path)


def import_hip_file(file_path=None):
    """
    Import/Load hip file in current session.

    params:
        file_path (str): HIP file path.

    returns:
        None
    """
    hou.hipFile.merge(file_path)