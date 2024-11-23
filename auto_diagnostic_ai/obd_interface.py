## obd_interface.py
import obd
from typing import Dict, Optional

class OBDInterface:
    def __init__(self, portstr: str = "/dev/ttyUSB0", baudrate: int = 9600, timeout: int = 0):
        """
        Initialize the OBDInterface with default connection parameters.

        :param portstr: The port string for OBD connection.
        :param baudrate: The baud rate for OBD connection.
        :param timeout: The timeout for OBD connection in seconds.
        """
        self.connection: Optional[obd.OBD] = None
        self.portstr: str = portstr
        self.baudrate: int = baudrate
        self.timeout: int = timeout

    def connect(self) -> bool:
        """
        Attempt to establish a connection to the OBD-II port.

        :return: True if the connection was successful, False otherwise.
        """
        self.connection = obd.OBD(portstr=self.portstr, baudrate=self.baudrate, timeout=self.timeout)
        return self.connection.is_connected()

    def get_data(self) -> Dict[str, str]:
        """
        Retrieve OBD-II data from the vehicle.

        :return: A dictionary containing the OBD-II data with command names as keys and their respective values as values.
        """
        obd_data: Dict[str, str] = {}
        if self.connection and self.connection.is_connected():
            # Retrieve all available OBD commands
            commands = self.connection.supported_commands
            # Execute each command and store the results in the obd_data dictionary
            for cmd in commands:
                response = self.connection.query(cmd)
                if response.is_null():
                    continue
                obd_data[cmd.name] = str(response.value)
        return obd_data
