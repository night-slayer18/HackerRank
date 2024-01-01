def calculate_balances(expenses, settlements):
    balances = {}
    
    # Calculate balances from expenses
    for expense in expenses:
        paid_by, amount, *persons = expense.split('/')
        amount = int(amount)
        num_persons = len(persons)
        split_amount = amount / num_persons
        
        for person in persons:
            if person not in balances:
                balances[person] = 0
            balances[person] -= split_amount
        
        if paid_by not in balances:
            balances[paid_by] = 0
        balances[paid_by] += amount
    
    # Calculate balances from settlements
    for settlement in settlements:
        transaction_type, person1, person2, amount = settlement.split('/')
        amount = int(amount)
        
        if transaction_type == 'Paid By':
            if person1 not in balances:
                balances[person1] = 0
            balances[person1] += amount
            
            if person2 not in balances:
                balances[person2] = 0
            balances[person2] -= amount
        elif transaction_type == 'Lent By':
            if person1 not in balances:
                balances[person1] = 0
            balances[person1] -= amount
            
            if person2 not in balances:
                balances[person2] = 0
            balances[person2] += amount
    
    return balances

expenses = [
    'A/240/A/B/C',
    'B/120/A/C',
    'C/A/100',
    'C/100/C/A'
]

settlements = [
    'C/B/L100',
    'B/A/L200',
    'C/B/L300',
    'B/C/100'
]

balances = calculate_balances(expenses, settlements)

for person, balance in balances.items():
    print(f'{person}: {balance}')
