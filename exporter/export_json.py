import json
from pathlib import Path


class JSONExporter:
    """
    Exports analysis results to a JSON file.
    """

    def export(self, data, output_path):
        """
        Export dictionary data to JSON.

        Parameters
        ----------
        data : dict
            Data to export.

        output_path : str | Path
            Output JSON file.

        Returns
        -------
        Path
            Path to the generated file.
        """

        output_path = Path(output_path)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return output_path
    