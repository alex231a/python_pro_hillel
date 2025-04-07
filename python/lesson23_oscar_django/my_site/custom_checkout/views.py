"""
Custom checkout view that overrides the default shipping address view.

This module allows replacing Oscar's default form with a custom
ShippingAddressForm that supports features like dynamic country filtering.
"""

from oscar.apps.checkout.views import ShippingAddressView as cs # pylint: disable=import-error

from custom_checkout.forms import ShippingAddressForm


# disable=import-error


class ShippingAddressView(cs): # pylint: disable=too-few-public-methods
    """
    Custom shipping address view used during the checkout process.

    Overrides Oscar's default `ShippingAddressView` to use a custom form
    that includes dynamic country selection and phone number validation.
    """

    def get_form_class(self):
        """
        Return the custom form class used for collecting shipping address.

        Returns:
            ShippingAddressForm: The custom shipping address form.
        """
        return ShippingAddressForm
