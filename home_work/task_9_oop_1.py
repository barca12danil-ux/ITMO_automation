from task_9_checks import Checks


class TextBox(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class CheckBox(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class RadioButton(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class WebTables(Checks):
    def __init__(self, loc):
        super().__init__(loc)


text_box = TextBox("#text-box")
check_box = CheckBox("#check-box")
radio_button = RadioButton("#radio-button")
web_tables = WebTables("#web-tables")

print(f"TextBox: {text_box.check_text()}")
print(f"CheckBox: {check_box.check_text()}")
print(f"RadioButton: {radio_button.check_text()}")
print(f"WebTables: {web_tables.check_text()}")
