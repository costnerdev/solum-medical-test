import array

class MagicalEnergyCalculator:
  energy: int
  number_of_wave:int

  def __init__(self, energy: int, number_of_wave: int) -> None:
    # Validate energy and number_of_wave range
    if not (1 <= energy <= 10):
      raise ValueError("Energy input is invalid")

    if not (1 <= number_of_wave <= 10):
      raise ValueError("Length of wave input is invalid")

    self.energy = energy
    self.number_of_wave = number_of_wave

  # Calculate total magical energy based on number of waves
  def calculate_magical_energy(self) -> int:
    return self.energy if self.number_of_wave % 2 != 0 else 0 

def process_inputs(input: array) -> str | None:
  results = []
  try:
    for index, item in enumerate(input, 1):
      parts = item.strip().split()

      # Validate if item is valid
      if len(parts) != 2:
        print(f"Error: Line {index} must contain two numbers separated by a space.\nPlease re-enter your input.")
        continue
     
      energy, waves = map(int, parts)
      magical_energy_calculator = MagicalEnergyCalculator(energy=energy, number_of_wave=waves)
      magical_energy = magical_energy_calculator.calculate_magical_energy()
      results.append(magical_energy)

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
      if number_of_line < 1 or number_of_line > 100: 
        print("Number of test cases must be minimum 1 and maximum 100.")
        continue

      inputs = [input() for _ in range(number_of_line)]
      results = process_inputs(inputs)
      print("Output:")
      print(*results, sep="\n")
      break
    except ValueError:
      print("Invalid input. Please re-enter your input.")
      continue
    except Exception:
      print("Invalid input. Please re-enter your input.")
      continue

if __name__ == "__main__":
  main()