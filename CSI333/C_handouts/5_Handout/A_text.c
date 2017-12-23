#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* The segment of code shown below indicates how the standard library functions malloc and free
   are used to dynamically allocate and deallocate memory in C programs. */


int main(void) {

  int *x;
  x = (int *) malloc(sizeof(int));
  if (x == NULL) {
    printf("Allocation failed.\n"); exit(1);
  }
  else {
    printf("you got it working\n");
  /* Can use *x here. */
  }

  free(x); /* Frees the storage pointed to by x. */
  return 0;
}
