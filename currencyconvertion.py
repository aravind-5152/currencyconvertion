        
    def display_result(self, amount, base_currency, target_currency, converted_amount):
        """Display the conversion result"""
        print("\n" + "="*50)
        print(f"Conversion Result:")
        print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        print("="*50 + "\n")
def main():
    # Replace with your API key from ExchangeRate-API
    API_KEY = "YOUR_API_KEY_HERE"
    
    converter = CurrencyConverter(API_KEY)
    
    print("Currency Converter")
    print("-----------------")
    
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            base_currency = input("Enter source currency code (e.g. USD, EUR): ").strip().upper()
            target_currency = input("Enter target currency code (e.g. GBP, JPY): ").strip().upper()
            
            converted_amount = converter.convert_currency(amount, base_currency, target_currency)
            if converted_amount is not None:
                converter.display_result(amount, base_currency, target_currency, converted_amount)
            
            another = input("Do you want to perform another conversion? (y/n): ").lower()
            if another != 'y':
                print("Thank you for using the Currency Converter!")
                break
                
        except ValueError:
            print("Error: Please enter a valid number for the amount")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user")
            break
if __name__ == "__main__":
    main()
