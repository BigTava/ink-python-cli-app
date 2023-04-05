"""This module provides the cli-app config functionality."""

from typing import Optional
import configparser
from pathlib import Path
import typer

from app import (
    ERR_DIR, ERR_FILE, SUCCESS, __app_name__
)

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def init_app(rpc_url: str) -> int:
    """Initialize the application."""
    config_code = _init_config_file()

    if config_code != SUCCESS:
        return config_code
    
    substrate_code = _set_node_rpc_url(rpc_url)
    if substrate_code != SUCCESS:
        return substrate_code
    return SUCCESS


def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return ERR_DIR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return ERR_FILE
    return SUCCESS


def _set_node_rpc_url(rpc_url: str) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"rpc_url": rpc_url}
    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return ERR_FILE
    return SUCCESS


def get_rpc_url():
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)

    return config_parser["General"].get("rpc_url")


def set_contract_address(address: str):
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)


    if "Contract" not in config_parser.sections():
        config_parser["Contract"] = {"contract_address": address}

    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return ERR_FILE

    return SUCCESS
    

def get_contract_address() -> Optional[str]:
    config_parser = configparser.ConfigParser()
    config_parser.read(CONFIG_FILE_PATH)

    return config_parser["Contract"].get("contract_address")