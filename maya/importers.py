import maya.cmds as cmds


def import_asset_shots(file_path="", file_type="mayaAscii", name_space=None, **kwargs):
    o = True
    r = True
    i = True
    namespace = name_space
    type=["mayaAscii", "mayaBinary", "OBJ", "ASS", "FBX", "Alembic", "USD import"]
    cmds.file(file_path, typ=file_type, namespace=name_space, **kwargs)
