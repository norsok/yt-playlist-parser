import json
import os
from typing import Dict, Any

def load_config(config_path: str = None) -> Dict[str, Any]:
    """Загружает конфигурацию из JSON файла"""
    if config_path is None:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Глобальная переменная с конфигурацией
CONFIG = load_config()