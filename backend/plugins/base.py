class InventraPlugin:
    """
    Base class pour les plugins Inventra.
    """

    name = "BasePlugin"
    description = "Plugin de base Inventra"
    version = "0.1.0"

    def ready(self):
        """
        Méthode appelée quand le plugin est chargé.
        """
        pass
