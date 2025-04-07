"""
Custom shipping address form used during checkout.

This form overrides Oscar's default AbstractAddressForm to:
- Filter the list of countries to only those allowed for shipping.
- Automatically assign a country if only one shipping country is available.
"""

from oscar.core.loading import get_class, get_model # pylint: disable=import-error
from oscar.forms.mixins import PhoneNumberMixin # pylint: disable=import-error

Country = get_model("address", "Country")
AbstractAddressForm = get_class("address.forms", "AbstractAddressForm")


class ShippingAddressForm(PhoneNumberMixin, AbstractAddressForm):# pylint: disable=too-few-public-methods
    """
    Custom form for entering shipping address during checkout.

    Inherits from:
        - PhoneNumberMixin: adds phone number validation.
        - AbstractAddressForm: base address form provided by Oscar.

    Key features:
        - Dynamically filters countries to those marked as shipping-enabled.
        - Removes country field if there's only one available option.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and adjust the country field based on available
        shipping countries.
        """
        super().__init__(*args, **kwargs)
        self.adjust_country_field()

    def adjust_country_field(self):
        """
        Modify the 'country' field to limit it to shipping-enabled countries
        only.

        If only one shipping country is available:
            - Remove the field from the form.
            - Automatically assign it to the instance.

        Otherwise:
            - Update the queryset and remove the empty label.
        """
        countries = Country._default_manager.filter(is_shipping_country=True) # pylint: disable=protected-access

        # No need to show country dropdown if there is only one option
        if len(countries) == 1:
            self.fields.pop("country", None)
            self.instance.country = countries[0]
        else:
            self.fields["country"].queryset = countries
            self.fields["country"].empty_label = None

    class Meta: # pylint: disable=too-few-public-methods
        """
        Meta configuration for the shipping address form.

        - Uses Oscar's `shippingaddress` model.
        - Defines a list of required address fields.
        """
        model = get_model("order", "shippingaddress")

        fields = [
            "first_name",
            "last_name",
            "line1",
            # "line2",
            # "line3",
            # "line4",
            # "state",
            "postcode",
            "country",
            "phone_number",
            # "notes",
        ]
