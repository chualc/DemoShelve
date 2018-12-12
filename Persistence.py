import shelve

class SaveInfo:
    def __init__(self, email, name):
        self.__email = email
        self.__name = name

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

accessShelve = shelve.open('data')

def saveToShelve(email, name):
    # To check if email already exist.
    # email is used as a key
    if email in accessShelve:
        return False  # Saving fail
    else:
        accessShelve[email] = SaveInfo(email, name)
        return True   # Saving ok

def retrieveAllDataFromShelve():
    infoList = []
    for email in accessShelve:
        infoList.append(accessShelve[email])
    return infoList

def retrieveDataUsingEmail(email):
    if email in accessShelve:  # email is the key
        return accessShelve[email]
    else:
        return None

def retrieveDataUsingName(name):
    result = None
    # name is not a key. Hence, has to use a loop and search for the name
    for email in accessShelve:
        if name.upper() == accessShelve[email].get_name().upper():
            result = accessShelve[email]
            break
    return result

def deleteAll():
    accessShelve.clear()

def deleteOneRecord(email):
    if email in accessShelve:
        del accessShelve[email]
        return True
    else:
        return False
