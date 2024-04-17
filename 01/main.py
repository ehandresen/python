from CashRegister import CashRegister

cr = CashRegister()
cr.add_item(1000)
cr.add_item(2000)
cr.add_item(3000)
cr.add_item(2500)

print(cr.get_count())
print(cr.get_total())