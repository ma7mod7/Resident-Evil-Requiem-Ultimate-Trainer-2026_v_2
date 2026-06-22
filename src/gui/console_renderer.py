
from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False

    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")

    def show_menu(self):
        print("╔═══════════════════════════════════════════════════════╗")
        print("║   RESIDENT EVIL REQUIEM ULTIMATE TRAINER v2.0        ║")
        print("╠═══════════════════════════════════════════════════════╣")
        print("║  COMBAT                                              ║")
        print("║  F2 - God Mode           F6 - One-Hit Kill           ║")
        print("║  F3 - Infinite Health    F7 - Super Accuracy         ║")
        print("║  F4 - Infinite Ammo      F8 - Damage Multiplier      ║")
        print("║  F5 - No Reload                                     ║")
        print("╠═══════════════════════════════════════════════════════╣")
        print("║  INVENTORY                                           ║")
        print("║  F9 - Edit CP            F11 - Stack Items to 999    ║")
        print("║  F10 - Unlock All        F12 - Ignore Consumption    ║")
        print("╠═══════════════════════════════════════════════════════╣")
        print("║  VISUAL & UTILITY                                    ║")
        print("║  Insert - Overlay        End - Freeze Enemies        ║")
        print("║  PageUp - First-Person   Num1 - Reset Save Count     ║")
        print("║  PageDown - Third-Person Num2 - Game Speed           ║")
        print("║  Home - Speed Multiplier Num3 - Freeze Playtime      ║")
        print("║                           Num4 - Aimbot              ║")
        print("╚═══════════════════════════════════════════════════════╝")
