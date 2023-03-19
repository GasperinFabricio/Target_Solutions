#include <stdio.h>
#include <string.h>


int main(void) {
  char str[] = "tolo";
  char ace;
  int outmostRight = strlen(str) - 1;

  for(int i = 0; i < outmostRight; i++) {
    char jar = str[i];
    str[i] = str[outmostRight];
    str[outmostRight] = jar;
    outmostRight--;
    }

  puts(str);

  
  
    

  
  
  return 0;
}