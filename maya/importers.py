import maya.cmds as cmds


def import_asset_shots(file_path="", file_type="mayaAscii", name_space=None, **kwargs):
    cmds.file(file_path, typ=file_type, namespace=name_space, **kwargs)
