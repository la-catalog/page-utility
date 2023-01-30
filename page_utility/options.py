from typing import Callable, TypeVar

from logger_utility import WritePoint

from page_utility.exceptions import UnknowMarketplaceError

MarketplaceClass = TypeVar("MarketplaceClass")


def create_get_option(
    options: dict[str, MarketplaceClass]
) -> Callable[[str, WritePoint], MarketplaceClass]:
    """
    Create a function that receives a string and map it to a marketplace option

    It's a logic used in many page packages, because you can have X marketplaces
    and you need it to create dynamically the marketplace object.
    Why dynamically? Because which object can add/remove variables like `self._example`.

    This function receives a dictionary like:

    options = {
        "ri_happy": RiHappy,
        "americanas": Americanas,
        "Amazon": Aamazon,
    }

    And returns a function that will receives the marketplace and logger
    to instantiate the right marketplace object.
    """

    def f(marketplace: str, logger: WritePoint) -> MarketplaceClass:
        try:
            marketplace_class = options[marketplace]
            return marketplace_class(marketplace=marketplace, logger=logger)
        except KeyError as e:
            valid = ", ".join(options.keys())

            raise UnknowMarketplaceError(
                f"Marketplace '{marketplace}' is not defined in {__package__} package. Valid options: {valid}"
            ) from e

    return f
