import importlib.metadata

try:
    __version__ = importlib.metadata.version("mem0ai")
except importlib.metadata.PackageNotFoundError:
    # Fallback version for development environment
    __version__ = "0.1.117-dev"

from mem0.client.main import AsyncMemoryClient, MemoryClient  # noqa
from mem0.memory.main import AsyncMemory, Memory  # noqa


def get_version() -> str:
    """
    Get the current version of Mem0.

    Returns:
        str: The version string
    """
    return __version__


def get_info() -> dict:
    """
    Get comprehensive information about the Mem0 installation.

    Returns:
        dict: Dictionary containing version and supported providers
    """
    from mem0.utils.factory import get_supported_providers

    return {
        "version": __version__,
        "supported_providers": get_supported_providers(),
    }
