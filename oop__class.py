class RegForm:
    amount_expected_to_be_paid = 50_000  

   
    def __init__(self, firstname, lastname, address, amount):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.amount_paid_by_student = amount

    
    def balance(self):
        return RegForm.amount_expected_to_be_paid - self.amount_paid_by_student


print("Welcome to Blockfueslabs")

joseph = RegForm("Joe", "Abu", "Jos", 30_000)
dorcas = RegForm("Dorcas", "Tanimu", "Bauchi", 50_000)

print(f"{joseph.firstname} paid {joseph.amount_paid_by_student}, balance: {joseph.balance()}")
print(f"{dorcas.firstname} paid {dorcas.amount_paid_by_student}, balance: {dorcas.balance()}")
