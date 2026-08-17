import json
import os


# ==========================================================
# SETTINGS FILE
# ==========================================================

SETTINGS_FILE = os.path.join(
    "config",
    "settings.json",
)


# ==========================================================
# DEFAULT SETTINGS
# ==========================================================

DEFAULT_SETTINGS = {

    "company_name": "MICT E-LEARNING SERVICES LTD",

    "dashboard_title": "Enterprise Sales Analytics",

    "currency": "₦ Nigerian Naira",

    "report_language": "English",

    "show_kpis": True,

    "show_summaries": True,

    "show_ai_insights": True,

    "show_charts": True,

    "include_logo": True,

    "include_footer": True,

    "include_page_numbers": True,

    "include_generation_date": True,
}


# ==========================================================
# ENSURE CONFIGURATION DIRECTORY
# ==========================================================

def ensure_config_directory():

    directory = os.path.dirname(
        SETTINGS_FILE
    )

    if directory:
        os.makedirs(
            directory,
            exist_ok=True,
        )


# ==========================================================
# LOAD SETTINGS
# ==========================================================

def load_settings():

    ensure_config_directory()

    if not os.path.exists(
        SETTINGS_FILE
    ):

        save_settings(
            DEFAULT_SETTINGS
        )

        return DEFAULT_SETTINGS.copy()

    try:

        with open(
            SETTINGS_FILE,
            "r",
            encoding="utf-8",
        ) as file:

            settings = json.load(file)

        # Make sure newly added settings
        # receive their default values.

        for key, value in DEFAULT_SETTINGS.items():

            if key not in settings:

                settings[key] = value

        return settings

    except (
        json.JSONDecodeError,
        OSError,
    ):

        return DEFAULT_SETTINGS.copy()


# ==========================================================
# SAVE SETTINGS
# ==========================================================

def save_settings(settings):

    ensure_config_directory()

    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            settings,
            file,
            indent=4,
            ensure_ascii=False,
        )


# ==========================================================
# UPDATE SETTINGS
# ==========================================================

def update_settings(updates):

    settings = load_settings()

    settings.update(
        updates
    )

    save_settings(
        settings
    )

    return settings


# ==========================================================
# GET SINGLE SETTING
# ==========================================================

def get_setting(
    key,
    default=None,
):

    settings = load_settings()

    return settings.get(
        key,
        default,
    )


# ==========================================================
# RESET SETTINGS
# ==========================================================

def reset_settings():

    settings = DEFAULT_SETTINGS.copy()

    save_settings(
        settings
    )

    return settings
# ==========================================================
# CURRENCY HELPERS
# ==========================================================

def currency_symbol():

    currency = get_setting(
        "currency",
        "₦ Nigerian Naira",
    )

    symbols = {
        "₦ Nigerian Naira": "₦",
        "$ US Dollar": "$",
        "€ Euro": "€",
        "£ British Pound": "£",
    }

    return symbols.get(
        currency,
        "₦",
    )


def format_currency(
    value,
    decimals=2,
):

    symbol = currency_symbol()

    return (
        f"{symbol}"
        f"{value:,.{decimals}f}"
    )
    
    