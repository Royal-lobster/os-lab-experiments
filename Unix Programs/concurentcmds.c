#include <stdio.h>
#include <fcntl.h>
main()
{
    int processFileDescriptor[2], processID;
    pipe(processFileDescriptor);
    processID = fork();
    if (processID == 0){
        close(processFileDescriptor[0]);
        close(1);
        dup(processFileDescriptor[1]);
        execlp("ls", "ls", "-l", (char *)0);
    }
    else{
        close(processFileDescriptor[1]);
        close(0);
        dup(processFileDescriptor[0]);
        execlp("sort", "sort", (char *)0);
    }
}