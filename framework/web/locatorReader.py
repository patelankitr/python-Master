import json


class Reader:
    """
    Class responsible for reading JSON data from a file and extracting configuration dynamically.
    """

    def __init__(self, config_file="D:\Projects\Python-Framework\pages\login_locator.json"):
        self.config_file = config_file

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
            config = data.get("Home_button", {})
            return config
        except Exception as e:
            print(f"Error extracting configuration: {e}")
            return {}


# Example Usage
if __name__ == "__main__":
    reader = Reader("D:\Projects\Python-Framework\pages\login_locator.json")
    config = reader.get_config()
    platform = config.get("platform")

    if platform == 'web':
        locator_type = config.get("locator_type")
        web_locator = config.get("web_locator")

        print(f"Platform: {locator_type}")
        print(f"Browser: {web_locator}")

    else:
        print("No configuration found for the specified run key.")
