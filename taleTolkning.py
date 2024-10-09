class Tale():

    def __init__(self, message_input, message_output: str) -> None:
        """
        Message input: Når brukeren sier noe
        Message output: Når programmet svarer
        """
        self.message_input = message_input
        self.message_output = message_output

    def approve_message(self, message_input):
        """
        Tar utgangspunkt i noe bruker sa, utfører en vilkårlig handlig.
        """
        pass

    def deny_message(self, message_input):
        print("Sorry I didn't understand that.")