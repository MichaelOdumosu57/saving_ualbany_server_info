#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main(void) {

  int *x;
  x = (int *) malloc(sizeof(int));
  if (x == NULL) {
    printf("Allocation failed.\n"); exit(1);
  }
  else {
    printf("you got it working\n");
 
  }

  free(x); /* Frees the storage pointed to by x. */
  return 0;
}
