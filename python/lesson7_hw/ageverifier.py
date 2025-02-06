"""Module with class age verifier"""


class AgeVerifier:
    """Class age verifier"""

    @staticmethod
    def is_adult(age: int) -> bool:
        """Method that verifiers age"""
        if age >= 18:
            return True
        return False
