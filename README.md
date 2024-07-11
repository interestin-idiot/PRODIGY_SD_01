# Software Development Intern At Prodigy Infotech

## Task 1 : Build a Temperature Conversion Program
Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales. The program should prompt the user to input a temperature value and the original unit of measurement. It should then convert the temperature to the other two units and display the converted values to the user. For example, if the user enters a temperature of 25 degrees Celsius, the program should convert it to Fahrenheit and Kelvin, and present the converted values as outputs.

# Dependencies

1.Python 3.12
      
2.Pyside6

# Project Overview 

## Objectives:
1. **User-Friendly Design**: Create an easy-to-use interface for converting temperatures between different units.
2. **Input and Output**: Allow users to enter temperatures and see the converted results immediately.
3. **Accuracy**: Ensure the conversions are precise and reliable.
4. **Multiple Conversions**: Enable conversions from one temperature scale to the other two (Fahrenheit, Celsius, Kelvin).
5. **Clear Instructions**: Provide clear guidance and feedback to users throughout the process.

# Project Structure
## Main Interface:

1. **Title and Instructions**: Display the application's title and instructions for the user.
2. **Input Fields**: Provide areas where users can enter temperatures in Fahrenheit, Celsius, or Kelvin.
3. **Convert Button**: A button that users can press to perform the conversion.
4. **Result Display**: Show the converted temperature values.

## Conversion Logic:

1. **User Input**: Users can enter a temperature value in one of the input fields.
2. **Perform Conversion**: The application calculates the equivalent temperatures in the other scales.
3. **Display Results**: The converted temperatures are shown to the user.
4. **Error Handling:** If the input is invalid or outside a reasonable range, the application informs the user and asks for a correct value.

# Implementation Details
## Interface Setup:

1. The main window is set up to be visually appealing and easy to understand.
2. Input fields are provided for users to type in their temperatures.
3. A button is available to trigger the conversion process.
4. The results are displayed clearly for the user to see.
## Game Flow:

1. When the application starts, users can see three input fields for entering temperatures in Fahrenheit, Celsius, or Kelvin.
2. Users type a temperature in one of the fields and press the convert button.
3. The application processes the input and displays the equivalent temperatures in the other two scales.
4. If the input is not valid (e.g., not a number), the application prompts the user to enter a correct value.
## Feedback and Messages:

1. Clear instructions guide the user on what to do.
2. The application informs the user if the input is incorrect or if there are any issues with the conversion.
3. Accurate results are displayed, allowing the user to see the converted temperatures immediately.
