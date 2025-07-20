//Matthew Heusser - 7/20/2025
//For use in CS 630 by Matthew Heusser 

#include <iostream>
#include <fstream>
char location[80];
double f;

//-----------------------------------//
int main() 
//-----------------------------------//
{ 
    std::ifstream input("FahrenheitList.txt");
    std::ofstream output("CelsiusList.txt");

    while (input >> location >> f) {
        double c = (f-32)* 5 / 9;
        output << location << " " << c << std::endl;
    }

    std::cout << "Done." << std::endl;
    
    return 0;
}
