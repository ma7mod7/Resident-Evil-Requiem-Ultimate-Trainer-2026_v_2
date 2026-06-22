
import sys
import time
import threading
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.trainer_engine import TrainerEngine
from core.feature_manager import FeatureManager
from utils.logger import log_info, log_success
from utils.config_loader import load_config
from utils.hotkey_manager import HotkeyManager
from gui.console_renderer import ConsoleRenderer

def main():
    load_config("config.ini")
    log_info("Resident Evil Requiem Ultimate Trainer v2.0 starting...")
    engine = TrainerEngine()
    feature_mgr = FeatureManager()
    hotkey_mgr = HotkeyManager()
    renderer = ConsoleRenderer()

    # Combat
    hotkey_mgr.register_hotkey('f1', lambda: renderer.toggle_menu())
    hotkey_mgr.register_hotkey('f2', lambda: feature_mgr.toggle('godmode'))
    hotkey_mgr.register_hotkey('f3', lambda: feature_mgr.toggle('infinite_health'))
    hotkey_mgr.register_hotkey('f4', lambda: feature_mgr.toggle('infinite_ammo'))
    hotkey_mgr.register_hotkey('f5', lambda: feature_mgr.toggle('no_reload'))
    hotkey_mgr.register_hotkey('f6', lambda: feature_mgr.toggle('one_hit_kill'))
    hotkey_mgr.register_hotkey('f7', lambda: feature_mgr.toggle('super_accuracy'))
    hotkey_mgr.register_hotkey('f8', lambda: feature_mgr.trigger('damage_multiplier'))

    # Inventory
    hotkey_mgr.register_hotkey('f9', lambda: feature_mgr.trigger('edit_cp'))
    hotkey_mgr.register_hotkey('f10', lambda: feature_mgr.trigger('unlock_all'))
    hotkey_mgr.register_hotkey('f11', lambda: feature_mgr.trigger('stack_999'))
    hotkey_mgr.register_hotkey('f12', lambda: feature_mgr.toggle('ignore_consumption'))

    # Visual
    hotkey_mgr.register_hotkey('insert', lambda: feature_mgr.trigger('toggle_overlay'))
    hotkey_mgr.register_hotkey('pageup', lambda: feature_mgr.trigger('first_person'))
    hotkey_mgr.register_hotkey('pagedown', lambda: feature_mgr.trigger('third_person'))
    hotkey_mgr.register_hotkey('home', lambda: feature_mgr.trigger('speed_multiplier'))

    # Utility
    hotkey_mgr.register_hotkey('end', lambda: feature_mgr.toggle('freeze_enemies'))
    hotkey_mgr.register_hotkey('num 1', lambda: feature_mgr.trigger('reset_save_count'))
    hotkey_mgr.register_hotkey('num 2', lambda: feature_mgr.trigger('set_game_speed'))
    hotkey_mgr.register_hotkey('num 3', lambda: feature_mgr.toggle('freeze_playtime'))
    hotkey_mgr.register_hotkey('num 4', lambda: feature_mgr.toggle('aimbot'))

    hotkey_mgr.register_hotkey('f9', lambda: sys.exit(0))

    engine_thread = threading.Thread(target=engine.run, args=(feature_mgr,), daemon=True)
    engine_thread.start()

    log_success("Trainer ready. Press F1 for help, Insert for overlay.")
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        log_info("Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
