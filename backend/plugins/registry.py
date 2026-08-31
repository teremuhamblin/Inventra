from importlib import import_module


class PluginRegistry:
    def __init__(self):
        self._plugins = []

    def load_from_settings(self, plugin_paths):
        for path in plugin_paths:
            module = import_module(path)
            plugin_class = getattr(module, "Plugin", None)
            if plugin_class:
                instance = plugin_class()
                instance.ready()
                self._plugins.append(instance)

    @property
    def plugins(self):
        return self._plugins


registry = PluginRegistry()
