# Base classes for test description

class MailTestBase:
    """Mail test base class"""
    active = False
    identifier = "base"
    name = "Mail Test Base"
    description = "Base class for mail tests"
    smtp_server = "main"        # one of "main" or "secondary" (for simulations of bounces etc.)

    def __init__(self, sender, recipient, config=None):
        self.sender = sender
        self.recipient = recipient
        self.config = config

    def finalizeMessage(self, msg):
        """Add sender and recipient address as From: and To: header to message"""
        if "From" not in msg:
            msg["From"] = self.sender

        if type(self.recipient) == list:
            msg["To"] = ", ".join(self.recipient)
        else:
            msg["To"] = self.recipient
        return msg
    
    def generateTestCases(self):
        """Test case generator - must be overridden"""
        raise NotImplementedError("Test case generator not implemented")

    def __iter__(self):
        """Generates test cases. By default, test cases from generateTestCases() are completed with finalizeMessage()."""
        yield from [self.finalizeMessage(msg) for msg in self.generateTestCases()]
