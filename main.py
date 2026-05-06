import tkinter as tk

root = tk.Tk()
root.title("BMI Health Calculator")


# Function
def calculate_bmi():
    try:
        mass = float(entry_mass.get())
        height_cm = float(entry_height.get())

        height_m = height_cm / 100
        bmi = mass / (height_m ** 2)

        result = f"BMI: {bmi:.2f}"

        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result += f"\nCategory: {category}"

        # Extra message if checkbox checked
        if advice_var.get() == 1:
            result += "\nStay healthy and active!"

        label_result["text"] = result

    except ValueError:
        label_result["text"] = "Enter valid numbers"


# ---- Widgets ----

# Mass
tk.Label(root, text="Mass (kg):").grid(row=0, column=0)
entry_mass = tk.Entry(root)
entry_mass.grid(row=0, column=1)

# Height
tk.Label(root, text="Height (cm):").grid(row=1, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1)

# Radiobutton (Gender)
tk.Label(root, text="Gender:").grid(row=2, column=0)

gender_var = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2)

# OptionMenu (Activity)
tk.Label(root, text="Activity Level:").grid(row=3, column=0)

activity_var = tk.StringVar(value="Low")

tk.OptionMenu(root, activity_var, "Low", "Medium", "High").grid(row=3, column=1)

# Checkbutton
advice_var = tk.IntVar()

tk.Checkbutton(root, text="Show health advice", variable=advice_var).grid(row=4, column=0)

# Button
# Output Label
# Run
