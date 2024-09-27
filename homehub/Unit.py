
# Dette er foreldre klassen til alle enhetsklasser senere

class Unit():
    
    def __init__(self, unit_id: int, name:str, status: bool) -> None:
        self.unit_id = unit_id
        self.name = name
        self.status = status
        
    
    # Create unit blir brukt til å produsere units i grensesnittet senere
    def create_unit():
        pass
    
    
    def setUnit_id(self, new_id: int) -> None:
        """Setter ny id på en enhet

        Args:
            new_id (int): det nye id nummeret til enheten
        """
        self.unit_id = new_id
    
    
    def setStatus(self) -> bool:
        """Setter ny status av/på for enheten

        Returns:
            bool: returnerer false dersom enheten var på 
            og true dersom enheten var av
        """
        self.status = not self.status
        return self.status
    
    
    def setName(self, name: str) -> None:
        """Setter nytt navn på enheten

        Args:
            name (str): Det nye navnet til enheten
        """
        self.name = name
        

def main():
    pass

if __name__ == "__Main__":
    main()