#include<Python.h>

void main()
{

//Initialise
Py_Initialize();

//Create file pointer of python script
FILE* fp = fopen("module_name.py","r");

//Run file
PyRun_SimpleFile(fp,"module_name.py");
fclose(fp);

PyObject* module = PyImport_ImportModule("module_name ");
PyObject* function = PyObject_GetAttrString(module, "function_name ");

// call the function and get its return value
    PyObject* args = PyTuple_New(0);
    PyObject* result = PyObject_CallObject(function, args);

    // print the result
    printf("The result is %ld\n", PyLong_AsLong(result));

//Close
Py_Finalize(); 

}
