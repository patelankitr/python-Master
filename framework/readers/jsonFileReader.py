import json
from pathlib import Path


class Reader:
    """
    Class responsible for reading JSON data from a file and extracting configuration dynamically.
    """

    def __init__(self, config_file=None):
        self.config_file = config_file


        if config_file is None:
            # Dynamically determine the base path for cross-platform compatibility
            self.config_path = Path(__file__).parent.parent.parent / "config" / "TestConfig.json"
            print("Updated Path:", self.config_path)

            self.config_file = self.config_path.resolve()
        else:
            self.config_file = Path(self.config_path).resolve()
            print("Provided Config File Path:", self.config_path)



    def read_json(self):
        """
        Reads a JSON file and returns the parsed data.

        Returns:
            dict: Parsed JSON data.
        """
        try:
            with open(self.config_file, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return {}

    def get_config(self):
        """
        Extracts configuration for the specified `run` key.

        Returns:
            dict: Configuration for the `run` key, or an empty dictionary if not found.
        """
        try:
            data = self.read_json()
            run_key = data.get("run", "")
            config = data.get("config", {}).get(run_key, {})
            return config
        except Exception as e:
            print(f"Error extracting configuration: {e}")
            return {}


# Example Usage
if __name__ == "__main__":
    reader = Reader("D:\Projects\Python-Framework\config\TestConfig.json")
    config = reader.get_config()

    if config:
        platform = config.get("platform")
        browser = config.get("browser")
        env = config.get("env")

        print(f"Platform: {platform}")
        print(f"Browser: {browser}")
        print(f"Environment URL: {env}")
    else:
        print("No configuration found for the specified run key.")
