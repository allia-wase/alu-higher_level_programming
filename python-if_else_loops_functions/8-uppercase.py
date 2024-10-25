def uppercase(str):
        """Print a string in uppercase followed by a new line."""
            result = ""
                for char in str:
                            if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
                                            # Convert to uppercase by adjusting the ASCII value
                                                        result += chr(ord(char) - 32)
                                                                else:
                                                                                result += char  # Keep other characters unchanged
                                                                                    print("{}".format(result))  # Print the result

                                                                                    # Example usage:
                                                                                    if __name__ == "__main__":
                                                                                            uppercase("best")
                                                                                                uppercase("Best School 98 Battery street")

