"""Module with class StringProcessor"""


class StringProcessor:
    """Class StringProcessor, contains methods for string processing"""

    @staticmethod
    def reverse_string(string: str) -> str:
        """Returns reverse_string"""
        return string[::-1]

    @staticmethod
    def capitalize_string(string: str):
        """Returns capitalize_string"""
        return string.capitalize()

    @staticmethod
    def count_vowels(string: str) -> int:
        """Returns count_vowels"""
        vowels = "aeiouyAEIOUY"
        return sum(1 for char in string if char in vowels)


if __name__ == "__main__":
    ST = "abcdefghijky"

    REV_STR = StringProcessor.reverse_string(ST)
    CAP_STR = StringProcessor.capitalize_string(ST)
    count_v = StringProcessor.count_vowels(ST)

    print(REV_STR)
    print(CAP_STR)
    print(count_v)
