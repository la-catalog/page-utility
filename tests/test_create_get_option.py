import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from logger_utility import WritePoint

from page_utility import create_get_option
from page_utility.exceptions import UnknowMarketplaceError


class TestCreateGetOption(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        class BaseMarketplace:
            """Base class which all marketplaces are from"""

            def __init__(self, marketplace: str, logger: WritePoint):
                pass

            def example(self):
                return -1

        class Marketplace1(BaseMarketplace):
            def example(self):
                return 100

        class Marketplace2(BaseMarketplace):
            def example(self):
                return 50

        self._options: dict[str, BaseMarketplace] = {
            "marketplace_1": Marketplace1,
            "marketplace_2": Marketplace2,
        }

    def test_create_get_option(self):
        get_marketplace_test = create_get_option(self._options)

        marketplace_1 = get_marketplace_test("marketplace_1", MagicMock())
        assert marketplace_1.example() == 100

        marketplace_2 = get_marketplace_test("marketplace_2", MagicMock())
        assert marketplace_2.example() == 50

        with self.assertRaises(UnknowMarketplaceError):
            marketplace_3 = get_marketplace_test("marketplace_3", MagicMock())
            assert marketplace_3.example() == "shouldn't reach this line"


if __name__ == "__main__":
    unittest.main()
