epr__(self) -> str:
        return repr({
            'comapany_name': self.company_name,
            'riders': len(self.riders),
            'drivers': len(self.drivers),
            'rides': len(self.rides),
        })