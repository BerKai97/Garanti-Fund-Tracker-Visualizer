class Fund:
    def __init__(self, json_data: dict):
        keys = list(json_data.keys())
        self.fund_name = json_data.get(keys[0])[:3]
        self.weight = json_data.get(keys[2])
        self.quantity = json_data.get(keys[3])
        self.amount = json_data.get(keys[4]).split('\n')[0]
        self.amount = self.amount.replace(".", "").replace(",", ".").replace("TL", "")
        self.amount = float(self.amount)
        self.profit_loss: float = float(
            json_data.get(keys[5]).replace(".", "").replace(",", ".").replace("TL", "")
        )
        self.price = json_data.get(keys[6])
