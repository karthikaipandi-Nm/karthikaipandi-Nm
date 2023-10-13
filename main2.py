class bank account:
    def_init_(self,account_number,account_holder|_name,initial_balance=0.0):
  self._account_number=account_number
self._account_holder_name=account_holder_name
self._balance=initial_balance
def deposit(self,amount):
  if amount>0;
  self._account_balance+_=amount
  print("deposited.new balance:.format(amount,self._account_balance))
        else:
  printf("invalid deposit amount.")
  def withdraw(Self,amount):
    if amount>0 and amount<=
    self._account_balance:
      self._account_balance_=amountprint("withdrew.new balance:".formate(amount,self._account_balance))
        else:
      printf("invalid withdrawaql amount or insufficent blance:")
    def display_balance(self):
      print("account balance for{}(account #\{}):a^,{}".format(
      self._account_holder_name,
      self._account_number,
      self._account_balance))
      account=
      bankaccount(account_number="1234
      56789",account_holder_name="subsri",initial_balance=5000.0)
      account.display_balance()
      account.deposit(500.0)
      account.withdraw(200.0)
      account.withdraw(20000.0)
      account.display_balance()