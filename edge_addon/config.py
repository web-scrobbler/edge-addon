import sys
from dataclasses import dataclass

from edge_addons_api.client import Options as EdgeOptions


@dataclass
class Options:
    product_id: str
    client_id: str
    api_key: str
    file_path: str
    notes: str
    debug: bool
    retry_count: int
    sleep_seconds: int

    def to_edge_options(self) -> EdgeOptions:
        return EdgeOptions(
            product_id=self.product_id,
            client_id=self.client_id,
            api_key=self.api_key,
            retry_count=self.retry_count,
            sleep_seconds=self.sleep_seconds,
        )


def create_options() -> Options:
    """
    create Options object from system arguments.

    Returns:
        Options object containing all configuration
    """
    if len(sys.argv) < 9:
        print("Incorrect number of arguments given. Please check action parameters")
        sys.exit(1)

    product_id = sys.argv[1]
    client_id = sys.argv[2]
    api_key = sys.argv[3]
    file_path = sys.argv[4]
    notes = sys.argv[5]
    debug = sys.argv[6].lower() in ["true", "1"]
    retry_count = int(sys.argv[7])
    sleep_seconds = int(sys.argv[8])

    return Options(
        product_id=product_id,
        client_id=client_id,
        api_key=api_key,
        file_path=file_path,
        notes=notes,
        debug=debug,
        retry_count=retry_count,
        sleep_seconds=sleep_seconds,
    )
