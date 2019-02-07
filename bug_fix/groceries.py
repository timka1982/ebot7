from datetime import datetime
import inspect

class Groceries():
  def __init__(self, items=[], date_needed_by=datetime.now()):
    self.items = items
    self.date_needed_by = date_needed_by
  
  def __repr__(self):
    return ', '.join(self.items) + ' must be bought by ' + self.date_needed_by.strftime('%d-%m-%y')
  
  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    self.items.remove(item)
  
  def update_date_needed_by(self, date):
    self.date_needed_by = date


