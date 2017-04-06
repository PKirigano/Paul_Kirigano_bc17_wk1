class bank_acc(object):
  
  def withdraw(self):
    pass
  def deposit(self):
    pass
  
class savings_acc(bank_acc):
  def __init__(self):
    self.bal = 500
  def deposit(self, amount):
    if amount <= 0:
      return "Invalid deposit amount"
    else:
      self.bal = self.bal + amount
    return self.bal
  
  def withdraw(self, amount):
    if self.bal - amount < 500:
      return 'Cannot withdraw beyond the minimum account balance'
    elif amount >= self.bal:
      return 'Cannot withdraw beyond the current account balance'
    elif amount < 0:
      return 'Invalid withdraw amount'
    else :
      self.bal = self.bal - amount
      return self.bal
      
class current_Acc(bank_acc):
  def __init__(self): 
    self.bal = 0
    
  def deposit(self, amount):
    if amount < 0:
      return 'Invalid deposit amount'
    else:
      self.bal = self.bal + amount
      return self.bal
      
  def withdraw(self, amount):
    if amount < 0:
      return 'Invalid withdraw amount'
    elif amount > self.bal:
      return 'Withdrawing beyond the current account balance is not allowed'
    else:
      self.bal = self.bal - amount
      return self.bal
