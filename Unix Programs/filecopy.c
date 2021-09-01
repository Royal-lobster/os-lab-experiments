#include<stdio.h>    
#include<stdlib.h>
int main(){    
    
    char ch, source_file[25], target_file[25];
    FILE *source, *target;    
    
    // Get the file that we are coping from
    printf("Enter name of file to copy\n");
    gets(source_file);    
    source = fopen(source_file, "r");

    if( source == NULL ){
        printf("Press any key to exit...\n");
        exit(EXIT_FAILURE);
    }
    
    // Get the file that we are coping to
    printf("Enter name of target file\n");
    gets(target_file);
    target = fopen(target_file, "w");
    
    if( target == NULL ){
        fclose(source);        
        printf("Press any key to exit...\n");        
        exit(EXIT_FAILURE);
    }    
    
    // Copy the file
    while((ch = fgetc(source)) != EOF)
        fputc(ch, target);

    // Indicate Success and Close the files
    printf("File copied successfully.\n");        
    fclose(source);        
    fclose(target);
    return 0;
}