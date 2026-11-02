# SMART UMBRELLA 2050
# A futuristic umbrella that detects weather conditions

def get_weather_data():
    print("\n--- Weather Detection ---")

    temperature = float(input("Enter temperature (°C): "))
    uv_level = int(input("Enter UV level (0-11): "))
    rain = input("Is it raining? (yes/no): ").lower()
    thunderstorm = input("Is there a thunderstorm? (yes/no): ").lower()

    return temperature, uv_level, rain, thunderstorm


def detect_conditions(temperature, uv_level, rain, thunderstorm):
    print("\n--- Smart Umbrella Response ---")

    if thunderstorm == "yes":
        print("RED ALERT: Thunderstorm detected!")
        print("Do not use the umbrella.")
        print("Seek safe shelter.")

    elif temperature >= 32 and uv_level >= 6:
        print("HIGH HEAT AND UV DETECTED!")
        print("Heat-reflective coating and UV protection recommended.")
        print("LED colour: RED")

    elif temperature >= 32:
        print("HIGH TEMPERATURE DETECTED!")
        print("Heat protection recommended.")
        print("LED colour: YELLOW")

    elif uv_level >= 6:
        print("HIGH UV LEVEL DETECTED!")
        print("UV protection recommended.")
        print("LED colour: YELLOW")

    elif rain == "yes":
        print("RAIN DETECTED!")
        print("Waterproof umbrella mode recommended.")
        print("LED colour: BLUE")

    else:
        print("Normal weather conditions.")
        print("LED colour: GREEN")


def main():
    print("=== SMART UMBRELLA 2050 ===")
    print("Your intelligent weather protection system!")

    while True:
        temperature, uv_level, rain, thunderstorm = get_weather_data()

        detect_conditions(temperature, uv_level, rain, thunderstorm)

        again = input("\nCheck weather again? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Smart Umbrella 2050!")
            break


main()