# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        
        addresses = re.split(r'[,\s]+', self.email_addresses)
        
        valid_addresses = [address for address in addresses if email_pattern.fullmatch(address)]
        
        unique_addresses = sorted(set(valid_addresses))
        return unique_addresses