from credit.models import Client, Account, Credit

a = Client(name='Бердиев Н.Д', citizenship='КР', birth_year=1994, work_place='Codify')
b = Client(name='Баяман Айдаров', citizenhip='КР', birth_year=2004, work_place='Codify')
a1 = Account(number=6710654834137604, account_type=1)
b1 = Account(number=6552138061952374, account_type=2)
a2 = Credit(sum=10000)
b2 = Credit(sum=12000)