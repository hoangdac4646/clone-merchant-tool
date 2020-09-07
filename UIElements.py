class UIElement:
    template: str = ''


class IdentifyElement(UIElement):
    template: str = "//*[contains(text(),'{}')]"


class InputTxtElement(UIElement):
    template: str = "//*[contains(text(),'{}')]/following-sibling::input"


class InputCbbElement(UIElement):
    template: str = "//*[contains(text(),'{}')]/following::input"


class ButtonElement(UIElement):
    template: str = "//button[text()='{}']"
