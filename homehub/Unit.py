


class Unit():
    
    def __init__(self, unit_id: int, name:str, status: bool) -> None:
        self.unit_id = unit_id
        self.name = name
        self.status = status
        
    
    # Create unit blir brukt til å produsere units i grensesnittet senere
    def create_unit():
        pass
    
    def setUnit_id(self, new_id):
        self.unit_id = new_id
    
    
    def setStatus(self):
        self.status = not self.status
        return self.status
    
    def setName(self, name):
        self.name = name
        
    
        





def main():
    pass

if __name__ == "__Main__":
    main()