#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the specified file.

        Parameters:
        filename (str): The filename of the output file where the object will
        be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from the specified file.

        Parameters:
        filename (str): The filename of the input file where the object is
        saved.

        Returns:
        CustomObject: The deserialized instance of CustomObject, or None if
        an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
