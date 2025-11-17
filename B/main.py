import array
from math import gcd

class CargoCraftPredictor:
  craft_a = 4
  craft_b = 6

  # Calculate combination of crafts based on first and second crafts in order
  def calculate_craft_combination(self, unit: int, primary_craft: int, secondary_craft: int) -> int:
    # Cover edge cases
    if unit == 0:
        return 0

    # Using Greatest Common Divisor to check if there is a solution
    g = gcd(primary_craft, secondary_craft)
    if unit % g != 0:
        return -1
    
    # Get maximum divison of based on primary craft first
    primary_count = unit // primary_craft

    # Range from 0 to maximum division
    for count in range(0, primary_count + 1):
      remainder = unit - count * primary_craft

      # Return the total if remainder is 0
      if remainder % secondary_craft == 0:
        total = count + remainder // secondary_craft
        return total
  
    return -1

  # Return the max combination of crafts
  def predict_max_craft(self, unit: int) -> int:
    return self.calculate_craft_combination(unit, self.craft_b, self.craft_a)

  # Return the min combination of crafts
  def predict_min_craft(self, unit: int) -> int:
    return self.calculate_craft_combination(unit, self.craft_a, self.craft_b)

def process_inputs(input: array) -> str | None:
  results = []
  try:
    for item in input:
      unit = int(item)
      cargo_craft_calculator = CargoCraftPredictor()
      min_craft = cargo_craft_calculator.predict_min_craft(unit=unit)
      max_craft = cargo_craft_calculator.predict_max_craft(unit=unit)

      if min_craft == -1 and max_craft == -1:
        results.append(min_craft)
      else:
        # If one of min_craft or max_craft is -1, use the other for both min and max
        min_val = min_craft if min_craft != -1 else max_craft
        max_val = max_craft if max_craft != -1 else min_craft
        results.append(f"{min_val} {max_val}")

  except ValueError:
    print("Error: Invalid input.")
    return None

  return results

def main():
  while True:
    try:
      # Read for user inputs
      number_of_line = int(input("Please enter the number of lines and then the lines, each on its own line:\n").strip())

      # Validate number of line
      if number_of_line < 1 or number_of_line > 1000: 
        print("Number of test cases must be minimum 1 and maximum 1000.")
        continue

      inputs = [input() for _ in range(number_of_line)]
      results = process_inputs(inputs)

      print("Output:")
      print(*results, sep="\n")
      break
    except ValueError:
      print("Invalid input. Please re-enter your input.")
      continue
    except Exception as e:
      print("Invalid input. Please re-enter your input.")
      continue

if __name__ == "__main__":
  main()