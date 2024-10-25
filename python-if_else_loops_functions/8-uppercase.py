  #!/usr/bin/python3

  def to_uppercase(input_string):
          """Convert the input string to uppercase."""
              return input_string.upper()

          if __name__ == "__main__":
                  # Test cases
                      print(to_uppercase("holberton"))  # Expected: HOLBERTON
                          print(to_uppercase("Holberton School"))  # Expected: HOLBERTON SCHOOL
                              print(to_uppercase("Holberton School, 98 battery street"))  # Expected: HOLBERTON SCHOOL, 98 BATTERY STREET
                                  print(to_uppercase(""))  # Expected: (empty string)
                                      print(to_uppercase("98"))  # Expected: 98
                                          print(to_uppercase("z"))  # Expected: Z

