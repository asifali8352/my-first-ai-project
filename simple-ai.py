# My first AI model!
# Let's make an AI that predicts if someone will like ice cream
# based on the temperature outside

def ice_cream_predictor(temperature):
    """
    This is our simple AI brain!
    It takes the temperature and predicts if you'd want ice cream
    """
    if temperature >= 25:  # Hot day
        return "🍦 Perfect ice cream weather! You'll definitely want some!"
    elif temperature >= 15:  # Warm day  
        return "🤔 Maybe some ice cream? It's pretty nice outside!"
    elif temperature >= 5:   # Cool day
        return "🧥 Probably too cool for ice cream, maybe hot chocolate?"
    else:  # Cold day
        return "❄️ Way too cold for ice cream! Hot soup time!"

# Let's test our AI!
print("🤖 Welcome to the Ice Cream Prediction AI!")
print("-" * 40)

# Test with different temperatures
test_temperatures = [30, 20, 10, 0, -5]

for temp in test_temperatures:
    prediction = ice_cream_predictor(temp)
    print(f"Temperature: {temp}°C → {prediction}")

print("\n" + "=" * 50)    
print("🎉 Congratulations! You just made your first AI model!")


# Make it interactive - let the user input temperature
print("\n🎮 Interactive Mode!")
print("Enter a temperature and I'll predict your ice cream mood!")

while True:
    try:
        user_temp = float(input("\nWhat's the temperature today? (or type 'quit' to exit): "))
        result = ice_cream_predictor(user_temp)
        print(result)
    except ValueError:
        print("👋 Thanks for using the Ice Cream Predictor AI!")
        break
    except:
        print("Please enter a valid number!")
