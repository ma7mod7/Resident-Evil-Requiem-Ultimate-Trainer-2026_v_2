
import configparser
import os

def load_config(filename="config.ini"):
    config = configparser.ConfigParser()
    if not os.path.exists(filename):
        config["Settings"] = {
            "godmode_key": "f2",
            "health_key": "f3",
            "ammo_key": "f4",
            "reload_key": "f5",
            "onehit_key": "f6",
            "accuracy_key": "f7",
            "damage_key": "f8",
            "cp_key": "f9",
            "unlock_key": "f10",
            "stack_key": "f11",
            "consumption_key": "f12",
        }
        with open(filename, "w") as f:
            config.write(f)
    else:
        config.read(filename)
    return config["Settings"]
