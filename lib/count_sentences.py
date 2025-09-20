#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = None
    self.value = value

  def get_value(self):
    return self._value
  
  def set_value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return isinstance(self.value, str) and self.value.endswith(".")
  
  def is_question(self):
    return isinstance(self.value, str) and self.value.endswith("?")
  
  def is_exclamation(self):
    return isinstance(self.value, str) and self.value.endswith("!")
  
  def count_sentences(self):
    if not isinstance(self.value, str) or not self.value:
      return 0
    
    s = self.value.strip()

    s = s.replace("!", ".").replace("?", ".")

    pieces = [part.strip() for part in s.split(".") if part.strip()]

    return len(pieces)