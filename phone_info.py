import phonenumbers
from phonenumbers import geocoder, carrier, timezone

number = input("Enter phone number with country code: ")

try:
    phone = phonenumbers.parse(number, None)

    print("\n--- Phone Number Information ---")
    print("International format:",
          phonenumbers.format_number(
              phone,
              phonenumbers.PhoneNumberFormat.INTERNATIONAL
          ))

    print("Valid number:",
          phonenumbers.is_valid_number(phone))

    print("Possible number:",
          phonenumbers.is_possible_number(phone))

    print("Region information:",
          geocoder.description_for_number(phone, "en"))

    print("Carrier information:",
          carrier.name_for_number(phone, "en"))

    print("Time zones:",
          timezone.time_zones_for_number(phone))

except phonenumbers.NumberParseException as error:
    print("Invalid input:", error)
