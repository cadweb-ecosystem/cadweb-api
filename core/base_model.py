class BaseModel:
    """Common base class for all API components."""

    def info(self):
        return f"{self.__class__.__name__} loaded"
