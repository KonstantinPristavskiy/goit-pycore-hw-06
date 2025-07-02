from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, phone_number):
        if isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) == 10:
            super().__init__(phone_number)
        else:
              raise ValueError("Phone must be 10 digits")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_raw):
        """
        Створює обʼєкт класу Phone та 
        додає номер телефону в список self.phones
        """
        new_phone = Phone(phone_raw)
        self.phones.append(new_phone)
    
    def find_phone(self, phone: str) -> Phone | None:
        """Повертає об’єкт Phone або None, якщо не знайдено."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone_to_delete):
        phone_obj = self.find_phone(phone_to_delete)
        if phone_obj:
            self.phones.remove(phone_obj)

                

    def edit_phone(self, old_phone, new_phone):
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index] = Phone(new_phone)
    
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass



def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")






if __name__ == "__main__":
    main()