#include <iostream>
#include <string>

int get_number(std::string number) { return std::stoi(number); }

int main() {

#ifndef JUDGE
#define JUDGE
  freopen("in.in", "r", stdin);
  freopen("out.out", "w", stdout);
#endif
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(NULL);

  std::string input;

  int count_zero = 0;

  int sum = 50;

  while (std::getline(std::cin, input)) {
    std::string number(input.begin() + 1, input.end());
    // int num = get_number(number);
    //
    // if (input[0] == 'R') {
    //       } else {
    //
    // }
    //
    std::cout << number << std::endl;
  }

  return 0;
}
