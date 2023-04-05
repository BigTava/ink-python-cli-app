"""Top-level package for cli-app."""

__app_name__ = "cli-app"
__version__ = "0.1.0"

(
    SUCCESS,
    ERR_DIR,
    ERR_FILE,
    ERR_SC_DEPLOY,
    ERR_SC_READ,
    ERR_SC_WRITE,
    ERR_ID,
) = range(7)

ERRORS = {
    ERR_DIR: "config directory error",
    ERR_FILE: "config file error",
    ERR_SC_DEPLOY: "smart contract deploy error",
    ERR_SC_READ: "smart contract read error",
    ERR_SC_WRITE: "smart contract write error",
    ERR_ID: "energy-trade id error",
}