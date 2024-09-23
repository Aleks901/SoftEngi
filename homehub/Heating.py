import Unit as unit


class Heating(unit):
    
    def __init__(self, unit_id, name, status, temperature: float) -> None:
        super.__init__(self, unit_id, name, status)
        self.temperature = temperature
        
        

def main():
    pass

if __name__ == "__Main__":
    main()