#!/usr/bin/env python3
import re
class MyString:
      def __init__(self, value=''):
        self._value = ''
        self.value = value  

      @property
      def value(self):
        return self._value

      @value.setter
      def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:    
         self._value = new_value

      def is_sentence(self):
          if self._value.endswith('.'):
            return True
          else:
            return False
          
      def is_question(self):
          return self._value.endswith('?')
            
      def is_exclamation(self):
           return self._value.endswith('!')      
         
      def count_sentences(self):
        sentences = re.split(r'[.!?]', self._value)
        return len([s for s in sentences if s.strip()])
