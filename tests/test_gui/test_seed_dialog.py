import time
from unittest.mock import MagicMock

import keyring
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from node_launcher.gui.launch_widget import LaunchWidget


class TestSeedDialog(object):
    def test_show(self, qtbot: QTest, launch_widget: LaunchWidget):
        launch_widget.node_launcher.generate_seed = MagicMock(return_value=['test', 'seed'])

        qtbot.mouseClick(launch_widget.testnet_group_box.initialize_wallet_button,
                         Qt.LeftButton)

    def test_keyring(self):
        timestamp = str(time.time())

        keyring.set_password(service_name='test_entry',
                             username=timestamp,
                             password='test_password')
        password = keyring.get_password(service_name='test_entry',
                                        username=timestamp)
        assert password == 'test_password'
        keyring.delete_password(service_name='test_entry',
                                username=timestamp)