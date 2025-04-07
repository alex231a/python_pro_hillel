"""Custom checkout application configuration for Django Oscar.

This module overrides the default Oscar checkout app configuration
to enable custom behavior, such as injecting a custom shipping address view.

Classes:
    CheckoutConfig: Extends Oscar's default CheckoutConfig to provide
    project-specific configuration and view logic.
"""

from oscar.apps.checkout import \
    apps as checkout_apps  # pylint: disable=import-error


class CheckoutConfig( # pylint: disable=too-few-public-methods
    checkout_apps.CheckoutConfig):
    """
    Custom configuration for the checkout app.

    This class extends Oscar's default `CheckoutConfig` to allow
    overriding or extending functionality in the checkout process.

    Attributes:
        default_auto_field (str): Defines the type of primary key to use by
        default.
        name (str): The dotted Python path to the application.

    When the app is ready (i.e., all apps are initialized), this config
    dynamically imports and attaches a custom shipping address view,
    allowing it to be referenced elsewhere (e.g., in URL configuration).
    """

    default_auto_field = "django.db.models.AutoField"
    name = "custom_checkout"

    def ready(self):
        """
        Called when the app is fully loaded.

        Imports and assigns the custom `ShippingAddressView` to be used
        during the checkout process. This ensures that Django's app registry
        has been initialized before importing any models or views.
        """
        super().ready()
        # 👇 тепер це безпечно, бо Django вже ініціалізував apps
        from custom_checkout.views import \
            ShippingAddressView  # pylint: disable=import-outside-toplevel
        self.shipping_address_view = ShippingAddressView  # pylint: disable=attribute-defined-outside-init
