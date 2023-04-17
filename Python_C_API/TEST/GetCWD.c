#include <unistd.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char GeneratedKey[16] = {0};

int main()
{
/*
	char* cwd = get_current_dir_name();
	printf("Current working directory: %s\n", cwd);
        free(cwd);
*/
char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Current working directory: %s\n", cwd);
    } else {
        perror("getcwd() error");
        return 1;
    }
    char Key[16] = ReadKey();
    return 0;
}

unsigned char *ReadKey(void)
{
	char cwd[1024];
	    if (getcwd(cwd, sizeof(cwd)) != NULL) {
		printf("Current working directory: %s\n", cwd);
	    } else {
		perror("getcwd() error");
		//return 1;
	    }
    	
    
	FILE *file;
	file = fopen(strcat(cwd,"/key.txt"), "r");
	fgets(GeneratedKey, 128, file);
	printf("GeneratedKey :\n");
	for (int i = 0; i < 16; i++) {
		printf("%02x ", GeneratedKey[i]);
	}
	printf("\n");
	printf("size of key = %ld \n", sizeof(GeneratedKey));
	//system("rm -v /home/amalr/Desktop/PythonTraining/Python_C_API/TEST/key.txt"); /*Remove the temporary file,and doesnt send it to trash folder,so no one else can access the random key*/
	return GeneratedKey;
}
