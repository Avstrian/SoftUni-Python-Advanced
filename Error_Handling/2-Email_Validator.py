class Error(Exception):
    pass


class NameTooShortError(Error):
    """Name must be more than 4 characters"""
    pass


class MustContainAtSymbolError(Error):
    """Email must contain @"""
    pass


class InvalidDomainError(Error):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass


emails = input()
while not emails == "End":
    email_name = []
    for char in emails:
        if char == "@":
            break
        email_name.append(char)

    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in emails:
        raise MustContainAtSymbolError("Email must contain @")

    if ".com" not in emails and ".bg" not in emails and ".org" not in emails and ".net" not in emails:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net""")

    else:
        print("Email is valid")

    emails = input()
