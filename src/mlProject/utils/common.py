import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Parsed content of the YAML file.
    
    Raises:
        ValueError: If the YAML file is empty.
        Exception: For any other exceptions.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty!")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        logger.error("YAML file is empty!")
        raise ValueError("YAML file is empty!")
    except Exception as e:
        logger.error(f"Failed to read YAML file: {e}")
        raise e

@ensure_annotations
def create_directories(paths: List[Path], verbose: bool = True):
    """
    Creates directories for the given list of paths.

    Args:
        paths (List[Path]): List of directory paths to create.
        verbose (bool): Whether to log the creation of each directory.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save.
    """
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"JSON file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save JSON file at {path}: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads content from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Parsed content of the JSON file.
    """
    try:
        with open(path, 'r') as f:
            content = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except Exception as e:
        logger.error(f"Failed to load JSON file from {path}: {e}")
        raise e

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        logger.error(f"Failed to save binary file at {path}: {e}")
        raise e

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Loaded data.
    """
    try:
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data
    except Exception as e:
        logger.error(f"Failed to load binary file from {path}: {e}")
        raise e

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of the file at the specified path in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: Size of the file in KB.
    """
    try:
        size_in_kb = round(os.path.getsize(path) / 1024, 2)
        logger.info(f"Size of the file at {path}: {size_in_kb} KB")
        return f"~ {size_in_kb} KB"
    except Exception as e:
        logger.error(f"Failed to get size for file at {path}: {e}")
        raise e
