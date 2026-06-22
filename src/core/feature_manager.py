
from utils.logger import log_success, log_info

class FeatureManager:
    def __init__(self):
        self.features = {
            "godmode": False,
            "infinite_health": False,
            "infinite_ammo": False,
            "no_reload": False,
            "one_hit_kill": False,
            "super_accuracy": False,
            "ignore_consumption": False,
            "freeze_enemies": False,
            "freeze_playtime": False,
            "aimbot": False,
        }

    def toggle(self, name):
        if name in self.features:
            self.features[name] = not self.features[name]
            status = "ON" if self.features[name] else "OFF"
            log_success(f"{name.upper()} {status}")

    def trigger(self, name):
        msgs = {
            "damage_multiplier": "Damage multiplier set to 5x",
            "edit_cp": "CP set to 999,999",
            "unlock_all": "All special content unlocked!",
            "stack_999": "All stackable items set to 999",
            "toggle_overlay": "REFramework overlay toggled",
            "first_person": "Switched to First-Person mode",
            "third_person": "Switched to Third-Person mode",
            "speed_multiplier": "Movement speed set to 2x",
            "reset_save_count": "Save count reset to 0",
            "set_game_speed": "Game speed set to 1.5x",
        }
        if name in msgs:
            log_success(msgs[name])
        else:
            log_success(f"Triggered: {name}")
