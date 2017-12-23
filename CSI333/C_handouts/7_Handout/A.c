#include <stdio.h>
#include <stdlib.h> 
#include <string.h> 
#define MAXLEN 81

#define NUMARG 4
#define IN_FILE_ARG 1
#define OUT_FILE_ARG 2
#define PATTERN_ARG 3
int main(int argc, char *argv[]){
  
  char line[MAXLEN];
  char tret[MAXLEN];
  int i =0; 
  FILE *finp, *foutp; 
  if (argc != NUMARG) {
    printf("Usage: findpat infile outfile pattern\n"); exit(1);
  }
  
  if ((finp = fopen(argv[IN_FILE_ARG], "r")) == NULL) {
    
    printf("Could not open file %s for reading.\n", argv[IN_FILE_ARG]); exit(1);
  }
  
    
    if ((foutp = fopen(argv[OUT_FILE_ARG], "w")) == NULL) {

      printf("Could not open file %s for writing.\n", argv[OUT_FILE_ARG]); exit(1);
    }
  
  while (fgets(line, MAXLEN, finp) != NULL) {
    if (strstr(line, argv[PATTERN_ARG]) != NULL) { 
      fputs(line, foutp);
    }
  }

  
  
  
  if (fclose(finp) == EOF) { 
    printf("Error in closing file input.dat.\n");
  }
  if (fclose(foutp) == EOF) { 
    printf("Error in closing file output.dat.\n");
  }
  return 0;
} 
