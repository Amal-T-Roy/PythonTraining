CC = gcc
CFLAGS = -Wall -Wextra -Werror
LDFLAGS = -I/usr/include/python3.8 -lpython3.8

test_my_program: main.c
	$(CC) $(CFLAGS) main.c -o main  $(LDFLAGS) 

.PHONY: clean
clean:
	rm -f main



