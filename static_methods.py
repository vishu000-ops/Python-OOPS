class BurgerUtils:
    @staticmethod
    def clean__ingredients(text):
        return [item.strip() for item in text.split(",")]


raw = " Bread , Onion , Tikki , Mionis , Sauces "
cleaned = BurgerUtils.clean__ingredients(raw)
print(cleaned)