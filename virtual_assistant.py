from collections import UserDict

class Field:
    """Базовий клас для полів запису."""
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """Клас для зберігання імені контакту. Обов'язкове поле."""
    pass

class Phone(Field):
    """Клас для зберігання номера телефону. Має валідацію формату (10 цифр)."""
    
    def __init__(self, phone_number):
        
        """перевіряє що був переданий String який складається з 10 цифр"""
        if isinstance(phone_number, str) and phone_number.isdigit() and len(phone_number) == 10:
            super().__init__(phone_number)
        else:
              raise ValueError("Phone must be 10 digits")
        

class Record:
    """Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_raw: str) -> None:
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

    def remove_phone(self, phone_to_delete: str) -> bool:
        """Видаляє телефон; повертає True, якщо знайшов і видалив."""
        for index, phone in enumerate(self.phones):
            if phone.value == phone_to_delete:
                self.phones.pop(index)
                return True
        return False

                

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        """
        Замінює об’єкт Phone(old_phone) на Phone(new_phone);
        повертає True, якщо заміна відбулася, False інакше.
        """
        for index, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[index] = Phone(new_phone)
                return True
        return False
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        """Додає Record у словник під ключем імені контакту."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """Повертає Record за точним ім’ям або None, якщо не знайдено."""
        return self.data.get(name)
        
    def delete(self, name: str) -> bool:
        """
        Видаляє Record за ім’ям.
        Повертає True, якщо контакт був, і False, якщо не було такого ключа.
        """
        if name in self.data:
            del self.data[name]
            return True
        return False



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