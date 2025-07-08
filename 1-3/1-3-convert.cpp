//Christiel Podieu  - 6/18/2025
//CS 210, May 2025
//
//Submitted for use in CS 630 by Matthew Heusser, July 2025
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Function to convert Fahrenheit to Celsius
double fahrenheitToCelsius(int fahrenheit) {
    return (fahrenheit - 32) * 5.0 / 9.0;
}

int main() {
    ifstream inputFile("FahrenheitTemperature.txt");
    ofstream outputFile("CelsiusTemperature.txt");

    string city;
    int fahrenheit;

    // Check if files opened correctly
    if (!inputFile) {
        cerr << "Error opening input file.\n";
        return 1;
    }
    if (!outputFile) {
        cerr << "Error opening output file.\n";
        return 1;
    }

    // Read data and convert
    while (inputFile >> city >> fahrenheit) {
        double celsius = fahrenheitToCelsius(fahrenheit);
        outputFile << city << " " << celsius << endl;
    }

    inputFile.close();
    outputFile.close();

    cout << "Temperature conversion complete." << endl;
    return 0;
}
