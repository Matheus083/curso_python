# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool:
        ...

class NotificationEmail(Notification):
    def send(self) -> True:
        print('E-mail: sending:', self.message)
        return True

class NotificationSMS(Notification):
    def send(self) -> True:
        print('SMS: sending:', self.message)
        return True
    
# n = NotificationEmail('Testing Notification.')
# n.send()

def notify(notification: Notification): 
    send_notification = notification.send()

    if not send_notification:
        print('Send not notification.')
        return 
    
    print('Notification SEND!')

notify_email = NotificationEmail('Testing E-mail.')
notify(notify_email)
