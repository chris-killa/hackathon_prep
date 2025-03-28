import Peyman
import Chris
import martin
def main():
    username = Peyman.get_username()
    adding = Chris.add_at_symbol_to_username(username)
    full_mail = martin.add_domain_to_username(adding)
    print(full_mail)
main()