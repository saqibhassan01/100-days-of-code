import requests
import tabulate as tb  # Renaming the tabulate module to 'tb'

class Main:
    def __init__(self):
        # Initializing the base_currency and response variables
        self.base_currency = None
        self.response = None
        self.index_counter = 1  # Initialize the global index counter

    def converter(self):
        while True:
            try:
                # Prompting the user for the currency they want to convert
                self.base_currency = input("Enter the currency you want to convert: ").upper()

                # Constructing the API URL with the selected base currency and an API key
                url = f"https://open.er-api.com/v6/latest/{self.base_currency}?apikey=9fbf79be1ca546c497ea0036397224c5"

                # Sending a GET request to the API
                api = requests.get(url)

                # Parsing the JSON response from the API
                data = api.json()

                # Checking if the base currency is valid
                if self.base_currency in data["rates"]:
                    break
                else:
                    # Informing the user if the base currency is not valid
                    print("Invalid Currency Name")

            except KeyError:
                # Informing the user if there's an issue with the API response
                print("An error occurred while fetching exchange rates. Please try again later.")
        
        while True:
            choice = input("1. Do you want to see list of all rates.\n2. Or you want to see specific currency.(1/2)\n")
            if choice == "1":
                # Extract the list of currency names and their corresponding rates
                currency_names = list(data["rates"].keys())
                currency_rates = list(data["rates"].values())

                # Define the number of names to display on each page
                names_per_page = 15

                # Split the names and rates into chunks of 15 names each
                name_chunks = [currency_names[i:i + names_per_page] for i in range(0, len(currency_names), names_per_page)]
                rate_chunks = [currency_rates[i:i + names_per_page] for i in range(0, len(currency_rates), names_per_page)]

                # Initialize the current page to 1
                current_page = 1

                while True:
                    # Display the current page
                    if current_page > len(name_chunks):
                        print("Invalid page number. Please enter a valid page number.")
                    else:
                        names_chunk = name_chunks[current_page - 1]
                        rates_chunk = rate_chunks[current_page - 1]

                        print(f"Page {current_page}:")
                        data = list(enumerate(zip(names_chunk, rates_chunk), start=self.index_counter))
                        formatted_data = [(index, name, rate) for index, (name, rate) in data]
                        table = tb.tabulate(formatted_data, headers=["Index", "Currency Name", "Rate"], tablefmt="grid", floatfmt=".6f")
                        print(table)
                        print("\n")

                        # Increment the global index counter
                        self.index_counter += len(names_chunk)

                    # Prompt the user for input
                    user_input = input("Enter 'next' for the next page, 'prev' for the previous page, or 'quit' to exit: ").lower()

                    if user_input == 'next':
                        current_page += 1
                    elif user_input == 'prev':
                        current_page -= 1
                    elif user_input == 'quit':
                        break
                    else:
                        print("Invalid input. Please enter 'next', 'prev', or 'quit'.")
            elif choice == "2":
                while True:
                    # Prompting the user for the target currency
                    target_currency = input("Enter the currency you want to convert to: ").upper()

                    # Checking if the target currency is valid
                    if target_currency in data["rates"]:
                        # Retrieving the exchange rate for the target currency
                        exchange_rate = data["rates"][target_currency]

                        # Displaying the exchange rate to the user
                        print(f"Exchange rate for {target_currency}: {exchange_rate}")
                        break
                    else:
                        # Informing the user if the target currency is not valid
                        print(f"{target_currency} is not a valid currency code.")
            else:
                print("Invalid Input")
            break

# Creating an instance of the Main class
main = Main()

# Calling the converter method to fetch and display exchange rates
main.converter()
