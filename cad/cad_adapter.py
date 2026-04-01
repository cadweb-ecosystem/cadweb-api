class CADAdapter:
    """Abstract CAD interface (FreeCAD, Blender, etc.)."""

    def load(self, path):
        raise NotImplementedError

    def export(self, obj, path):
        raise NotImplementedError
