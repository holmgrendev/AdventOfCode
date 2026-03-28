from pathlib import Path
import tomllib

CONFIG_PATH = Path.cwd() / "config.toml"

class Config:
    """
    Config for Holmgrens AoC.
    """

    def __init__(self, config_path=CONFIG_PATH):
        self.path = config_path
        self._data = {}
        self._load()
    
    def _load(self):
        """
        Load config.
        """
        
        if not self.path.exists():
            raise FileNotFoundError(f"Config file not found: {self.path}")
        
        with open(self.path, "rb") as file:
            self._data = tomllib.load(file)
    
    def get(self, *keys) -> str:
        """
        Get a config value.
        Returns empty string if missing.

        Args:
            *keys (str): Key/s for desired value.
        
        Returns:
            str: Config value.
        """

        config_data = self._data

        for key in keys:

            if isinstance(config_data, dict) and key in config_data:
                config_data = config_data[key]

            else:
                return ""

        return config_data if not isinstance(config_data, dict) else ""

config = Config()